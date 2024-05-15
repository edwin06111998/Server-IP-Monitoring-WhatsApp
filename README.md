![Monitoreo de Servidores](/images/cover.png)
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

![Monitoreo de Servidores](/images/Captura.png)

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

![Monitoreo de Servidores](/images/Alerta2.png)

![Monitoreo de Servidores](/images/Alerta.png)

## Retroalimentación

Siéntete libre de comentarme tu experiencia utilizando este sistema, puedes escribir al siguiente correo: edwin06111998@gmail.com. Tus comentarios son importantes para seguir haciendo robusto este sistema.

## Contribuidores

Este proyecto ha sido desarrollado únicamente por mí (Edwin Veloz).

## Proceso de construcción

- Clona el repositorio
- Crea una aplicación en Facebook para usar la API de WhatsApp Business
- Obtén un token permanente y el ID de la aplicación
- Crea las 3 plantillas en Facebook para los mensajes de alerta
- Ingresa las variables de entorno descritas en el archivo .env
- Ingresa las IPs en el archivo ips.txt y los destinatarios en el archivo numbers.txt
- Ejecuta ping.py

## Contacto

- LinkedIn: www.linkedin.com/in/edwin-veloz-2153a9137
- Correo: edwin06111998@gmail.com
