import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Tenta pegar a chave. Se não achar, retorna None.
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Validação simples: se a chave não existir, paramos o programa agora.
if not GOOGLE_API_KEY:
    raise ValueError("ERRO FATAL: A variável GOOGLE_API_KEY não foi encontrada no .env")

# Definições de caminhos (para não usar caminhos fixos no código)
import sys
from pathlib import Path

# Raiz do projeto (uma pasta acima da pasta src)
ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
LOG_DIR = ROOT_DIR / "logs"

# Caminhos dos arquivos
INPUT_FILE = DATA_DIR / "dados_prf.csv"
OUTPUT_FILE = DATA_DIR / "resultados_prf.csv"
LOG_FILE = LOG_DIR / "pipeline.log"
