"""Aumentar: construye el prompt del sistema con los fragmentos recuperados"""

from langchain_core.documents import Document

SYSTEM_TEMPLATE = (
    "Eres un asistente que responde únicamente con base en la información proporcionada "
    "a continuación, extraída de documentos oficiales que te fueron precargados. \n Reglas:\n"
    "- Si la respuesta no está contenida en el contexto, indica claramente "
    "que no dispones de esa información.\n"
    " - No saludes, solo responde.\n"
    "- No inventes datos ni uses conocimiento externo.\n"
    "- Responde en español, de forma clara y natural, como si estuvieras conversando con el usuario y cita el documento y la página "
    "cuando sea útil.\n\n"
    "===== INFORMACION PROPORCIONADA: =====\n"
    "{contexto}"
)


def formatear_contexto(fragmentos: list[Document]) -> str:
    """Concatena los fragmentos recuperados con su cita de origen."""
    bloques = []
    for frag in fragmentos:
        fuente = frag.metadata.get("source", "desconocido")
        pagina = frag.metadata.get("page", "?")
        bloques.append(f"[{fuente}, página {pagina}]\n{frag.page_content}")
    return "\n\n---\n\n".join(bloques)


def construir_system_prompt(fragmentos: list[Document]) -> str:
    """Aumentar: inyecta el contexto recuperado en la plantilla de sistema"""
    return SYSTEM_TEMPLATE.format(contexto=formatear_contexto(fragmentos))
