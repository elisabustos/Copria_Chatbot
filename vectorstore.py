"""Vector store y retrieval: embeddings Google + índice en memoria.

El índice vive en la RAM del proceso (InMemoryVectorStore): no se sube a
Google ni persiste en disco. Lo que sí usa la API de Google es el cálculo de
los embeddings (texto -> vector), con la misma GEMINI_API_KEY.
"""
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config import EMBEDDING_MODEL, GEMINI_API_KEY, TOP_K
from loader import cargar_documentos
from splitter import trocear

embeddings = GoogleGenerativeAIEmbeddings(
    model=EMBEDDING_MODEL,
    google_api_key=GEMINI_API_KEY,
)


def construir_indice() -> InMemoryVectorStore:
    """Carga -> trocea -> embebe -> indexa. Devuelve el vector store."""
    documentos = cargar_documentos()
    fragmentos = trocear(documentos)
    print(f"Indexando {len(fragmentos)} fragmentos desde {len(documentos)} páginas...")
    store = InMemoryVectorStore.from_documents(fragmentos, embedding=embeddings)
    print("Índice construido en memoria.")
    return store


# Índice y retriever creados una sola vez al importar el módulo.
_store = construir_indice()
retriever = _store.as_retriever(search_kwargs={"k": TOP_K})


def recuperar(pregunta: str) -> list[Document]:
    """Retrieval: devuelve los fragmentos más relevantes a la pregunta."""
    return retriever.invoke(pregunta)
