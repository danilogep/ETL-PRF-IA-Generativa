# 🚀 Projeto ETL de Segurança no Trânsito com IA Generativa

## Desafio Adaptado da Santander Dev Week 2023

Este projeto é uma adaptação do desafio "ETL com Python" proposto na Santander Dev Week 2023. O contexto original, focado em marketing bancário, foi reimaginado para a realidade da segurança pública, especificamente para o trabalho da Polícia Rodoviária Federal (PRF).

O objetivo deste pipeline de **ETL (Extract, Transform, Load)** é utilizar o poder da Inteligência Artificial Generativa para criar mensagens de segurança no trânsito personalizadas para motoristas, com base em dados fictícios de abordagens.

---

### 📋 Fluxo do Processo ETL

1.  **Extract:** Os dados de motoristas (Nome, Veículo, Placa, etc.) são extraídos de um arquivo de origem chamado `dados_prf.csv`.
2.  **Transform:** Para cada motorista, o script se conecta à API da OpenAI (utilizando o modelo GPT-4o) para gerar uma mensagem de segurança única e personalizada, levando em consideração o nome do condutor e o veículo. O código também possui um tratamento de erros robusto para lidar com falhas na API, garantindo a continuidade do processo.
3.  **Load:** Os dados originais, agora enriquecidos com a mensagem de segurança gerada pela IA, são carregados em um novo arquivo CSV chamado `resultados_prf.csv`.

---

### 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Bibliotecas:**
    * `pandas`: Para extração e manipulação de dados dos arquivos CSV.
    * `openai`: Para integração e consumo da API do GPT.
* **Inteligência Artificial:**
    * OpenAI GPT-4o

---

### ⚙️ Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:
* [Python 3.10+](https://www.python.org/downloads/)
* Uma conta na plataforma da [OpenAI](https://platform.openai.com/) e uma **chave de API** válida.

---

### 📝 Configuração do Ambiente

1.  **Clone este repositório (ou crie sua pasta de projeto):**
    ```bash
    # Se estiver usando git
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Crie o arquivo de dados de entrada:**
    Crie um arquivo na raiz do projeto chamado `dados_prf.csv` com o seguinte conteúdo:
    ```csv
    UserID,Nome,Veiculo,Placa,Horario,Data
    1,Carlos Silva,Honda Civic,ABC-1234,08:30,2025-10-06
    2,Mariana Costa,Fiat Strada,DEF-5678,14:15,2025-10-06
    3,João Pereira,Toyota Hilux,GHI-9012,19:45,2025-10-06
    4,Ana Souza,VW Gol,JKL-3456,22:00,2025-10-06
    ```

3.  **Instale as dependências:**
    No seu terminal, execute o comando abaixo para instalar as bibliotecas necessárias.
    ```bash
    pip install pandas openai
    ```

---

### ▶️ Como Executar o Projeto

1.  **Adicione sua Chave de API:**
    Abra o arquivo de script principal (ex: `main.py`) e insira sua chave da API da OpenAI na variável indicada:
    ```python
    MINHA_CHAVE_API = "sk-..." # Cole sua chave secreta aqui
    ```
    ⚠️ **Atenção:** Nunca exponha sua chave de API em repositórios públicos ou locais não seguros.

2.  **Execute o script:**
    Com tudo configurado, rode o script através do terminal:
    ```bash
    python main.py
    ```

### ✅ Resultado Esperado

Após a execução, o terminal irá exibir o progresso de cada etapa do ETL. Ao final, um novo arquivo chamado `resultados_prf.csv` será criado na pasta do projeto, contendo todos os dados originais mais uma nova coluna, `MensagemSeguranca`, com o texto gerado pela IA para cada motorista.