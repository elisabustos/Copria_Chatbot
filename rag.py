"""Orquestador RAG: pregunta -> retrieval -> augment -> generation -> respuesta."""
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from vectorstore import recuperar
from prompt import construir_system_prompt
from llm import llm


def responder(mensaje: str, historial: list) -> str:
    """Ejecuta el pipeline RAG completo para una pregunta."""
    # 1. Retrieval: fragmentos relevantes a la pregunta.
    fragmentos = recuperar(mensaje)

    # 2. Augment: prompt de sistema con el contexto recuperado.
    system_prompt = construir_system_prompt(fragmentos)

    # 3. Generation: se arma la conversación y responde el LLM.
    mensajes = [SystemMessage(content=system_prompt)]
    for turno in historial:
        if turno["role"] == "user":
            mensajes.append(HumanMessage(content=turno["content"]))
        elif turno["role"] == "assistant":
            mensajes.append(AIMessage(content=turno["content"]))
    mensajes.append(HumanMessage(content=mensaje))

    respuesta = llm.invoke(mensajes)
    return respuesta.content
