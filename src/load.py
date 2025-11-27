import pandas as pd
import matplotlib.pyplot as plt
from src.config import OUTPUT_FILE, DATA_DIR


def salvar_resultados(dados: list):
    """
    Salva o CSV final e gera um gráfico de resumo.
    """
    if not dados:
        print("⚠️ Nenhum dado para salvar.")
        return

    # 1. Salvar CSV
    df = pd.DataFrame(dados)
    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
    print(f"💾 Arquivo CSV salvo com sucesso em: {OUTPUT_FILE}")

    # 2. Gerar Gráfico
    # Vamos contar quantos veículos de cada tipo foram abordados
    try:
        plt.figure(figsize=(10, 6))
        contagem = df["Veiculo"].value_counts()

        # Cria um gráfico de barras
        contagem.plot(kind="bar", color="skyblue")
        plt.title("Veículos Abordados - Relatório Automático")
        plt.xlabel("Modelo do Veículo")
        plt.ylabel("Quantidade")
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Salva a imagem na pasta data
        caminho_grafico = DATA_DIR / "relatorio_grafico.png"
        plt.savefig(caminho_grafico)
        print(f"📊 Gráfico gerado com sucesso em: {caminho_grafico}")

    except Exception as e:
        print(f"⚠️ Não foi possível gerar o gráfico: {e}")
