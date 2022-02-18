# Chatbot Aerito

## Descripción

Aerito es un chatbot creado para la atención automatizada por la pagina web a las consultas frecuentes de los alumnos de la Facultad de Ciencias sobre los temas de matricula, procedimientos y tramites académicos.

## Descripción general de los archivos

Los siguientes archivos son propios del framework RASA

`data/nlu.yml` - contiene los ejemplos de consultas que son proveídas como datos y son clasificación en una intención que determinara la siguiente acción o respuesta del chatbot.

`data/stories.yml` - contiene los flujos de ejemplos en los que el chatbot sera entrenado.

`domain.yml` - contiene las respuestas del chatbot

`config.yml` - configuración del pipeline de procesamiento natural para procesar las entradas del usuario

La arquitectura del proyecto se ha generado con el Framework de código abierto RASA, puede encontrar mas información sobre la descripción de estos archivos en la [documentación oficial](https://rasa.com/docs/rasa/training-data-format).

`webchat/` - contiene el widget del chat que puedo ser integrado al pagina web para la interaction con el bot.

`despligue/` - contiene archivos para el despliegue por docker en un servidor.

## Instalación Local

Para instalar, clone el repositorio o descomprima el archivo zip, luego ejecute los siguiente comando para instalar las dependencias

```
pip3 install requiriments.txt
pip3 install rasa[spacy] rasa[transformers]
python -m spacy download es_core_news_md
```

Esto instalará el bot y todos sus requisitos. Tenga en cuenta que este bot debe usarse con Python 3.6 o 3.7.

# Como ejecutar Aerito

Si desea volver a entrenar el modelo luego de hacer cambios o agregar mas datos corra el comando `rasa train` para entrenar el modelo

Luego para compilar y ejecutar el modelo chatbot primero ejecute el siguiente comando:

```
rasa run --cors "*"

rasa run actions
```

Luego, corra los siguientes comando para iniciar el chat web de la aplicación.

```
cd webchat
python3 -m http.server
```
