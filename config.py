"""Configuración central: carga de variables de entorno y constantes"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Credenciales
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Rutas
BASE_DIR = Path(__file__).parent
FILES_DIR = BASE_DIR / "files"

# Modelos (mismo proveedor Google, misma GEMINI_API_KEY)
CHAT_MODEL = "gemini-2.5-flash"
EMBEDDING_MODEL = "models/gemini-embedding-001"

# Parámetros de troceo (chunking)
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

# Cantidad de fragmentos a recuperar por consulta
TOP_K = 4
