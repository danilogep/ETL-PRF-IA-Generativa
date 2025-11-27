import pandas as pd
from typing import List, Dict
from src.config import INPUT_FILE


def carregar_dados() -> List[Dict]:
    """
    Lê o arquivo CSV definido em config.INPUT_FILE e retorna uma lista de dicionários.
    """
    print(f"🔄 Iniciando leitura do arquivo: {INPUT_FILE}")

    try:
        df = pd.read_csv(INPUT_FILE)

        # Validação básica
        colunas_obrigatorias = ["Nome", "Veiculo", "Placa"]
        colunas_existentes = df.columns.tolist()

        for coluna in colunas_obrigatorias:
            if coluna not in colunas_existentes:
                raise ValueError(
                    f"❌ ERRO: A coluna '{coluna}' não foi encontrada no CSV!"
                )

        dados = df.to_dict("records")
        print(f"✅ Sucesso! {len(dados)} registros carregados.")
        return dados

    except FileNotFoundError:
        print(f"❌ ERRO CRÍTICO: O arquivo não foi encontrado em: {INPUT_FILE}")
        return []
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return []
