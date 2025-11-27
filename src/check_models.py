import google.generativeai as genai
from src.config import GOOGLE_API_KEY

# Configura a chave
genai.configure(api_key=GOOGLE_API_KEY)

print("🔍 Buscando modelos disponíveis para sua chave...")

try:
    # Lista todos os modelos que sua chave tem acesso
    found = False
    for m in genai.list_models():
        # Filtra apenas modelos que geram texto (chat)
        if "generateContent" in m.supported_generation_methods:
            print(f"✅ Disponível: {m.name}")
            found = True

    if not found:
        print("⚠️ Nenhum modelo de geração de texto encontrado para esta chave.")

except Exception as e:
    print(f"❌ Erro ao conectar na API: {e}")
    print("Verifique se sua chave no .env está correta e sem espaços extras.")
