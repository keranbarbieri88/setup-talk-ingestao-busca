# setup-talk-ingestao-busca
This project involves the ingestion and semantic search of data from a PDF document

# 📑 Pipeline de Ingestão e Busca Semântica (RAG)

Este projeto implementa uma solução completa de **RAG (Retrieval-Augmented Generation)** utilizando o framework **LangChain** para orquestração, **PostgreSQL (via Docker)** com a extensão **pgVector** como banco de dados vetorial, e a API do **Google Gemini** como motor de Inteligência Artificial.

O sistema é capaz de ler um arquivo PDF local, extrair seu conteúdo, transformá-lo em embeddings matemáticos, armazená-los no banco e expor uma interface de Chat via CLI (Linha de Comando) com regras estritas de contexto.

---

## 🛠️ Tecnologias e Recursos Utilizados

* **Linguagem:** Python 3.10 ou superior
* **Orquestrador:** LangChain (Interface unificada para o pipeline)
* **LLM & Embeddings:** Google Gemini (`gemini-2.5-flash` e `embedding-001`)
* **Banco de Dados Vetorial:** PostgreSQL + pgVector Extension
* **Ambiente e Infraestrutura:** Docker & Docker Compose

---

## 🚀 Como Configurar e Executar o Projeto

Siga os passos abaixo sequencialmente para preparar o ambiente e rodar a aplicação em sua máquina.

### 1. Pré-requisitos
Certifique-se de ter instalado em sua máquina:
* [Python 3.10+](https://www.python.org/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) ativo e rodando ou WSL.
* Uma chave de API do Google Gemini (Gere gratuitamente no [Google AI Studio](https://aistudio.google.com/))

### 2. Configurando o Ambiente Virtual (Venv)
Abra o terminal na raiz do projeto (`SETUP-TALK-INGESTAO-BUSCA`) e execute os comandos correspondentes ao seu sistema operacional para criar e ativar o ambiente isolado do Python:

* **Criar o ambiente virtual:**
    ```bash
    python -m venv .venv
    ```

* **Ativar o ambiente virtual:**
    * **Windows (Command Prompt):**
        ```cmd
        .venv\Scripts\activate.bat
        ```
    * **Windows (PowerShell):**
        ```powershell
        .venv\Scripts\Activate.ps1
        ```
    * **Linux / macOS:**
        ```bash
        source .venv/bin/activate
        ```

*(Você saberá que deu certo quando o prefixo `(.venv)` aparecer no início da linha do seu terminal).*

### 3. Instalando as Dependências
Com o ambiente virtual devidamente ativo, atualize o gerenciador de pacotes e instale as bibliotecas necessárias listadas no `requirements.txt`:
```bash
pip install --upgrade pip
pip install -r requirements.txt