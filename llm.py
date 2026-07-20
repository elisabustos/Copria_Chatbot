"""Generacion: instancia del modelo de chat de Gemini"""

from langchain_google_genai import ChatGoogleGenerativeAI 

from config import CHAT_MODEL, GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(
    model=CHAT_MODEL,
    google_api_key=GEMINI_API_KEY,
    temperature=0,
)