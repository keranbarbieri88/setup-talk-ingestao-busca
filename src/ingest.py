import os
import time
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from langchain_postgres import PGVector


load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")

def ingest_pdf():
     # carrega o PDF definido no .env.
    docs = PyPDFLoader(os.getenv("PDF_PATH")).load()

    if not docs:
        print("Erro: PDF_PATH não encontrado no .env")
        return

    # divide o texto em chunks de 1000 caracteres com overlap de 150.
    # o overlap serve para não perder contexto entre um pedaço e outro.
    splits = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        add_start_index=False
    ).split_documents(docs)

    if not splits:
        raise SystemExit(0)
    
    add_ids = [
        Document(
            page_content=d.page_content, 
            metadata={k: v for k, v in d.metadata.items() if v not in ("", None)}
        )
        for d in splits
    ]

    all_ids = [f"doc-{i}" for i in range(len(add_ids))]

    # configura o modelo de embeddings do Google
    embeddings = GoogleGenerativeAIEmbeddings(model=os.getenv("GOOGLE_EMBEDDING_MODEL"))
    
    # conecta ao PostreSQL 
    connection = os.getenv("DATABASE_URL")
    collection = os.getenv("PG_VECTOR_COLLECTION_NAME")

    #configuração de lotes, pois estou usando o Gemini gratuito
    batch_size = 5  # envio 5 chunks por vez para ficar bem seguro na cota
    wait_time = 20  # espero 20 segundos entre cada lote

    print(f"Iniciando ingestão de {len(add_ids)} pedaços em lotes de {batch_size}...")

    # inicialização o banco de vetores

    #loop para processar os lotes
    for i in range(0, len(add_ids), batch_size):
        batch = add_ids[i:i+batch_size]
        batch_ids = all_ids[i:i+batch_size]

        print(f"Enviando lote {i//batch_size + 1}...")
 
        db = PGVector.from_documents(
            embedding=embeddings,
            documents=batch,
            collection_name=collection,
            connection=connection,
            use_jsonb=True,
            # se for o primeiro lote, cria a tabela
            # nos próximos, apenas adiciona
            )

        db.add_documents(batch, ids=batch_ids)

        if i + batch_size < len(splits):
            print(f"Aguardando {wait_time}s para respeitar a cota...")
            time.sleep(wait_time)


    print("Ingestão concluída com sucesso!")

if __name__ == "__main__":
    ingest_pdf()