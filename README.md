<p align="center">
  <a href="https://gitpoint.co/">
    <img alt="Chatbot" title="Chatbot" src="https://github.com/edwin06111998/Imagenes/blob/main/Proceso%20Chatbot/Header%20Monitoreo.jpg">
  </a>
</p>
<h1 align="center"> Monitoreo de Servidores </h1> <br>

<p align="center">
  Envío de alerta en tiempo real sobre la conexión del servidor.
</p>

## Tabla de contenidos

- [Introducción](#introduction)
- [Funciones](#features)
- [Retroalimentación](#feedback)
- [Contribuidores](#contributors)
- [Proceso de construcción](#build-process)
- [Contacto](#acknowledgments)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Introducción

Servicio de alerta de monitoreo de servidores y antenas de energía eléctrica UISP. El sistema está desarrollado en Python, se ejecuta en tiempo real sobre un servidor Linux, envía alertas sobre el estado de conexión del servidor, a través de WhatsApp.

**Dispinible para WhatsApp, Telegram o Messenger.**

<p align="center">
  <img src = "https://raw.githubusercontent.com/edwin06111998/monitoreo_servidores_alerta/main/images/Captura.png" width=700>
</p>

## Funciones

Estas son algunas de las características del sistema de monitoreo:

* Verificar el estado de conexión de servidores.
* Verificar el estado de conexión de antenas UISP.
* Notificar en tiempo real mediante WhatsApp sobre caída de servidor/antena.
* Notificar sobre restablecimiento de conexión de servidor/antena.
* Enviar alerta cada 15 minutos en caso de que el servidor/antena siga caído.
* Almacenar registro de eventos.
* Lectura dinámica de direcciones IPs de servidores/antenas.
* Agregar múltiples destinatarios simultáneos para recibir la alerta.
* Escalabilidad y posibilidad de implementarse en una interfaz web.
<h1></h1>
<p align="center">
  <img src = "https://raw.githubusercontent.com/edwin06111998/monitoreo_servidores_alerta/main/images/Alerta2.png" width=350>
</p>

<p align="center">
  <img src = "https://raw.githubusercontent.com/edwin06111998/monitoreo_servidores_alerta/main/images/Alerta.png" width=350>
</p>

## Retroalimentación

Siéntete libre de comentarme tu experiencia utilizando este sistema, puedes escribir al siguiente correo: edwin06111998@gmail.com. Tus comentarios son importantes para seguir haciendo robusto este sistema.

## Contribuidores

Este proyecto ha sido desarrollado únicamente por mí (Edwin Veloz).

## Proceso de construcción

- Clona o descarga el repositorio
- Crea una aplicación en Facebook para usar la API de WhatsApp
- Obtén un token permanente y el ID de la aplicación
- Crea las plantillas en Facebook para los mensajes de alerta
- Ingresa el token y ID en el archivo send_message.py
- Modifica el "filepath" ingresando la ruta del repositorio en los archivos ping.py y antennas.py
- Ingresa las IPs en el archivo ips.txt y los destinatarios en el archivo numbers.txt
- Ejecuta ping.py y antennas.py

Importante: para ejecutar el código 24/7, puedes implementarlo en un servidor Linux y usar comandos como "crontab -e" para ejecutar el código cada determinado tiempo.

## Contacto

- LinkedIn: www.linkedin.com/in/edwin-veloz-2153a9137
- Correo: edwin06111998@gmail.com
