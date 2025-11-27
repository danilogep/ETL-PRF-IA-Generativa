import asyncio
import google.generativeai as genai
from tenacity import retry, stop_after_attempt, wait_fixed
from src.config import GOOGLE_API_KEY

# 1. Configura a biblioteca do Google
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("models/gemini-2.0-flash-001")


# --- CONFIGURAÇÃO DE RETENTATIVA ---
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
async def gerar_mensagem(motorista: dict):
    """
    Gera mensagem usando Google Gemini.
    """
    nome = motorista["Nome"]
    veiculo = motorista["Veiculo"]

    # Pegamos os dados do local ---
    # Usamos .get() caso o dado não exista (prevenção de erro)
    br = motorista.get("BR", "Rodovia")
    km = motorista.get("KM", "?")
    municipio = motorista.get("Municipio", "Região")
    causa_risco = motorista.get("Causa_Frequente", "acidentes diversos")

    prompt = (
        f"Você é um policial rodoviário experiente da PRF."
        f"Gere um alerta curto e impactante (máximo 20 palavras) para {nome}, "
        f"que dirige um {veiculo}."
        f"CONTEXTO: O motorista está passando pela BR-{br} no KM {km} ({municipio}). "
        f"Neste local, o histórico mostra muitos acidentes causados por: '{causa_risco}'."
        f"A mensagem deve alertar especificamente sobre esse risco."
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
