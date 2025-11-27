import asyncio
import time
from src.extract import carregar_dados
from src.transform import processar_dados
from src.load import salvar_resultados


async def main():
    print("=" * 50)
    print("🚔 INICIANDO PIPELINE DE DADOS PRF - ENTERPRISE")
    print("=" * 50)

    inicio = time.time()

    # 1. EXTRACT (Síncrono)
    dados_brutos = carregar_dados()

    if not dados_brutos:
        print("Fluxo interrompido por falta de dados.")
        return

    # 2. TRANSFORM (Assíncrono - Rápido)
    dados_enriquecidos = await processar_dados(dados_brutos)

    # 3. LOAD (Síncrono)
    salvar_resultados(dados_enriquecidos)

    fim = time.time()
    print("=" * 50)
    print(f"🏁 Processo finalizado em {fim - inicio:.2f} segundos.")
    print("=" * 50)


if __name__ == "__main__":
    # É aqui que o Python começa a rodar o modo assíncrono
    asyncio.run(main())
