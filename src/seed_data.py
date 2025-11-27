import pandas as pd
import random
from src.config import DATA_DIR

# Configurações
ARQUIVO_SAIDA = DATA_DIR / "dados_prf.csv"
ARQUIVOS_ACIDENTES = [DATA_DIR / "datatran2024.csv", DATA_DIR / "datatran2025.csv"]

# Dados fictícios para gerar aleatoriedade
NOMES = [
    "Carlos Silva",
    "Ana Souza",
    "Bruno Lima",
    "Mariana Costa",
    "Pedro Santos",
    "Julia Oliveira",
    "Ricardo Almeida",
    "Fernanda Pereira",
    "Lucas Gomes",
    "Patricia Rocha",
]
VEICULOS = [
    "Honda Civic",
    "Toyota Corolla",
    "Fiat Strada",
    "VW Gol",
    "Chevrolet Onix",
    "Jeep Compass",
    "Hyundai Creta",
    "Ford Ranger",
    "Nissan Kicks",
    "Renault Kwid",
]
PLACAS_LETRAS = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX"]


def gerar_placa():
    letras = random.choice(PLACAS_LETRAS)
    numeros = random.randint(1000, 9999)
    return f"{letras}-{numeros}"


def gerar_dataset_ficticio():
    print("🔄 Lendo dados reais de acidentes (Datatran)...")
    dfs = []

    for arquivo in ARQUIVOS_ACIDENTES:
        try:
            # Datatran usa separador ';' e encoding latin1 ou utf-8
            df = pd.read_csv(arquivo, sep=";", encoding="latin1", low_memory=False)
            dfs.append(df)
        except Exception as e:
            print(f"⚠️ Erro ao ler {arquivo.name}: {e}")

    if not dfs:
        print("❌ Nenhum arquivo de acidentes encontrado na pasta data/.")
        return

    df_total = pd.concat(dfs)

    # Vamos pegar uma amostra de 50 acidentes para usar como base para nossas "abordagens"
    # Focamos nas colunas que dão contexto: Onde foi? Qual a causa comum lá?
    amostra = df_total.sample(50)[
        ["uf", "br", "km", "municipio", "causa_acidente", "tipo_acidente"]
    ]

    novos_dados = []

    print("🛠️ Gerando motoristas fictícios baseados nos locais de risco...")

    count = 1
    for _, row in amostra.iterrows():
        motorista = {
            "UserID": count,
            "Nome": random.choice(NOMES),
            "Veiculo": random.choice(VEICULOS),
            "Placa": gerar_placa(),
            "Data": "2025-11-27",  # Data fictícia da abordagem
            "Horario": f"{random.randint(6, 22):02d}:{random.randint(0, 59):02d}",
            "UF": row["uf"],
            "BR": row["br"],
            "KM": row["km"],
            "Municipio": row["municipio"],
            "Causa_Frequente": row["causa_acidente"],
        }
        novos_dados.append(motorista)
        count += 1

    # Salva o novo arquivo dados_prf.csv
    df_final = pd.DataFrame(novos_dados)

    try:
        df_final.to_csv(ARQUIVO_SAIDA, index=False)
        print(
            f"✅ Sucesso! Novo arquivo '{ARQUIVO_SAIDA}' gerado com {len(df_final)} registros."
        )
        print("Exemplo de contexto adicionado:")
        print(df_final[["BR", "KM", "Causa_Frequente"]].head(3))

    except PermissionError:
        print("❌ ERRO DE PERMISSÃO:")
        print(
            f"O arquivo '{ARQUIVO_SAIDA}' está aberto em outro programa (provavelmente Excel)."
        )
        print("➡️  Feche o arquivo e tente rodar o script novamente.")


if __name__ == "__main__":
    gerar_dataset_ficticio()
