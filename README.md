# **Copria_Chatbot**
Chatbot enfocado en apoyar a comités de administración a que resuelvan sus dudas referentes a la ley 21.442 de copropiedad inmobiliaria en Chile

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

### **1. Crear el entorno virtual**

```bash
python3 -m venv nombreEntorno
```

### **2. Activar el entorno virtual**

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

### **3. Instalar las dependencias**

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