import pandas as pd
import json
from openai import OpenAI

# ---------------------------------------------------------------------------
# PASSO 1: EXTRACT - Extrair os dados do arquivo CSV
# ---------------------------------------------------------------------------

try:
    # Lê o arquivo CSV para um DataFrame do pandas
    df = pd.read_csv('dados_prf.csv')

    # Converte o DataFrame para uma lista de dicionários (similar a um JSON)
    # O método 'records' cria exatamente a estrutura que precisamos
    motoristas = df.to_dict('records')

    # Exibe os dados extraídos de forma organizada para verificação
    print("--- DADOS EXTRAÍDOS ---")
    print(json.dumps(motoristas, indent=2))
except:
    print("Erro: Arquivo 'dados_prf.csv' não encontrado. Crie o arquivo e tente novamente.")
    exit()

# ---------------------------------------------------------------------------
# PASSO 2: TRANSFORM - Gerar mensagens personalizadas com IA
# ---------------------------------------------------------------------------

# Coloquei minha chave da API da OpenAI apenas para TESTE. Se for utilizar o código, mude para a sua chave.

MINHA_CHAVE_API = 'COLOQUE AQUI A SUA KEY'
try:
    # Inicializar o cliente, passando sua chave de API
    client = OpenAI(api_key=MINHA_CHAVE_API)
except Exception as e:
    print(f"Erro ao inicializar o cliente da OpenAI. Verifique sua chave. Erro: {e}")
    # Se não conseguir inicializar, não adianta continuar.
    exit()

def gerar_mensagem_seguranca(motorista, openai_client):
  """
  Gera uma mensagem de segurança no trânsito usando a API da OpenAI.
  """
  try:
    completion = client.chat.completions.create(
        model="gpt-4o", # Você tem que colocar qual versão do GPT irá utilizar.
        messages=[
        {
            "role": "system",
            "content": "Você é um especialista em segurança no trânsito e Policial Rodoviário Federal."
        },
        {
            "role": "user",
            "content": f"Crie uma mensagem curta e impactante de segurança no trânsito para {motorista['Nome']}, que dirige um {motorista['Veiculo']}. A mensagem deve ser amigável e enfatizar a importância da direção segura. (máximo de 150 caracteres)"
        }
        ]
    )
    return completion.choices[0].message.content.strip()
  except Exception as e:
    print(f"Erro ao chamar a API da OpenAI para {motorista.get('Nome', 'um motorista')}: {e}")
    return "Lembre-se: a segurança no trânsito é responsabilidade de todos. Dirija com cuidado."

# Itera sobre cada motorista na nossa lista para gerar e adicionar a mensagem
print("\n--- GERANDO MENSAGENS PERSONALIZADAS ---")
for motorista in motoristas:
  # Passamos o 'motorista' e o 'client' da OpenAI para a função
  mensagem = gerar_mensagem_seguranca(motorista, client)
  # Adiciona a nova mensagem ao dicionário do motorista
  motorista['MensagemSeguranca'] = mensagem
  print(f"Mensagem para {motorista['Nome']}: {mensagem}")

# Exibe a estrutura de dados final, agora com as mensagens
print("\n--- DADOS TRANSFORMADOS E PRONTOS PARA CARREGAR---")
# Usamos ensure_ascii=False para garantir a correta exibição de acentos no print
print(json.dumps(motoristas, indent=2, ensure_ascii=False))

# ---------------------------------------------------------------------------
# PASSO 3: LOAD - Salvar os dados enriquecidos em um novo CSV
# ---------------------------------------------------------------------------

# Cria um novo DataFrame a partir da nossa lista de motoristas modificada
df_final = pd.DataFrame(motoristas)

# Salva o DataFrame em um novo arquivo CSV com codificação UTF-8
# index=False evita que o pandas adicione uma coluna de índice desnecessária
df_final.to_csv('resultados_prf.csv', index=False, encoding='utf-8-sig')

print("\n--- PROCESSO ETL CONCLUÍDO ---")
print("Os dados enriquecidos foram salvos com sucesso no arquivo 'resultados_prf.csv'!")