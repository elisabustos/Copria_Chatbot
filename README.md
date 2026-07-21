# **Copria_Chatbot**
Chatbot enfocado en apoyar a comités de administración a que resuelvan sus dudas referentes a la ley 21.442 de copropiedad inmobiliaria en Chile.

## **Infraestructura**

- **Máquina Virtual** — OCI Compute.
- **Red** — Firewall, Vnic, Subred, reserva de IP configurado sobre OCI.


## **Arquitectura (módulos)**

Cada etapa del trabajo está en su propio archivo:

| Archivo | Responsabilidad | Etapa RAG |
|---|---|---|
| `config.py` | Variables de entorno y constantes (rutas, modelos, chunking, `k`) | — |
| `loader.py` | Lee los PDF de `files/` → `Document`s con metadata (`source`, `page`) | — |
| `splitter.py` | Trocea los documentos (`RecursiveCharacterTextSplitter`) | — |
| `vectorstore.py` | Embeddings Google + `InMemoryVectorStore` + `retriever` | **Retrieval** |
| `prompt.py` | Plantilla de sistema + arma el contexto con los fragmentos | **Augment** |
| `llm.py` | Instancia `ChatGoogleGenerativeAI` (Gemini) | **Generation** |
| `rag.py` | Orquesta el pipeline completo (`responder()`) | Pipeline |
| `app.py` | Interfaz Gradio; llama a `rag.responder()` | UI |


## **Tecnologías Utilizadas **

- **LangChain** — orquestación del pipeline RAG.
- **Google Gemini** (`langchain-google-genai`) — chat y embeddings.
- **pypdf** — extracción de texto de los PDF.
- **Gradio** — interfaz web de chat.
- **InMemoryVectorStore** (LangChain) — índice vectorial en memoria.
- **Nginx** — servidor web configurado en máquina virtual.


## **Requisitos**

Antes de comenzar, asegúrate de contar con lo siguiente:

- Python 3.14 (incluido en `requirements.txt`).
- Una `GEMINI_API_KEY` obtenida desde Google AI Studio.

## **Configuración**

1. Crea un archivo llamado `.env` en la raíz del proyecto.
2. Agrega tu clave de API con el siguiente formato:

```env
GEMINI_API_KEY=tu_clave_aqui
```

3. Copia todos los archivos PDF que deseas consultar dentro de la carpeta `files/`.

## **Instalación**

Una vez descargado el proyecto, realiza los siguientes pasos:

**1. Crear el entorno virtual**

```bash
python3 -m venv nombreEntorno
```

**2. Activar el entorno virtual**

En Linux o macOS:

```bash
source nombreEntorno/bin/activate
```

En Windows (PowerShell):

```powershell
nombreEntorno\Scripts\Activate.ps1
```

En Windows (CMD):

```cmd
nombreEntorno\Scripts\activate.bat
```

**3. Instalar las dependencias**

```bash
pip3 install -r requirements.txt
```

## **Ejecutar el proyecto**

Una vez completada la instalación, inicia la aplicación con:

```bash
python3 app.py
```

Al ejecutar el comando, la aplicación mostrará una URL de **localhost** similar a la siguiente:

```text
http://127.0.0.1:7860
```

Abre esa dirección en tu navegador para comenzar a utilizar el proyecto.


## **Demo Proyecto**
Para acceder a la demo copia el siguiente link:
http://146.181.44.130/


## **Ejemplos**

**-1:**
**Usuario**: a los cuántos meses de acumulación de deuda del gasto común se puede cortar algún servicio básico?

**Chatbot**: Se puede solicitar la suspensión de servicios como la electricidad o las telecomunicaciones cuando los propietarios se encuentren morosos en el pago de tres o más cuotas, continuas o discontinuas, de los gastos comunes.

Para que esto ocurra, el administrador debe solicitarlo por escrito y contar con la autorización previa del comité de administración. Es importante destacar que no se puede solicitar la suspensión de más de un servicio a la vez.

Además, existen excepciones importantes:

No se puede suspender ningún servicio por deudas generadas durante un estado de catástrofe que afecte al condominio.
En el caso de que en la unidad resida una persona electrodependiente, no se podrá suspender el servicio eléctrico bajo ninguna circunstancia por mora en los gastos comunes.
Esta información se encuentra en la Ley 21.442, página 37.

**-2:**
**Usuario**: cuántos deben ser los miembros del comité?

**Chatbot**: El comité de administración debe estar compuesto por un número impar de miembros, con un mínimo de tres y un máximo de cinco.

Existen algunas excepciones a esta regla:

No es necesario designar un comité si el número de copropietarios es inferior a tres (Ley-21442.pdf, página 26).
En condominios divididos en sectores, el comité debe estar conformado por, al menos, un representante de cada sector (Ley-21442.pdf, página 31).
