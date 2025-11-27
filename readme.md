# 🚔 Pipeline ETL - PRF (Enterprise Edition)

Projeto de Engenharia de Dados focado em segurança viária, utilizando **Python Assíncrono**, **IA Generativa (Google Gemini)** e **Arquitetura Modular**.

## 🚀 Sobre o Projeto
Este pipeline ETL (Extract, Transform, Load) processa dados de abordagens policiais e utiliza Inteligência Artificial para gerar mensagens de conscientização personalizadas para motoristas, visando a redução de acidentes.

Diferente de scripts básicos, este projeto foi arquitetado simulando um ambiente de produção real (Enterprise), com foco em **performance**, **segurança** e **escalabilidade**.

## 🏗️ Arquitetura e Tecnologias

O projeto segue uma arquitetura modularizada:

* **Linguagem:** Python 3.12+
* **IA Generativa:** Google Gemini 1.5 Flash (via API)
* **Processamento:** Assíncrono (`asyncio`) para alta performance.
* **Resiliência:** Implementação de *Retry Logic* com `tenacity` para falhas de rede.
* **Segurança:** Gestão de credenciais via Variáveis de Ambiente (`python-dotenv`).
* **Visualização:** Geração automática de relatórios gráficos com `matplotlib`.

## 📂 Estrutura do Projeto

```text
├── data/              # Armazenamento de arquivos (CSV e Imagens)
├── logs/              # Logs de execução
├── src/               # Código Fonte
│   ├── config.py      # Configurações centrais e variáveis de ambiente
│   ├── extract.py     # Leitura e validação de dados (Pandas)
│   ├── transform.py   # Lógica de IA Assíncrona (Google Gemini)
│   ├── load.py        # Salvamento de dados e geração de gráficos
│   └── pipeline.py    # Orquestrador principal
├── .env.example       # Modelo de variáveis de ambiente
├── requirements.txt   # Dependências do projeto
└── README.md          # Documentação
```

## ⚙️ Como Executar

### 1. Preparação

Clone o repositório e entre na pasta:

```bash
git clone [https://github.com/seu-usuario/seu-repo.git](https://github.com/seu-usuario/seu-repo.git)
cd seu-repo
```

### 2. Configuração do Ambiente Virtual

É recomendado usar um ambiente virtual para manter as bibliotecas isoladas.

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalação das Dependências

Instale todas as bibliotecas necessárias de uma vez:

```bash
pip install pandas google-generativeai python-dotenv tenacity matplotlib
```

### 4. Configuração de Segurança (API Key)

O projeto usa variáveis de ambiente para proteger sua chave de API.

1.  Crie um arquivo chamado `.env` na raiz do projeto (use o `.env.example` como base).
2.  Adicione sua chave do Google Gemini (AI Studio):

```ini
# Conteúdo do arquivo .env
GOOGLE_API_KEY=ColeSuaChaveAqui
```

### 5. Execução do Pipeline

Para rodar o processo completo (Extração -> IA -> Gráficos):

```bash
python -m src.pipeline
```

## 📊 Resultados Esperados

Ao final da execução, verifique a pasta `data/`:
* `resultados_prf.csv`: Dados enriquecidos com as mensagens da IA.
* `relatorio_grafico.png`: Gráfico estatístico das abordagens gerado automaticamente.

---
Desenvolvido com foco em boas práticas de Engenharia de Dados.