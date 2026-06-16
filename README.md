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
  Caso já tenha instalado, verificar se a versão igual 3.10 ou superior:
  ```powershell
    python --version
    ``` 
  A versão do gerenciador python-dotenv deve ser 1.1.1 conforme `requirements.txt`:
  ```powershell
    pip show python-dotenv
    ```
  Para instalar:
  1. Acesse a página oficial de [Downloads do Python para Windows](https://www.python.org/downloads/windows/).
  2. Clique no botão amarelo "Download Python" (ele detectará automaticamente a versão de 64 bits do seu Windows 11).
  3. Abra o arquivo baixado (ex: python-3.x.x.exe) na sua pasta de downloads.
  4. Passo mais importante: Na parte inferior da primeira tela, marque a caixinha "Add Python.exe to PATH" (Adicionar o Python ao PATH). Isso permite que você rode comandos Python de qualquer pasta no terminal.Clique em "Install Now" e aguarde a conclusão

* [Docker WSL](https://docs.docker.com/desktop/features/wsl/) 
  Caso já tenha instalado, verificar através do comando:
  ```powershell
    wsl --version
    ``` 
  Para instalar:
   ```powershell
    wsl --install
    ``` 
  Isso ativará os recursos necessários, baixará o kernel do Linux e instalará a distribuição padrão (Ubuntu).
  
  
* [API do Google Gemini](https://aistudio.google.com/) Gere gratuitamente no `Google AI Studio`.

### 2. Configurando o Ambiente Virtual (Venv)
Abra o terminal na raiz do projeto (`SETUP-TALK-INGESTAO-BUSCA`) e execute os comandos correspondentes ao seu sistema operacional para criar e ativar o ambiente isolado do Python:

* **Criar o ambiente virtual:**
    ```powershell
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