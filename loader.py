"""Carga de documentos: lee los PDF de la carpeta files/ como Document."""
from pathlib import Path

from langchain_core.documents import Document
from pypdf import PdfReader

from config import FILES_DIR


def cargar_documentos(directorio: Path = FILES_DIR) -> list[Document]:
    """Lee todos los PDF de la carpeta y devuelve un Document por página.

    Cada Document conserva metadata útil para citar la fuente:
    - source: nombre del archivo
    - page: número de página (1-indexado)
    """
    documentos: list[Document] = []
    for pdf in sorted(directorio.glob("*.pdf")):
        try:
            lector = PdfReader(str(pdf))
            for i, pagina in enumerate(lector.pages, start=1):
                texto = pagina.extract_text() or ""
                if not texto.strip():
                    continue
                documentos.append(
                    Document(
                        page_content=texto,
                        metadata={"source": pdf.name, "page": i},
                    )
                )
        except Exception as e:
            print(f"Error leyendo {pdf.name}: {e}")
    return documentos
