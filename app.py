"""Interfaz gráfica (Gradio) del asistente RAG sobre la Ley 21.442."""
import gradio as gr

from rag import responder

chatbot = gr.ChatInterface(
    fn=responder,
    title="Asistente Ley 21.442 de copropiedad inmobiliaria",
    description="",
)

if __name__ == "__main__":
    chatbot.launch(footer_links=[])
