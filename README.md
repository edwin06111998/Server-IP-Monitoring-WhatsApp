<h1 align="center"> Monitoreo de Servidores </h1> <br>
<p align="center">
  <a href="https://gitpoint.co/">
    <img alt="Chatbot" title="Chatbot" src="https://raw.githubusercontent.com/edwin06111998/monitoreo_servidores_alerta/main/images/Logo%20Monitereo.png" width="450">
  </a>
</p>

<p align="center">
  Envío de alerta en tiempo real sobre la conexión del servidor.
</p>

## Tabla de contenidos

- [Introducción](#introduction)
- [Funciones](#features)
- [Retroalimentación](#feedback)
- [Contributors](#contributors)
- [Build Process](#build-process)
- [Backers](#backers-)
- [Sponsors](#sponsors-)
- [Acknowledgments](#acknowledgments)

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
* Almacenar registro de eventos.
* Lectura dinámica de direcciones IPs de servidores/antenas.
* Agregar múltiples destinatarios simultáneos para recibir la alerta.
* Escalabilidad y posibilidad de implementarse en una interfaz web.

<p align="center">
  <img src = "https://raw.githubusercontent.com/edwin06111998/monitoreo_servidores_alerta/main/images/Alerta2.png" width=350>
</p>

<p align="center">
  <img src = "https://raw.githubusercontent.com/edwin06111998/monitoreo_servidores_alerta/main/images/Alerta.png" width=350>
</p>

## Feedback

Feel free to send us feedback on [Twitter](https://twitter.com/gitpointapp) or [file an issue](https://github.com/gitpoint/git-point/issues/new). Feature requests are always welcome. If you wish to contribute, please take a quick look at the [guidelines](./CONTRIBUTING.md)!

If there's anything you'd like to chat about, please feel free to join our [Gitter chat](https://gitter.im/git-point)!

## Contributors

This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification and is brought to you by these [awesome contributors](./CONTRIBUTORS.md).

## Build Process

- Follow the [React Native Guide](https://facebook.github.io/react-native/docs/getting-started.html) for getting started building a project with native code. **A Mac is required if you wish to develop for iOS.**
- Clone or download the repo
- `yarn` to install dependencies
- `yarn run link` to link react-native dependencies
- `yarn start:ios` to start the packager and run the app in the iOS simulator (`yarn start:ios:logger` will boot the application with [redux-logger](<https://github.com/evgenyrodionov/redux-logger>))
- `yarn start:android` to start the packager and run the app in the the Android device/emulator (`yarn start:android:logger` will boot the application with [redux-logger](https://github.com/evgenyrodionov/redux-logger))

Please take a look at the [contributing guidelines](./CONTRIBUTING.md) for a detailed process on how to build your application as well as troubleshooting information.

**Development Keys**: The `CLIENT_ID` and `CLIENT_SECRET` in `api/index.js` are for development purposes and do not represent the actual application keys. Feel free to use them or use a new set of keys by creating an [OAuth application](https://github.com/settings/applications/new) of your own. Set the "Authorization callback URL" to `gitpoint://welcome`.

## Backers [![Backers on Open Collective](https://opencollective.com/git-point/backers/badge.svg)](#backers)

Thank you to all our backers! 🙏 [[Become a backer](https://opencollective.com/git-point#backer)]

<a href="https://opencollective.com/git-point#backers" target="_blank"><img src="https://opencollective.com/git-point/backers.svg?width=890"></a>

## Sponsors [![Sponsors on Open Collective](https://opencollective.com/git-point/sponsors/badge.svg)](#sponsors)

Support this project by becoming a sponsor. Your logo will show up here with a link to your website. [[Become a sponsor](https://opencollective.com/git-point#sponsor)]

<a href="https://opencollective.com/git-point/sponsor/0/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/0/avatar.svg"></a>
<a href="https://opencollective.com/git-point/sponsor/1/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/1/avatar.svg"></a>
<a href="https://opencollective.com/git-point/sponsor/2/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/2/avatar.svg"></a>
<a href="https://opencollective.com/git-point/sponsor/3/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/3/avatar.svg"></a>
<a href="https://opencollective.com/git-point/sponsor/4/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/4/avatar.svg"></a>
<a href="https://opencollective.com/git-point/sponsor/5/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/5/avatar.svg"></a>
<a href="https://opencollective.com/git-point/sponsor/6/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/6/avatar.svg"></a>
<a href="https://opencollective.com/git-point/sponsor/7/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/7/avatar.svg"></a>
<a href="https://opencollective.com/git-point/sponsor/8/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/8/avatar.svg"></a>
<a href="https://opencollective.com/git-point/sponsor/9/website" target="_blank"><img src="https://opencollective.com/git-point/sponsor/9/avatar.svg"></a>

## Acknowledgments

Thanks to [JetBrains](https://www.jetbrains.com) for supporting us with a [free Open Source License](https://www.jetbrains.com/buy/opensource).
