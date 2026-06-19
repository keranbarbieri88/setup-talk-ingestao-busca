import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_postgres import PGVector
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Recebe a pergunta, precuras os chunks mais parecidos no banco, monta o prompt com as regra que defini.
PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""

def search_prompt():
    
    # configuração de conexão e embeddings (iguais ao ingest)
    embeddings = GoogleGenerativeAIEmbeddings(model=os.getenv("GOOGLE_EMBEDDING_MODEL"))
    connection = os.getenv("DATABASE_URL")
    collection = os.getenv("PG_VECTOR_COLLECTION_NAME")



    # inicialização o banco de vetores
    vectorstore = PGVector(
        embeddings=embeddings,
        connection=connection,
        collection_name=collection,
        use_jsonb=True,
    )

    # configura o modelo de Chat (LLM)
    llm = ChatGoogleGenerativeAI(model=os.getenv("GOOGLE_CHAT_MODEL"), temperature=0)
    
    def ask(question):
        
        # busca os 10 documentos mais relevantes (k=10)
        docs_with_score = vectorstore.similarity_search(question, k=10)

        # concatena o conteúdo dos documentos para o contexto
        contexto = "\n\n".join([doc.page_content for doc in docs_with_score])

        # preenche o template de prompt
        prompt = PROMPT_TEMPLATE.format(contexto=contexto, pergunta=question)

        # chama a LLM  e retorne a resposta
        response = llm.invoke(prompt)
        return response.content
    
    return ask # retorno a função pronta para ser usada