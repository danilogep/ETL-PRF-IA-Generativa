import asyncio
import google.generativeai as genai
from tenacity import retry, stop_after_attempt, wait_fixed
from src.config import GOOGLE_API_KEY

# 1. Configura a biblioteca do Google
genai.configure(api_key=GOOGLE_API_KEY)

# 2. Escolhe o modelo (gemini-1.5-flash é rápido e ótimo para mensagens curtas)
model = genai.GenerativeModel("models/gemini-2.0-flash-001")


# --- CONFIGURAÇÃO DE RETENTATIVA ---
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
async def gerar_mensagem(motorista: dict):
    """
    Gera mensagem usando Google Gemini.
    """
    nome = motorista["Nome"]
    veiculo = motorista["Veiculo"]

    prompt = (
        f"Você é um policial rodoviário virtual educado. "
        f"Crie uma frase curta (máximo 15 palavras) de conscientização para {nome}, "
        f"que dirige um {veiculo}. Foque em segurança."
    )

    try:
        response = await model.generate_content_async(prompt)

        # O Gemini retorna o texto dentro de .text
        return response.text.strip()

    except Exception as e:
        print(f"⚠️ Erro ao gerar para {nome}: {e}")
        raise e


async def processar_dados(lista_motoristas: list):
    """
    Processa a lista de motoristas em paralelo.
    """
    print(
        f"🚀 Iniciando processamento com Google Gemini para {len(lista_motoristas)} registros..."
    )

    tarefas = []

    for motorista in lista_motoristas:
        tarefas.append(gerar_mensagem(motorista))

    # Executa tudo junto
    mensagens = await asyncio.gather(*tarefas)

    for i, motorista in enumerate(lista_motoristas):
        motorista["Mensagem_IA"] = mensagens[i]

    print("✅ Processamento da IA concluído!")
    return lista_motoristas
