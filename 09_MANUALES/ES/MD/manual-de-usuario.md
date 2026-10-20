<!-- running-head: MANUAL DE USUARIO: SISTEMA DE LAVADO VEHICULAR -->

# Manual de Usuario

Sistema de Gestión de Lavado Vehicular (Vehicle Washing)

Plataforma Web para Reservar Lavados, Pagar con Código QR, Acumular Puntos y Gestionar el Trabajo Diario del Operario

Brayan Estiven Patiño Cabrera (líder de proyecto), Juan Camilo Guilombo Osorio (líder de frontend) y Merari Urbano (líder de backend)

Tecnólogo en Análisis y Desarrollo de Software (ADSO), Servicio Nacional de Aprendizaje (SENA), Centro de Formación: Industria

Ficha 3145556

Instructora: Karol Daniela Correa

17 de octubre de 2026

Tipo de manual: Manual de usuario (roles Cliente y Operario) · Versión 4.1

## Control de Versiones

La Tabla 1 registra el historial de cambios de este documento. Cada vez que el equipo de desarrollo modifique el manual, se debe agregar una fila con la versión, la fecha, la descripción del cambio y el responsable.

**Tabla 1**

*Historial de Versiones del Manual de Usuario*

| Versión | Fecha | Descripción del cambio | Responsable |
|---|---|---|---|
| 1.0 | 2026-10-03 | Creación inicial del manual de usuario (en español) para los roles Cliente y Operario. | Equipo de desarrollo |
| 2.0 | 2026-10-05 | Datos de portada completados (ficha, instructora y centro de formación) y nombre del sistema ajustado a Vehicle Washing. | Equipo de desarrollo |
| 3.0 | 2026-10-07 | Traducción al inglés, formato según las normas APA (7.ª ed.), reestructuración según la guía del SENA y verificación contra el código fuente de la aplicación web. Se corrigieron: rutas de las pantallas, campos del registro (número de documento, nombres, apellidos y aceptación de los documentos legales), reglas de la contraseña, ausencia de bloqueo de cuenta, flujo de reserva (sin elección de operario ni reprogramación desde la web), flujo de pago (reglas de la referencia), filtros del historial, notificaciones por correo y estados del operario. | Equipo de desarrollo |
| 3.1 | 2026-10-09 | Actualización contra el código del 9 de octubre de 2026 y creación de esta versión en español (la versión en inglés es Manual_usuario_LavadoVehicular_3145556_EN.md). Se agregaron: puntos de fidelización por servicio y en el resumen de la reserva, progreso de fidelidad y cupones desbloqueados en el panel, canje de cupones al pagar, lista de datos faltantes bajo el botón de confirmar, estado del pago en el historial y botón Pagar ahora solo cuando la reserva se puede pagar, avisos por correo de pagos aprobados, rechazados y reembolsados, de puntos ganados, de cupones desbloqueados y de informes de inspección, interruptores de notificaciones guardados en la cuenta, avisos al operario y nuevos mensajes. Se retiró WhatsApp del centro de ayuda. | Equipo de desarrollo |
| 4.0 | 2026-10-16 | Revisión contra el código del 16 de octubre de 2026. Las figuras pasaron de marcadores a capturas reales del sistema funcionando con datos de prueba. Se agregaron: elección opcional del operario al reservar y asignación automática de uno libre, bloqueo de la cuenta por 15 minutos después de cinco intentos fallidos, mensajes que explican por qué una hora no se puede reservar, inicio del servicio desde 15 minutos antes de la hora reservada, descarga de la aplicación Android desde la web, dirección del perfil guardada en la cuenta y la opción Desactivar mi cuenta, que antes se llamaba Eliminar cuenta. Se retiró el botón Reportar progreso, que ya no existe en la pantalla del operario. | Equipo de desarrollo |
| 4.1 | 2026-10-17 | Revisión contra el código del 17 de octubre de 2026. Se actualizó la pantalla de bienvenida (sección "Quiénes somos" sin cifras, nueva sección de preguntas frecuentes, pie de página sin redes sociales ni enlaces de contacto) y se describió cómo se adapta a celulares y tabletas. Se aclaró que el avance del próximo servicio queda en 0 % hasta que empieza el lavado y que el saludo del panel nombra al lavadero como Lavado Vehicular. | Equipo de desarrollo |
| 4.2 | 2026-10-19 | Las cuentas de administrador no tienen la opción Desactivar mi cuenta (preguntas frecuentes). | Equipo de desarrollo |
| 4.3 | 2026-10-19 | Capturas tomadas de nuevo el 19 de octubre de 2026 (fecha en los paneles, calendarios sin días pasados y resumen de la reserva). | Equipo de desarrollo |
| 4.4 | 2026-10-20 | El historial del cliente y el del operario van de la reserva más reciente a la más antigua y abren el detalle al hacer clic, con los botones **Ir al pago** e **Ir a calificaciones**. Las notificaciones abren su detalle al hacer clic, con un botón para ir al apartado de donde viene el aviso. Con el pago aprobado, la pantalla de pago solo muestra el resumen. | Equipo de desarrollo |

*Nota.* Las fechas se escriben en formato ISO 8601 (año-mes-día). Elaborado por el equipo de desarrollo.

## Tabla de Contenido

<!-- toc -->

- [Control de Versiones](#control-de-versiones)
- [4. Introducción](#4-introducción)
  - [4.1 Fuentes y Convenciones de Este Manual](#41-fuentes-y-convenciones-de-este-manual)
- [5. Objetivo](#5-objetivo)
  - [5.1 Objetivo General](#51-objetivo-general)
  - [5.2 Objetivos Específicos](#52-objetivos-específicos)
- [6. Alcance](#6-alcance)
  - [6.1 Qué Cubre Este Manual](#61-qué-cubre-este-manual)
  - [6.2 Qué No Cubre Este Manual](#62-qué-no-cubre-este-manual)
  - [6.3 Sobre las Capturas de Pantalla](#63-sobre-las-capturas-de-pantalla)
- [7. Requisitos para Usar el Sistema](#7-requisitos-para-usar-el-sistema)
  - [7.1 Requisitos del Dispositivo y del Navegador](#71-requisitos-del-dispositivo-y-del-navegador)
  - [7.2 Roles del Sistema](#72-roles-del-sistema)
  - [7.3 Presentación del Sistema](#73-presentación-del-sistema)
- [8. Ingreso al Sistema](#8-ingreso-al-sistema)
  - [8.1 Registro de un Cliente Nuevo](#81-registro-de-un-cliente-nuevo)
  - [8.2 Inicio de Sesión](#82-inicio-de-sesión)
  - [8.3 Recuperación de la Contraseña](#83-recuperación-de-la-contraseña)
- [9. Menú Principal](#9-menú-principal)
  - [9.1 Menú del Cliente](#91-menú-del-cliente)
  - [9.2 Menú del Operario](#92-menú-del-operario)
- [10. Módulos del Sistema](#10-módulos-del-sistema)
  - [10.1 Módulos del Rol Cliente](#101-módulos-del-rol-cliente)
  - [10.2 Módulos del Rol Operario](#102-módulos-del-rol-operario)
- [11. Mensajes y Validaciones](#11-mensajes-y-validaciones)
- [12. Cierre de Sesión](#12-cierre-de-sesión)
- [13. Preguntas Frecuentes](#13-preguntas-frecuentes)
- [14. Glosario](#14-glosario)
- [Referencias](#referencias)
- [15. Anexos](#15-anexos)
  - [Anexo A. Origen de las Capturas](#anexo-a-origen-de-las-capturas)
  - [Anexo B. Lista de Verificación para la Entrega](#anexo-b-lista-de-verificación-para-la-entrega)

<!-- /toc -->

## 4. Introducción

El Sistema de Gestión de Lavado Vehicular (Vehicle Washing) es una plataforma web que permite a los clientes de un lavadero reservar un turno desde el teléfono o el computador, y que organiza en un solo lugar el trabajo de los operarios, la verificación de los pagos y el seguimiento de cada servicio.

Antes del sistema, los clientes tenían que llamar o desplazarse al local sin saber si había un turno libre. Dentro del negocio, las reservas se anotaban a mano, los turnos podían superponerse, el trabajo se repartía a criterio del encargado y los pagos en efectivo no dejaban registro del cliente. El sistema reemplaza ese procedimiento por un flujo digital: el cliente consulta la disponibilidad real del lavadero, reserva en pocos minutos, paga escaneando el código QR del negocio, acumula puntos que desbloquean cupones de descuento y conserva el historial y la calificación de cada servicio.

Este manual explica, en lenguaje sencillo y paso a paso, cómo trabajan con el sistema las dos personas que lo usan todos los días: el **cliente**, que es el dueño del vehículo, y el **operario**, que es el empleado que realiza el lavado. No se necesitan conocimientos de programación, de bases de datos ni de configuración técnica para seguir las instrucciones.

El documento sigue la estructura de la guía para elaborar manuales de software del programa Tecnólogo en Análisis y Desarrollo de Software (Servicio Nacional de Aprendizaje [SENA], 2026) y aplica las normas APA, séptima edición, en títulos, tablas, figuras, citas y referencias. Su contenido se verificó contra el código fuente de la aplicación web (Equipo de Desarrollo Vehicle Washing, 2026b) y la documentación del proyecto (Equipo de Desarrollo Vehicle Washing, 2026a). En cuanto a los datos personales de los usuarios, el sistema se rige por la Ley Estatutaria 1581 de 2012, que regula el tratamiento de datos personales en Colombia (Congreso de la República de Colombia, 2012).

### 4.1 Fuentes y Convenciones de Este Manual

Las pantallas, rutas, botones y mensajes descritos corresponden a la rama *develop* de la aplicación web al 17 de octubre de 2026. En la interfaz el sistema aparece con su nombre comercial, **LavaRápido**. Los nombres de botones, menús y mensajes se escriben en **negrita** o entre comillas tal como aparecen cuando el idioma de la interfaz es el español; la interfaz también está disponible en inglés, francés y portugués. Una ruta como */client/vehicles* es la parte de la dirección web que sigue al dominio del sistema (por ejemplo, *http://localhost:4200/client/vehicles* en el entorno local).

## 5. Objetivo

### 5.1 Objetivo General

Explicar paso a paso cómo el cliente y el operario deben ingresar, navegar y usar las funciones principales del Sistema de Gestión de Lavado Vehicular, de modo que cualquier persona pueda usar el software sin ayuda del equipo de desarrollo.

### 5.2 Objetivos Específicos

- Guiar al cliente en el registro de la cuenta, el inicio de sesión y la recuperación de la contraseña.
- Describir cómo el cliente registra vehículos, reserva un lavado, cancela una reserva, paga el servicio, canjea cupones y califica la atención recibida.
- Describir cómo el operario consulta la agenda, revisa los servicios asignados, inicia y finaliza cada servicio y consulta las calificaciones recibidas.
- Explicar el significado de los mensajes y validaciones del sistema y la acción que debe tomar la persona en cada caso.
- Responder las preguntas más frecuentes de las personas que usan la plataforma.

## 6. Alcance

### 6.1 Qué Cubre Este Manual

- La aplicación web del sistema, usada desde un navegador en un computador, una tableta o un teléfono.
- El rol **Cliente**: registro, inicio de sesión, recuperación de la contraseña, panel, vehículos, reservas, pagos, puntos de fidelización y cupones, historial, calificaciones, notificaciones, perfil y configuración.
- El rol **Operario**: panel, agenda, servicios asignados, inicio y finalización de servicios, notificaciones, historial, calificaciones recibidas, perfil y configuración.
- Las preferencias de apariencia (cuatro temas de color) e idioma (español, inglés, francés y portugués).

### 6.2 Qué No Cubre Este Manual

- Las funciones del rol **Administrador** (reservas, asignación de operarios, revisión de pagos, horarios y bahías, usuarios, servicios, promociones, reportes y configuración), que se explican en el Manual de Administrador.
- La instalación, la configuración y la construcción interna del software, que se explican en el Manual de Instalación y en el Manual Técnico.
- La aplicación móvil Android (React Native con Expo), que ofrece módulos equivalentes para los tres roles. Se descarga desde la página de inicio de la web con el botón de descarga o el código QR; este manual documenta solo la versión web.
- El lavado a domicilio: en la versión actual el cliente lleva el vehículo al lavadero en la fecha y la hora reservadas.
- La facturación electrónica ante la DIAN, las pasarelas de pago y la gestión de insumos o inventario.

### 6.3 Sobre las Capturas de Pantalla

Las figuras de este manual son capturas reales del sistema funcionando en el entorno local, tomadas el 16 de octubre de 2026 con cuentas y datos de prueba. Están ordenadas según el flujo de uso y su origen se explica en el Anexo A.

## 7. Requisitos para Usar el Sistema

### 7.1 Requisitos del Dispositivo y del Navegador

El sistema funciona en las versiones actuales de Google Chrome, Mozilla Firefox y Microsoft Edge, y su interfaz se adapta a la pantalla de un teléfono, una tableta o un computador. La Tabla 2 lista los requisitos.

**Tabla 2**

*Requisitos Mínimos para Usar el Sistema*

| Recurso | Requisito |
|---|---|
| Dispositivo | Computador, tableta o teléfono inteligente. |
| Navegador | Google Chrome, Mozilla Firefox o Microsoft Edge, en una versión actualizada. |
| Conexión | Acceso estable a internet durante todo el uso del sistema. |
| Correo | Una cuenta de correo terminada en @gmail.com. El sistema solo acepta este tipo de correo. |
| Documento de identidad | Un número de documento colombiano de 5 a 20 dígitos. |
| Teléfono | Un número celular colombiano de 10 dígitos que empiece por 3. |
| Cuenta | Un usuario registrado y activo. Los operarios reciben su cuenta del administrador del negocio. |
| Pago digital (clientes) | Nequi, Daviplata o una aplicación bancaria para escanear el código QR y hacer la transferencia. |

*Nota.* Elaborado por los autores a partir de las validaciones del formulario de registro y de los requisitos no funcionales del sistema.

### 7.2 Roles del Sistema

El sistema reconoce tres roles fijos. Cada persona ve solo las opciones de su rol y no puede abrir las pantallas de otro: si lo intenta, el sistema la devuelve a la pantalla de inicio de su rol (Tabla 3).

**Tabla 3**

*Roles del Sistema y Descripción General*

| Rol | Quién es | Qué hace en el sistema | Ruta de inicio |
|---|---|---|---|
| Cliente | Dueño del vehículo. | Registra vehículos, reserva turnos, paga, acumula puntos, canjea cupones, califica el servicio y consulta el historial. | /client |
| Operario | Empleado que realiza el lavado. | Consulta la agenda y los servicios asignados, inicia y finaliza cada servicio y consulta las calificaciones. | /operator |
| Administrador | Dueño o encargado del lavadero. | Gestiona reservas, operarios, pagos, horarios, usuarios, promociones y reportes. Se documenta en el Manual de Administrador. | /admin |

*Nota.* Elaborado por los autores a partir de la configuración de rutas de la aplicación web.

### 7.3 Presentación del Sistema

**Pantalla de bienvenida.** Al abrir la dirección web del sistema aparece la pantalla de bienvenida. En la parte superior hay una barra de navegación con los enlaces **Inicio**, **Nosotros** y **Servicios**, un selector de idioma y los botones **Iniciar Sesión** y **Registrarse**. El bloque central muestra los botones **Comenzar ahora** y **Ya tengo cuenta**; más abajo aparecen, en este orden, la sección "Quiénes somos", "¿Por qué elegirnos?", los servicios de lavado con su descripción y duración, la descarga de la aplicación móvil, los datos de contacto del lavadero y la sección **Preguntas frecuentes**, que responde en un acordeón (una pregunta abierta a la vez) cómo reservar, los métodos de pago, la cancelación, la elección del operario, los puntos, los recordatorios y la aplicación para celular. El pie de página tiene los enlaces **Sobre nosotros**, los tres servicios, **Centro de ayuda**, **Preguntas frecuentes** (que lleva a esa sección), **Términos de servicio** y **Política de privacidad**.

**Uso en celulares y tabletas.** Todas las pantallas se adaptan al ancho del dispositivo desde 360 píxeles, sin desplazamiento lateral. En el celular, la barra superior muestra solo el selector de idioma e **Iniciar sesión** (el registro sigue disponible con **Comenzar ahora**), los botones de la portada ocupan todo el ancho y, con la sesión iniciada, el menú lateral se abre con el botón ☰ de la esquina superior izquierda.

**Figura 1**

*Pantalla de Bienvenida del Sistema*

![Pantalla de Bienvenida del Sistema](capturas/usuario-01-pantalla-de-bienvenida-del-sistema.jpg)

*Nota.* Captura en un navegador de escritorio con la ventana completa.

**Tipos de servicio de lavado.** El lavadero ofrece tres niveles de limpieza. Cada servicio tiene su propia duración, su precio y los puntos de fidelización que suma, y **el precio depende del tipo de vehículo**; por eso el valor final se muestra en el resumen de la reserva una vez la persona elige el vehículo y el servicio (Tabla 4).

**Tabla 4**

*Niveles de Servicio de Lavado*

| Servicio | Qué incluye | Duración estimada |
|---|---|---|
| Básico | Lavado exterior completo, aspirado básico y limpieza de vidrios. | 45 minutos |
| Premium | Todo lo del Básico, más lavado de motor y cera líquida protectora. | 75 minutos |
| Completo | Todo lo del Premium, más encerado a mano y detallado interior. | 120 minutos |

*Nota.* Las duraciones corresponden a los datos iniciales del sistema. El administrador configura los precios, las duraciones y los puntos de cada tipo de vehículo, y pueden cambiar.

**Idiomas y temas.** Toda la interfaz está disponible en español, inglés, francés y portugués, y en cuatro temas de color (verde claro, verde oscuro, rosado y rosado oscuro). El idioma se puede cambiar desde la pantalla de bienvenida o, con la sesión iniciada, desde **Configuración** (sección 10.1.9).

## 8. Ingreso al Sistema

Toda persona debe tener una cuenta para usar las funciones del sistema. Los clientes crean su propia cuenta mediante el registro; los operarios reciben su cuenta del administrador del negocio, con una contraseña temporal que deben cambiar después del primer ingreso.

### 8.1 Registro de un Cliente Nuevo

**Nombre del módulo:** Registro de clientes.

**Descripción:** Permite a una persona nueva crear una cuenta de cliente para reservar servicios de lavado.

**Rol que puede usarlo:** Persona sin cuenta (futuro cliente).

**Ruta o menú donde se encuentra:** Pantalla de bienvenida > botón **Registrarse** (ruta */auth/register*).

**Pasos para utilizarlo:**

1. Abrir el navegador e ingresar la dirección web del sistema.
2. Hacer clic en **Registrarse** en la barra superior (o en **Comenzar ahora**).
3. Escribir el **Número de Documento**: solo dígitos, entre 5 y 20.
4. Escribir los **Nombres** (mínimo 3 caracteres) y los **Apellidos** (mínimo 2 caracteres).
5. Escribir el **Correo Electrónico**, que debe terminar en @gmail.com. El campo no admite espacios.
6. Escribir el **Teléfono**: un número celular colombiano de 10 dígitos que empiece por 3. El campo solo acepta dígitos.
7. Escribir la **Contraseña** y observar la lista de requisitos, que se marcan a medida que se cumplen: mínimo 8 caracteres, al menos una letra mayúscula, al menos un número y al menos un carácter especial. **Los cuatro requisitos son obligatorios**; no se admiten espacios.
8. Repetir la contraseña en **Confirmar Contraseña**. El ícono del ojo muestra u oculta lo escrito.
9. Abrir los **Términos y Condiciones** y la **Política de Tratamiento de Datos Personales** con sus enlaces y aceptar ambos. Al hacer clic en **Aceptar y continuar** dentro de cada documento, la casilla correspondiente se marca automáticamente.
10. Hacer clic en **Registrarse**. Mientras se procesa la solicitud, el botón muestra "Registrando...".

**Resultado esperado:** El sistema muestra el mensaje "¡Registro exitoso!" y, al hacer clic en **Ir a iniciar sesión**, lleva a la persona a la pantalla de inicio de sesión. Si el lavadero tiene activado el correo, llega un mensaje de bienvenida.

**Observaciones o restricciones:** No es posible registrar dos cuentas con el mismo correo ni con el mismo número de documento. En esos casos, el sistema muestra "Ya existe una cuenta con este correo" o "Ya existe una cuenta con este número de documento" y no crea la cuenta.

**Figura 2**

*Formulario de Registro de Clientes*

![Formulario de Registro de Clientes](capturas/usuario-02-formulario-de-registro-de-clientes.jpg)

*Nota.* En la captura no debe aparecer información personal real.

**Figura 3**

*Mensajes de Validación en el Registro*

![Mensajes de Validación en el Registro](capturas/usuario-03-mensajes-de-validacion-en-el-registro.jpg)

*Nota.* Apoya la Tabla 11 de la sección 11.

### 8.2 Inicio de Sesión

**Nombre del módulo:** Inicio de sesión.

**Descripción:** Permite al cliente, al operario o al administrador entrar al sistema con sus credenciales.

**Rol que puede usarlo:** Cliente, Operario y Administrador.

**Ruta o menú donde se encuentra:** Pantalla de bienvenida > botón **Iniciar Sesión** (ruta */auth*).

**Pasos para utilizarlo:**

1. Abrir el navegador e ingresar la dirección web del sistema.
2. Hacer clic en **Iniciar Sesión**.
3. Escribir el **Correo Electrónico** registrado (terminado en @gmail.com).
4. Escribir la **Contraseña**.
5. Hacer clic en **Iniciar Sesión**. Mientras se procesa la solicitud, el botón muestra "Ingresando...".

**Resultado esperado:** El sistema abre la pantalla de inicio del rol de la persona: */client* para el cliente, */operator* para el operario o */admin* para el administrador. El tema y el idioma guardados en la cuenta se aplican automáticamente.

**Observaciones o restricciones:** Si el correo o la contraseña son incorrectos, el sistema muestra "Correo o contraseña incorrectos" y no revela cuál de los dos falló. Después de cinco intentos fallidos en menos de 15 minutos, la cuenta queda bloqueada durante 15 minutos y el sistema muestra "Demasiados intentos fallidos. Tu cuenta quedó bloqueada 15 minutos; espera o usa "¿Olvidaste tu contraseña?" para entrar ya." Si la persona restablece la contraseña, puede entrar de inmediato. La sesión dura una hora; al vencerse, el sistema vuelve a la pantalla de inicio de sesión con el mensaje "Tu sesión expiró. Inicia sesión de nuevo." Una cuenta desactivada no puede ingresar y recibe el mensaje "Tu cuenta está desactivada. Contacta al administrador."

**Figura 4**

*Pantalla de Inicio de Sesión*

![Pantalla de Inicio de Sesión](capturas/usuario-04-pantalla-de-inicio-de-sesion.jpg)

*Nota.* Usar un correo de prueba; no mostrar contraseñas reales.

### 8.3 Recuperación de la Contraseña

**Nombre del módulo:** Recuperación de la contraseña.

**Descripción:** Permite recuperar el acceso a la cuenta cuando se olvidó la contraseña, mediante un código de verificación de seis dígitos enviado por correo.

**Rol que puede usarlo:** Cliente, Operario y Administrador.

**Ruta o menú donde se encuentra:** Pantalla de inicio de sesión > enlace **¿Olvidaste tu contraseña?** (ruta */auth/forgot-password*).

**Pasos para utilizarlo:**

1. En la pantalla de inicio de sesión, hacer clic en **¿Olvidaste tu contraseña?**.
2. **Paso 1 (Recuperar Contraseña):** escribir el correo de la cuenta y hacer clic en **Enviar Código**.
3. Abrir el correo recibido y copiar el código de seis dígitos. El código es válido durante 15 minutos.
4. **Paso 2 (Verificación):** escribir los seis dígitos, uno en cada casilla, y hacer clic en **Verificar Código**. Si el correo no llegó, hacer clic en **¿No recibiste el código? Reenviar**.
5. **Paso 3 (Nueva Contraseña):** escribir la nueva contraseña, que debe cumplir los cuatro requisitos, confirmarla y hacer clic en **Actualizar Contraseña**.
6. Cuando aparezca el mensaje "¡Contraseña actualizada!", hacer clic en **Ir a iniciar sesión** e ingresar con la nueva contraseña.

**Resultado esperado:** La contraseña se cambia y el código usado no puede volver a usarse.

**Observaciones o restricciones:** Por seguridad, el sistema muestra la misma pantalla esté o no registrado el correo, de modo que no revela qué cuentas existen. Cada código nuevo invalida el anterior ("Te enviamos un código nuevo. El anterior ya no sirve."). Después de cinco intentos incorrectos el código deja de funcionar y se debe solicitar uno nuevo. Un indicador de tres pasos en la parte superior muestra la etapa del proceso.

**Figura 5**

*Recuperación de la Contraseña, Paso 1: Correo Electrónico*

![Recuperación de la Contraseña, Paso 1: Correo Electrónico](capturas/usuario-05-recuperacion-de-la-contrasena-paso-1-correo-elec.jpg)

**Figura 6**

*Recuperación de la Contraseña, Paso 2: Código de Verificación*

![Recuperación de la Contraseña, Paso 2: Código de Verificación](capturas/usuario-06-recuperacion-de-la-contrasena-paso-2-codigo-de-v.jpg)

**Figura 7**

*Recuperación de la Contraseña, Paso 3: Nueva Contraseña*

![Recuperación de la Contraseña, Paso 3: Nueva Contraseña](capturas/usuario-07-recuperacion-de-la-contrasena-paso-3-nueva-contr.jpg)

**Figura 8**

*Confirmación del Cambio de Contraseña*

![Confirmación del Cambio de Contraseña](capturas/usuario-08-confirmacion-del-cambio-de-contrasena.jpg)

## 9. Menú Principal

Después de iniciar sesión, el sistema muestra un menú lateral con las opciones del rol de la persona. En la parte superior del menú aparecen las iniciales, el nombre y el correo de la persona con la sesión abierta; en la parte inferior está la opción **Cerrar Sesión**. En el teléfono, el menú se abre y se cierra con el ícono de menú.

### 9.1 Menú del Cliente

**Tabla 5**

*Opciones del Menú Principal del Rol Cliente*

| Opción (ruta) | Para qué sirve |
|---|---|
| Dashboard (/client) | Muestra un resumen de reservas, vehículos, el próximo servicio, accesos rápidos, el progreso de fidelidad y los beneficios. |
| Perfil (/client/profile) | Permite ver y editar los datos personales, cambiar el correo y la contraseña, y desactivar la cuenta. |
| Mis vehículos (/client/vehicles) | Permite registrar, editar, eliminar y ver los vehículos del cliente. |
| Reservar lavado (/client/reserve) | Permite programar un nuevo servicio de lavado. |
| Pagar servicio (/client/payment) | Permite pagar una reserva con código QR o en efectivo, canjear un cupón y cancelarla. |
| Notificaciones (/client/notifications) | Muestra los avisos de reservas, recordatorios, asignaciones, avance del servicio, pagos, puntos y cupones. |
| Historial (/client/history) | Lista las reservas con el estado de su pago y permite pagarlas, cancelarlas y calificarlas. |
| Configuración (/client/configuration) | Permite elegir el tema, el idioma y las preferencias de notificación, y abrir el centro de ayuda y los documentos legales. |
| Cerrar Sesión | Termina la sesión de forma segura. |

*Nota.* Los nombres de las opciones son los del menú lateral cuando la interfaz está en español.

**Figura 9**

*Menú Lateral del Rol Cliente*

![Menú Lateral del Rol Cliente](capturas/usuario-09-menu-lateral-del-rol-cliente.jpg)

### 9.2 Menú del Operario

**Tabla 6**

*Opciones del Menú Principal del Rol Operario*

| Opción (ruta) | Para qué sirve |
|---|---|
| Dashboard (/operator) | Muestra los servicios pendientes, el avance del día e indicadores de resumen. |
| Perfil (/operator/profile) | Permite ver y editar los datos personales y cambiar la contraseña. |
| Mi Agenda (/operator/schedule) | Muestra los servicios por día o por semana y permite iniciarlos y finalizarlos. |
| Servicios asignados (/operator/assigned-services) | Lista los servicios asignados con su detalle y permite iniciarlos y finalizarlos. |
| Notificaciones (/operator/notifications) | Muestra los avisos de asignaciones, reprogramaciones, cancelaciones y reasignaciones. |
| Historial (/operator/service-history) | Lista los servicios realizados con su estado final y su calificación. |
| Calificaciones (/operator/qualifications) | Muestra las calificaciones que dejaron los clientes. |
| Configuración (/operator/settings) | Permite elegir el tema y el idioma y abrir el centro de ayuda. |
| Cerrar Sesión | Termina la sesión de forma segura. |

*Nota.* Los nombres de las opciones son los del menú lateral cuando la interfaz está en español. La ruta antigua de tareas del operario redirige a Servicios asignados.

**Figura 10**

*Menú Lateral del Rol Operario*

![Menú Lateral del Rol Operario](capturas/usuario-10-menu-lateral-del-rol-operario.jpg)

## 10. Módulos del Sistema

Cada módulo se documenta con el mismo formato: nombre, descripción, rol que puede usarlo, ruta o menú, pasos, resultado esperado y observaciones. Los módulos se agrupan por rol.

### 10.1 Módulos del Rol Cliente

#### 10.1.1 Panel del Cliente

**Nombre del módulo:** Panel del cliente.

**Descripción:** Pantalla de inicio del cliente. Resume la actividad y ofrece atajos a las acciones más frecuentes.

**Rol que puede usarlo:** Cliente.

**Ruta o menú donde se encuentra:** Menú lateral > **Dashboard** (ruta */client*).

**Pasos para utilizarlo:**

1. Iniciar sesión con una cuenta de cliente; el sistema abre el panel automáticamente.
2. Revisar las tarjetas de resumen: **Reservas activas**, **Mis vehículos** y **Lavados realizados**.
3. Consultar el bloque **Tu próximo servicio**, que muestra el servicio, el vehículo, la fecha, la hora, el **Operario asignado** y el avance del servicio. El avance queda en 0 % mientras la reserva está programada o confirmada, porque el lavado aún no ha empezado; sube cuando el operario inicia el servicio y llega a 100 % al finalizar. Hacer clic en **Ver detalle** para ver toda la información.
4. Usar los **Accesos rápidos** (Agendar lavado, Pagar servicio, Mis vehículos y Notificaciones) para ir directamente a cada módulo.
5. Revisar el bloque **Tus beneficios y promociones**: la barra **Progreso de fidelidad** muestra los puntos acumulados ("N de M puntos") y, para cada promoción, indica "¡Ya la desbloqueaste! Cánjala al pagar." o cuántos puntos faltan para desbloquearla ("Te faltan N puntos para desbloquearla").

**Resultado esperado:** El cliente ve la información más importante y llega a cualquier módulo con un solo clic.

**Observaciones o restricciones:** Si no hay reservas, el bloque muestra "No tienes servicios programados" en lugar de una pantalla vacía. Los puntos se acreditan cuando el administrador aprueba el pago de una reserva (o registra un pago en el local), no cuando termina el servicio; hasta que se apruebe el primer pago, el bloque de beneficios muestra "Aún no tienes datos de fidelidad". Los puntos nunca se gastan: desbloquean cupones, y canjear un cupón no reduce el saldo.

**Figura 11**

*Panel del Cliente*

![Panel del Cliente](capturas/usuario-11-panel-del-cliente.jpg)

#### 10.1.2 Mis Vehículos

**Nombre del módulo:** Mis vehículos.

**Descripción:** Permite registrar los vehículos del cliente y ver, para cada uno, el último lavado y el total de lavados. Se debe registrar un vehículo antes de poder reservar un servicio.

**Rol que puede usarlo:** Cliente.

**Ruta o menú donde se encuentra:** Menú lateral > **Mis vehículos** (ruta */client/vehicles*).

**Pasos para utilizarlo:**

1. Hacer clic en **Mis vehículos** en el menú lateral.
2. Revisar los indicadores de la parte superior: **Vehículos registrados**, **Lavados acumulados** y **Último lavado realizado**.
3. Para agregar un vehículo, hacer clic en **Registrar vehículo**.
4. En la ventana "Registrar nuevo vehículo", seleccionar el **Tipo de vehículo** (automóvil, sedán, camioneta SUV, pickup, camión o motocicleta) y escribir la **Marca**, el **Modelo**, la **Placa** y el **Color**.
5. Hacer clic en **Guardar vehículo** y verificar que el vehículo aparezca en la lista con el mensaje "¡Vehículo registrado!".
6. Para corregir los datos de un vehículo, usar la opción de editar de su tarjeta, cambiar los campos y hacer clic en **Guardar cambios**.
7. Para retirar un vehículo, usar la opción de eliminar de su tarjeta y confirmar en la ventana "¿Eliminar vehículo?".

**Resultado esperado:** El vehículo queda registrado y disponible para seleccionarlo al reservar un lavado.

**Observaciones o restricciones:** La placa debe ser una placa colombiana oficial: tres letras y tres números para automóviles y demás vehículos (por ejemplo, ABC123), o tres letras, dos números y una letra para motocicletas (por ejemplo, ABC12D). No se aceptan placas extranjeras ni promocionales. La marca es obligatoria (al menos dos caracteres) y el color solo admite letras. La misma placa no se puede registrar dos veces mientras el vehículo esté activo. El tipo de vehículo importa porque determina el precio de cada servicio.

**Figura 12**

*Lista de Vehículos del Cliente*

![Lista de Vehículos del Cliente](capturas/usuario-12-lista-de-vehiculos-del-cliente.jpg)

**Figura 13**

*Formulario para Registrar un Vehículo*

![Formulario para Registrar un Vehículo](capturas/usuario-13-formulario-para-registrar-un-vehiculo.jpg)

#### 10.1.3 Reservar un Lavado

**Nombre del módulo:** Reservar lavado.

**Descripción:** Permite programar un turno de lavado eligiendo el vehículo, el tipo de servicio, la fecha y la hora. El sistema solo ofrece horas que están realmente libres.

**Rol que puede usarlo:** Cliente.

**Ruta o menú donde se encuentra:** Menú lateral > **Reservar lavado** (ruta */client/reserve*), o el acceso rápido **Agendar lavado**.

**Pasos para utilizarlo:**

1. Hacer clic en **Reservar lavado**.
2. **Paso 1 (Elige tu vehículo):** seleccionar uno de los vehículos registrados. Si el vehículo no aparece, usar el enlace **Mis Vehículos** para registrarlo primero.
3. **Paso 2 (Tipo de servicio):** seleccionar Básico, Premium o Completo. Cada tarjeta muestra qué incluye, la duración, el precio para el tipo de vehículo elegido y los puntos de fidelización que suma ("Suma N puntos").
4. **Paso 3 (Fecha y hora):** elegir la fecha (el calendario no deja escoger días pasados) y luego una de las horas libres que aparecen en **Selecciona una hora**. Las horas se ofrecen cada 30 minutos, dentro del horario de atención, fuera del descanso y solo cuando hay una bahía de lavado libre durante toda la duración del servicio.
5. Si se desea, elegir en **Operario (opcional)** uno de los operarios libres a esa hora. Si se deja en "Sin preferencia: te asignamos uno libre", el sistema asigna uno automáticamente.
6. Revisar el **Resumen de tu reserva**: vehículo, placa, servicio, duración estimada, fecha, hora, ubicación, total y **Puntos que ganas**.
7. Hacer clic en **Reservar Ahora**.

**Resultado esperado:** La reserva se crea de inmediato con el estado Confirmada y una bahía de lavado. El sistema muestra "¡Reserva creada!" con el código de la reserva, y el botón **Ir a pagar** abre la pantalla de pago de esa reserva. El cliente recibe la confirmación en sus notificaciones y por correo.

**Observaciones o restricciones:**

- Elegir el operario es opcional. Si el operario elegido ya no está libre al confirmar, el sistema asigna otro ("Si el operario que elegiste ya no está libre al confirmar, te asignamos otro."). El operario asignado se ve en el panel y en las notificaciones, y el administrador puede cambiarlo después.
- Las reservas se pueden hacer con hasta 60 días de anticipación.
- Si el día está cerrado, el sistema muestra "Ese día el lavadero está cerrado"; si no hay horas libres, "No hay horas libres ese día".
- Si otra persona toma la hora mientras el cliente está reservando, el sistema no guarda nada, muestra "Esa hora ya se ocupó" y lista las horas libres más cercanas de ese mismo día (hasta cinco) para que el cliente elija otra.
- Si la hora elegida no se puede reservar por otro motivo, el sistema explica cuál: "El lavadero no abre ese día. Elige otra fecha.", "A esa hora el servicio no cabe en el horario de atención. Elige otra hora." o "Esa hora ya pasó. Elige una hora más tarde."
- Un vehículo no puede tener dos reservas a la misma hora ("Ese vehículo ya tiene una reserva a esa hora.").
- El servicio se presta en el lavadero: el cliente debe llevar el vehículo en la fecha y la hora reservadas.

**Figura 14**

*Reservar un Lavado, Pasos 1 y 2: Vehículo y Servicio*

![Reservar un Lavado, Pasos 1 y 2: Vehículo y Servicio](capturas/usuario-14-reservar-un-lavado-pasos-1-y-2-vehiculo-y-servic.jpg)

**Figura 15**

*Reservar un Lavado, Paso 3 y Resumen*

![Reservar un Lavado, Paso 3 y Resumen](capturas/usuario-15-reservar-un-lavado-paso-3-y-resumen.jpg)

**Figura 16**

*Confirmación de la Reserva*

![Confirmación de la Reserva](capturas/usuario-16-confirmacion-de-la-reserva.jpg)

#### 10.1.4 Consultar o Cancelar una Reserva

**Nombre del módulo:** Seguimiento y cancelación de reservas.

**Descripción:** Permite consultar el estado de una reserva y cancelarla antes de que empiece el servicio.

**Rol que puede usarlo:** Cliente.

**Ruta o menú donde se encuentra:** Dashboard > **Tu próximo servicio** > **Ver detalle**; menú lateral > **Historial**; o menú lateral > **Pagar servicio**.

**Pasos para utilizarlo:**

1. Abrir el **Dashboard** o el **Historial** y ubicar la reserva.
2. En el Dashboard, hacer clic en **Ver detalle** para consultar el servicio, el vehículo, la fecha, la hora, el operario asignado y el estado. En el **Historial**, hacer clic en la tarjeta de la reserva para ver su detalle (sección 10.1.6).
3. Para cancelar, hacer clic en **Cancelar reserva** en la tarjeta de la reserva en **Historial** (o en la pantalla **Pagar servicio**).
4. Leer el mensaje "¿Cancelar reserva?" y hacer clic en **Sí, cancelar**; hacer clic en **Volver** para conservar la reserva.

**Resultado esperado:** La reserva cambia a Cancelada, aparece el mensaje "Reserva cancelada", el cliente recibe el aviso por correo y el turno queda libre para otros clientes.

**Observaciones o restricciones:** Una reserva solo se puede cancelar antes de su hora de inicio; después, el sistema muestra "Esta reserva ya no se puede cambiar." La cancelación no se puede deshacer. La aplicación web no ofrece la opción de cambiar la fecha o la hora de una reserva: para moverla, el cliente la cancela y reserva de nuevo, o contacta al lavadero para que el administrador la reprograme.

**Tabla 7**

*Estados de una Reserva*

| Estado | Significado | ¿El cliente puede cancelarla? |
|---|---|---|
| Programada | La reserva se registró y está pendiente de confirmación. | Sí, antes de la hora de inicio. |
| Confirmada | La reserva tiene turno y bahía de lavado. Las reservas que hace el cliente se crean con este estado. | Sí, antes de la hora de inicio. |
| En progreso | El operario inició el lavado. | No. |
| Completada | El servicio terminó; desde este estado se puede calificar. | No. |
| Cancelada | La reserva fue anulada por el cliente o por el lavadero. | No aplica. |
| No asistió | El cliente no llegó al turno reservado. | No aplica. |

*Nota.* Códigos SCHEDULED, CONFIRMED, IN_PROGRESS, COMPLETED, CANCELLED y NO_SHOW en la base de datos; la interfaz los traduce.

**Figura 17**

*Confirmación de la Cancelación de una Reserva*

![Confirmación de la Cancelación de una Reserva](capturas/usuario-17-confirmacion-de-la-cancelacion-de-una-reserva.jpg)

#### 10.1.5 Pagar un Servicio

El pago se hace por transferencia a la cuenta del lavadero (escaneando su código QR o usando los datos de su cuenta) o en efectivo en el local. El sistema **no solicita ni guarda datos de tarjetas de crédito o débito** y no se conecta con los bancos: un administrador verifica manualmente cada pago digital (Tabla 8).

**Tabla 8**

*Métodos de Pago Disponibles*

| Método | Cómo se paga | ¿Requiere comprobante? |
|---|---|---|
| Nequi | Se escanea el código QR y se hace la transferencia desde la aplicación. | Sí |
| Daviplata | Se escanea el código QR y se hace la transferencia desde la aplicación. | Sí |
| Transferencia | Se escanea el código QR o se usan los datos de la cuenta que se muestran. | Sí |
| Efectivo | Se paga en el lavadero al recibir el servicio. No se muestra código QR. | No; el administrador registra el pago en el local. |

*Nota.* Los métodos digitales que se muestran dependen de las cuentas de pago que el administrador mantenga activas.

**Nombre del módulo:** Pagar servicio.

**Descripción:** Permite pagar una reserva adjuntando el comprobante del pago digital, o anunciar que se pagará en efectivo, con la opción de canjear un cupón de descuento.

**Rol que puede usarlo:** Cliente.

**Ruta o menú donde se encuentra:** Menú lateral > **Pagar servicio** (ruta */client/payment*); también **Ir a pagar** después de reservar, o **Pagar ahora** en el Historial.

**Pasos para utilizarlo:**

1. Abrir **Pagar servicio** y revisar el **Resumen de la reserva**: servicio, vehículo, **Subtotal**, **Descuento aplicado** y **TOTAL A PAGAR** (IVA del 19 % incluido).
2. Si se tiene un cupón desbloqueado, escribirlo en **Código del cupón** y hacer clic en **Aplicar**. Aparece el mensaje "Cupón aplicado: [nombre]" y el descuento se resta del total a pagar.
3. En **Selecciona tu método de pago**, elegir Nequi, Daviplata, Transferencia o Efectivo.
4. Para un método digital: escanear el código QR con la aplicación bancaria o la billetera, o copiar el número que aparece en **Llave / Cuenta autorizada** con **Copiar número**, y transferir exactamente el **Monto a pagar**.
5. En **Confirma tu pago**, arrastrar la imagen del comprobante o hacer clic para buscarla (JPG o PNG, máximo 10 MB).
6. Escribir la **Referencia de la transacción** impresa en el comprobante (de 8 a 12 letras o números emitidos por el banco) y revisar el **Monto pagado** (mayor que 0), que debe coincidir con lo transferido.
7. Hacer clic en **Ya realicé el pago**. Mientras falten datos, el botón permanece deshabilitado y la lista "Para confirmar el pago te falta:" indica lo pendiente (comprobante, referencia o monto).
8. Para efectivo: seleccionar **Efectivo** y hacer clic en **Confirmar reserva**; el pago se hace en el lavadero al recoger el vehículo.

**Resultado esperado:** El sistema muestra "¡Pago enviado!" y el pago queda en revisión ("Pago en verificación") hasta que un administrador lo apruebe o lo rechace. El cliente recibe una notificación y un correo con el resultado.

**Observaciones o restricciones:**

- El monto a pagar siempre lo calcula el sistema (total de la reserva menos el cupón aplicado, si lo hay); el cliente no puede cambiarlo. El administrador compara el monto pagado que declara el cliente con el comprobante y con el banco.
- Solo se pueden pagar las reservas en estado Confirmada, En progreso o Completada.
- Mientras un pago está en revisión no se puede reportar otro para la misma reserva; una reserva admite un solo pago aprobado.
- Si el administrador rechaza el pago, el cliente puede reportarlo de nuevo con un comprobante correcto.
- Cuando el pago se aprueba, el cliente recibe el aviso de pago confirmado (bandeja y correo), los puntos de fidelización de la reserva ("Ganaste N puntos", solo en la bandeja) y, por cada cupón que esos puntos desbloquean, el aviso "¡Tienes un cupón canjeable!" con su código (bandeja y correo). Si el pago se rechaza o se reembolsa, el cliente recibe un aviso y un correo; un reembolso revierte los puntos ganados por esa reserva.
- Cuando el pago queda aprobado, la pantalla **Pagar servicio** de esa reserva solo muestra el resumen: desaparecen el método de pago, el código QR, la carga del comprobante y el botón **Ya realicé el pago**, y el cupón usado (si lo hay) ya no se puede quitar.
- Un cupón se acepta solo si está activo, está dentro de sus fechas y el cliente alcanzó los puntos que exige; se puede canjear una vez por reserva. El sistema responde "Ese cupón no existe.", "Ese cupón no está vigente o todavía no acumulas los puntos necesarios." o "Ya canjeaste este cupón en esta reserva." Un canje exitoso envía un aviso y un correo de confirmación.

**Tabla 9**

*Estados de un Pago*

| Estado | Significado | Qué debe hacer el cliente |
|---|---|---|
| Pendiente | La reserva todavía no tiene un pago aprobado. | Hacer el pago. |
| En revisión | Se envió el comprobante y espera la verificación del administrador. | Esperar la verificación. |
| Aprobado | El administrador verificó el pago. | Ninguna acción. |
| Rechazado | No se pudo verificar el pago; el administrador registra el motivo. | Reportar de nuevo el pago con un comprobante correcto. |
| Reembolsado | El valor del pago se devolvió al cliente. | Ninguna acción. |

*Nota.* Códigos PENDING, IN_REVIEW, APPROVED, REJECTED y REFUNDED en la base de datos. En las tarjetas del Historial se muestran como Pendiente de verificación, En revisión, Pagado, Rechazado y Reembolsado.

**Figura 18**

*Selección del Método de Pago y Resumen de la Reserva*

![Selección del Método de Pago y Resumen de la Reserva](capturas/usuario-18-seleccion-del-metodo-de-pago-y-resumen-de-la-res.jpg)

**Figura 19**

*Código QR y Carga del Comprobante*

![Código QR y Carga del Comprobante](capturas/usuario-19-codigo-qr-y-carga-del-comprobante.jpg)

*Nota.* Usar un código QR de prueba; no mostrar cuentas bancarias reales.

#### 10.1.6 Historial y Calificación

**Nombre del módulo:** Historial.

**Descripción:** Lista las reservas del cliente con su estado y el estado de su pago, y permite pagarlas, cancelarlas y calificarlas.

**Rol que puede usarlo:** Cliente.

**Ruta o menú donde se encuentra:** Menú lateral > **Historial** (ruta */client/history*).

**Pasos para utilizarlo:**

1. Hacer clic en **Historial**. Las reservas aparecen de la más reciente a la más antigua.
2. Usar los filtros **Todas**, **Activas**, **Completadas** y **Canceladas**, y las fechas **Desde** y **Hasta**, para acotar la lista.
3. Usar **Buscar por servicio, vehículo o código** para encontrar una reserva.
4. En cada tarjeta, revisar el **Tipo de servicio**, el **Vehículo**, el **Estado** y el estado del **Pago**, y usar **Pagar ahora** o **Cancelar reserva** cuando estén disponibles. **Pagar ahora** aparece solo cuando la reserva se puede pagar (estado pagable, sin un pago aprobado y sin uno pendiente o en revisión).
5. Hacer clic en la tarjeta para abrir el **Detalle de la reserva** (servicios, fecha y hora, vehículo, total, estado del pago y calificación). El botón **Ir al pago** lleva a la pantalla de pago de esa reserva; no aparece en las reservas canceladas o en las que el cliente no asistió.
6. En un servicio completado, hacer clic en **Calificar Servicio**.
7. Elegir de una a cinco estrellas, escribir un comentario si se desea (máximo 500 caracteres) y hacer clic en **Enviar calificación**.

**Resultado esperado:** Aparece el mensaje "¡Gracias por tu calificación!", la tarjeta muestra **Calificado** y el operario que realizó el servicio puede ver la calificación.

**Observaciones o restricciones:** La calificación es opcional, se permite una sola vez por reserva y solo cuando la reserva está Completada; después no se puede modificar. Si no hay reservas para los filtros elegidos, el sistema muestra "No se encontraron servicios".

**Figura 20**

*Historial con Filtros*

![Historial con Filtros](capturas/usuario-20-historial-con-filtros.jpg)

**Figura 21**

*Calificación de un Servicio Completado*

![Calificación de un Servicio Completado](capturas/usuario-21-calificacion-de-un-servicio-completado.jpg)

#### 10.1.7 Notificaciones

**Nombre del módulo:** Notificaciones.

**Descripción:** Reúne los avisos del sistema (reserva creada, confirmada o cancelada, recordatorios, operario asignado, servicio iniciado y completado, pago confirmado, rechazado o reembolsado, puntos ganados, cupón desbloqueado o canjeado, e informe de inspección del vehículo) e indica cuáles se han leído.

**Rol que puede usarlo:** Cliente y Operario.

**Ruta o menú donde se encuentra:** Menú lateral > **Notificaciones**.

**Pasos para utilizarlo:**

1. Hacer clic en **Notificaciones**. El encabezado muestra cuántas notificaciones no se han leído.
2. Usar las pestañas **Todas**, **Recordatorios**, **Promociones**, **Confirmaciones** y **Otras** para filtrar por tipo.
3. Usar el filtro **Estado de lectura** y las fechas para acotar la lista.
4. Hacer clic en una notificación (o en **Ver detalle**) para leerla completa; queda marcada como leída. Si el aviso pertenece a un apartado, el detalle trae un botón para ir allí: **Ir al historial** (reservas, pagos, servicio e informe de inspección) o **Ir al inicio** (bienvenida, puntos y cupones); en el operario, **Ir a servicios asignados**.
5. Usar **Marcar leído** o **Marcar no leído** en cada notificación, o **Marcar todo como leído**.
6. Para eliminar una notificación, usar la opción de eliminar y confirmar "¿Eliminar esta notificación?".

**Resultado esperado:** La persona se mantiene informada sin tener que revisar cada módulo constantemente.

**Observaciones o restricciones:** El sistema envía recordatorios 24 horas y 1 hora antes de cada reserva. Los avisos que cambian algo para el cliente también llegan por correo: bienvenida, reserva creada, confirmada o cancelada y recordatorios, pago confirmado, rechazado o reembolsado, cupón canjeado o desbloqueado, e informe de inspección. El avance del servicio (operario asignado, iniciado y completado) y los puntos ganados llegan solo a la bandeja y como notificación push. El código de recuperación de la contraseña siempre llega por correo. Los interruptores de **Configuración > Notificaciones** deciden solo los canales externos; la bandeja siempre recibe todos los avisos. Una notificación eliminada no se puede recuperar.

**Figura 22**

*Centro de Notificaciones*

![Centro de Notificaciones](capturas/usuario-22-centro-de-notificaciones.jpg)

#### 10.1.8 Perfil

**Nombre del módulo:** Perfil.

**Descripción:** Permite ver y actualizar los datos personales, cambiar el correo y la contraseña, y desactivar la cuenta.

**Rol que puede usarlo:** Cliente, Operario y Administrador.

**Ruta o menú donde se encuentra:** Menú lateral > **Perfil**.

**Pasos para utilizarlo:**

1. Hacer clic en **Perfil**. La pantalla "Mi Perfil" se abre en modo de consulta con los nombres, apellidos, correo, teléfono y la fecha desde la cual la persona es cliente.
2. Para modificar los datos, hacer clic en **Editar perfil**, cambiar los campos y hacer clic en **Guardar**; aparece el mensaje "¡Perfil actualizado!".
3. Para cambiar el correo, que es el usuario de ingreso, escribir el nuevo y confirmar con la contraseña actual en la ventana "Confirma el cambio de correo"; desde ese momento se ingresa con el nuevo correo.
4. Para cambiar la contraseña, ir a **Contraseña** y hacer clic en **Cambiar**. Escribir la **Contraseña actual**, la **Nueva contraseña** y **Confirmar nueva contraseña**, y hacer clic en **Guardar**.
5. Para dejar de usar la cuenta, ir a **Cuenta**, hacer clic en **Desactivar mi cuenta**, leer el mensaje y confirmar con la contraseña.

**Resultado esperado:** Los datos quedan actualizados. Si se cambió la contraseña, la nueva se usa en el siguiente ingreso.

**Observaciones o restricciones:** Si la contraseña actual es incorrecta, el cambio se rechaza ("La contraseña actual es incorrecta"); la nueva contraseña debe ser distinta de la actual. La cuenta se desactiva, no se borra: la persona ya no puede ingresar y sus sesiones se cierran, pero se conserva el historial de reservas y pagos. Para reactivarla, la persona debe contactar al administrador. La **Dirección** se guarda en la cuenta, por lo que aparece igual en cualquier dispositivo.

**Figura 23**

*Perfil del Usuario*

![Perfil del Usuario](capturas/usuario-23-perfil-del-usuario.jpg)

#### 10.1.9 Configuración

**Nombre del módulo:** Configuración.

**Descripción:** Permite personalizar la apariencia, el idioma y las preferencias de notificación, y abrir el centro de ayuda y los documentos legales.

**Rol que puede usarlo:** Cliente, Operario y Administrador.

**Ruta o menú donde se encuentra:** Menú lateral > **Configuración** (ruta */client/configuration* para el cliente).

**Pasos para utilizarlo:**

1. Hacer clic en **Configuración**.
2. En **Apariencia**, hacer clic en **Elegir tema** y seleccionar uno de los cuatro temas de color. El cambio se aplica de inmediato.
3. En **Idiomas**, seleccionar Español, English, Français o Português. Todos los textos de la interfaz cambian al idioma elegido.
4. En **Notificaciones**, activar o desactivar **Notificaciones Push**, **Recordatorios por Email** (recordatorios de la reserva por correo, un día y una hora antes) y **Promociones y Ofertas** (avisos de los cupones que se desbloquean con los puntos, por correo y push).
5. En **Ayuda**, hacer clic en **Abrir** para ver el **Centro de ayuda**: línea de atención, correo, horario de atención (de lunes a sábado, de 7:00 a. m. a 6:30 p. m.) y dirección, tomados de los datos del lavadero registrados en el sistema.
6. En **Legal y privacidad**, abrir **Ver Términos y Condiciones** o **Ver Política de Datos**.

**Resultado esperado:** El tema, el idioma y los interruptores de notificación se aplican de inmediato y se guardan en la cuenta, de modo que se conservan en el siguiente ingreso y en cualquier dispositivo.

**Observaciones o restricciones:** Desactivar **Notificaciones Push** detiene los avisos al teléfono; desactivar **Recordatorios por Email** detiene solo los correos de recordatorio; desactivar **Promociones y Ofertas** detiene los avisos por correo y push de los cupones desbloqueados. Ningún interruptor afecta la bandeja. Si el cambio no se puede guardar, el sistema muestra "No se pudieron guardar tus preferencias de notificación. Inténtalo de nuevo." Las fechas se muestran en el formato del idioma seleccionado.

**Figura 24**

*Pantalla de Configuración*

![Pantalla de Configuración](capturas/usuario-24-pantalla-de-configuracion.jpg)

### 10.2 Módulos del Rol Operario

El operario recibe la cuenta del administrador del negocio. El operario solo puede ver y actualizar los servicios que tiene asignados; el sistema rechaza cualquier intento de cambiar un servicio de otro operario.

#### 10.2.1 Panel del Operario

**Nombre del módulo:** Panel del operario.

**Descripción:** Pantalla de inicio del operario. Resume el trabajo pendiente y el avance del día.

**Rol que puede usarlo:** Operario.

**Ruta o menú donde se encuentra:** Menú lateral > **Dashboard** (ruta */operator*).

**Pasos para utilizarlo:**

1. Iniciar sesión con una cuenta de operario; el sistema abre el panel automáticamente.
2. Leer el saludo, que indica cuántos servicios pendientes hay para el día, y hacer clic en **Ver servicios asignados** para ir a la lista.
3. Revisar los indicadores (reservas asignadas, servicios en curso, notificaciones y calificación) y la barra de avance **Servicios completados hoy**.
4. En **Servicios de hoy**, revisar los próximos servicios asignados con su tipo, vehículo, hora, cliente y estado, y hacer clic en **Iniciar** cuando sea el momento de empezar uno.

**Resultado esperado:** El operario sabe de un vistazo qué servicios debe realizar.

**Observaciones o restricciones:** Si no hay servicios asignados, el sistema muestra "No tienes servicios programados por ahora."

**Figura 25**

*Panel del Operario*

![Panel del Operario](capturas/usuario-25-panel-del-operario.jpg)

#### 10.2.2 Mi Agenda

**Nombre del módulo:** Mi Agenda.

**Descripción:** Muestra las reservas del operario en un calendario, por día o por semana, y permite iniciarlas y finalizarlas.

**Rol que puede usarlo:** Operario.

**Ruta o menú donde se encuentra:** Menú lateral > **Mi Agenda** (ruta */operator/schedule*).

**Pasos para utilizarlo:**

1. Hacer clic en **Mi Agenda**.
2. Seleccionar un día en el calendario o cambiar entre las pestañas **Día**, **Semana** y **Completados**.
3. Revisar los totales: **Total**, **Pendientes**, **En progreso** y **Completados**.
4. Consultar el bloque **Próximo servicio**, que indica cuántos minutos faltan para que empiece.
5. En la lista de reservas, hacer clic en **Iniciar** o **Finalizar** según el estado de cada servicio, o en **Ver detalle** para ver la fecha, la duración y el vehículo.

**Resultado esperado:** El estado del servicio cambia y el cliente puede seguir su avance.

**Observaciones o restricciones:** Un servicio solo se puede iniciar el día de la reserva, y solo puede haber un servicio en curso a la vez. Un servicio debe iniciarse antes de poder finalizarlo ("Primero debes iniciar el servicio."). Al finalizar, el sistema pregunta "¿Finalizar este servicio?" y lo pasa al historial.

**Figura 26**

*Agenda del Operario*

![Agenda del Operario](capturas/usuario-26-agenda-del-operario.jpg)

#### 10.2.3 Servicios Asignados

**Nombre del módulo:** Servicios asignados.

**Descripción:** Lista todos los servicios asignados al operario y permite iniciarlos y finalizarlos.

**Rol que puede usarlo:** Operario.

**Ruta o menú donde se encuentra:** Menú lateral > **Servicios asignados** (ruta */operator/assigned-services*).

**Pasos para utilizarlo:**

1. Hacer clic en **Servicios asignados**.
2. Revisar las tarjetas: **Servicios Totales**, **Pendientes**, **En Progreso** y **Finalizados Hoy**.
3. Usar **Filtrar por fecha**, **Filtrar por tipo de servicio** o el cuadro de búsqueda, y hacer clic en **Filtrar**.
4. En la tabla, leer el **ID**, el **Tipo de servicio**, la fecha y hora, el **Vehículo**, el **Cliente** y el **Estado** de cada servicio.
5. Hacer clic en un servicio para abrir **Información del servicio**: cliente, vehículo, tipo de servicio, hora programada y método de pago.
6. Hacer clic en **Iniciar Servicio** al comenzar el lavado y confirmar con **Iniciar**.
7. Al terminar el lavado, hacer clic en **Finalizar Servicio** y confirmar con **Finalizar**.
8. Si es necesario comunicarse con el cliente, usar **Contactar al cliente** en **Opciones adicionales**.

**Resultado esperado:** El estado cambia a En progreso y luego a Completado ("¡Servicio finalizado!"). El cliente recibe los avisos y puede calificar el servicio.

**Observaciones o restricciones:** El servicio se puede iniciar desde 15 minutos antes de la hora reservada. El operario solo puede actualizar los servicios que tiene asignados.

**Tabla 10**

*Estados del Servicio que Ve el Operario*

| Estado | Significado | Acción disponible |
|---|---|---|
| Pendiente | El servicio fue asignado y todavía no ha comenzado. | Iniciar Servicio (desde 15 minutos antes de la hora reservada). |
| En progreso | El operario inició el lavado. | Finalizar Servicio. |
| Completado | El lavado terminó y el cliente puede calificarlo. | Solo consulta. |

*Nota.* La base de datos también define los estados de ejecución PAUSED y WITH_ISSUE, que la interfaz actual no usa.

**Figura 27**

*Lista de Servicios Asignados con Filtros*

![Lista de Servicios Asignados con Filtros](capturas/usuario-27-lista-de-servicios-asignados-con-filtros.jpg)

**Figura 28**

*Información del Servicio y Botones de Acción*

![Información del Servicio y Botones de Acción](capturas/usuario-28-informacion-del-servicio-y-botones-de-accion.jpg)

#### 10.2.4 Notificaciones del Operario

Las notificaciones del operario funcionan como las del cliente (sección 10.1.7). Los avisos más frecuentes son un nuevo servicio asignado, un servicio movido a otra hora, un servicio cancelado y un servicio reasignado a otro operario. Estos avisos al personal llegan a la bandeja y como notificación push, nunca por correo. El operario los abre con **Notificaciones** en el menú lateral y usa las pestañas, los filtros y los botones **Marcar leído** y **Marcar todo como leído**. Al hacer clic en uno de estos avisos se abre su detalle con el botón **Ir a servicios asignados**.

**Figura 29**

*Notificaciones del Operario*

![Notificaciones del Operario](capturas/usuario-29-notificaciones-del-operario.jpg)

#### 10.2.5 Historial de Servicios

**Nombre del módulo:** Historial de servicios.

**Descripción:** Lista los servicios del operario con su fecha, vehículo, pago, calificación y estado final.

**Rol que puede usarlo:** Operario.

**Ruta o menú donde se encuentra:** Menú lateral > **Historial** (ruta */operator/service-history*).

**Pasos para utilizarlo:**

1. Hacer clic en **Historial**.
2. Revisar los indicadores, incluida la **Tasa de servicios completados**.
3. Usar las pestañas **Todos**, **Finalizados**, **Cancelados** y **Reasignados** y el filtro **Todos los servicios**.
4. Usar el cuadro de búsqueda para encontrar un servicio por código, placa, cliente o vehículo.
5. Hacer clic en **Limpiar** para quitar los filtros.
6. Hacer clic en un servicio para ver su detalle. Si el cliente lo calificó, el botón **Ir a calificaciones** lleva a **Calificaciones recibidas** (sección 10.2.6).

**Resultado esperado:** El operario consulta el trabajo realizado, del más reciente al más antiguo, y el estado final de cada servicio.

**Observaciones o restricciones:** Un servicio reasignado es uno que el administrador pasó a otro operario; deja de contar como servicio propio del operario.

**Figura 30**

*Historial de Servicios del Operario*

![Historial de Servicios del Operario](capturas/usuario-30-historial-de-servicios-del-operario.jpg)

#### 10.2.6 Calificaciones Recibidas

**Nombre del módulo:** Calificaciones recibidas.

**Descripción:** Muestra las calificaciones y comentarios que los clientes dejaron sobre el trabajo del operario.

**Rol que puede usarlo:** Operario.

**Ruta o menú donde se encuentra:** Menú lateral > **Calificaciones** (ruta */operator/qualifications*).

**Pasos para utilizarlo:**

1. Hacer clic en **Calificaciones**.
2. Revisar la calificación promedio y el total de calificaciones recibidas.
3. Usar **Filtrar por fecha**, **Filtrar por tipo de servicio** (lavado básico, premium o completo) y el número de estrellas, y hacer clic en **Filtrar**.
4. Leer cada calificación con el cliente, el servicio, la fecha y el comentario.

**Resultado esperado:** El operario conoce la opinión de los clientes.

**Observaciones o restricciones:** Solo aparecen las calificaciones que los clientes decidieron dejar, porque calificar es opcional. Si no hay ninguna, el sistema muestra "No se encontraron calificaciones".

**Figura 31**

*Calificaciones Recibidas por el Operario*

![Calificaciones Recibidas por el Operario](capturas/usuario-31-calificaciones-recibidas-por-el-operario.jpg)

#### 10.2.7 Perfil y Configuración del Operario

El operario consulta y edita sus datos personales y cambia la contraseña en **Perfil**, siguiendo los pasos de la sección 10.1.8. El tema, el idioma y el centro de ayuda están disponibles en **Configuración** (ruta */operator/settings*), como se explica en la sección 10.1.9. Si el administrador le entregó una contraseña temporal, debe cambiarla en el primer ingreso.

## 11. Mensajes y Validaciones

El sistema valida la información mientras la persona escribe. Cuando un dato no es correcto, resalta el campo con un borde rojo y muestra un mensaje debajo. Las Tablas 11 y 12 explican el significado de los mensajes más frecuentes y lo que debe hacer la persona.

**Tabla 11**

*Mensajes de los Formularios de Registro, Ingreso y Recuperación*

| Mensaje del sistema | Significado | Acción del usuario |
|---|---|---|
| El correo es obligatorio | El campo de correo está vacío. | Escribir el correo. |
| Debe ingresar un correo válido @gmail.com | El correo no tiene un formato válido o no termina en @gmail.com. | Corregir el correo. |
| Solo se permiten correos @gmail.com | En el registro se escribió un correo de otro proveedor. | Usar una cuenta de Gmail. |
| El documento es obligatorio / Debe tener entre 5 y 20 dígitos | El número de documento está vacío o tiene una longitud no válida. | Escribir el documento solo con dígitos. |
| El nombre es obligatorio / Debe tener mínimo 3 caracteres | Los nombres están vacíos o son demasiado cortos. | Escribir los nombres. |
| Los apellidos son obligatorios / Debe tener mínimo 2 caracteres | Los apellidos están vacíos o son demasiado cortos. | Escribir los apellidos. |
| El teléfono es obligatorio | El campo de teléfono está vacío. | Escribir el número celular. |
| Debe comenzar con 3 (número celular colombiano) | El número no empieza por 3. | Escribir un número celular colombiano. |
| El número debe tener 10 dígitos | El teléfono tiene menos de 10 dígitos. | Completar los 10 dígitos. |
| Las contraseñas no coinciden | La confirmación es diferente de la contraseña. | Escribir la misma contraseña en ambos campos. |
| La contraseña no cumple los requisitos de seguridad | Falta uno de los cuatro requisitos. | Seguir la lista de requisitos. |
| Debes aceptar los Términos y la Política de Datos para continuar | No se aceptó uno de los dos documentos legales. | Leer y aceptar ambos documentos. |
| Ya existe una cuenta con este correo | El correo ya está registrado. | Iniciar sesión o recuperar la contraseña. |
| Ya existe una cuenta con este número de documento | El número de documento ya está registrado. | Verificar los datos o contactar al lavadero. |
| Correo o contraseña incorrectos | Las credenciales no coinciden con ninguna cuenta. | Revisar los datos e intentar de nuevo, o recuperar la contraseña. |
| Tu cuenta está desactivada. Contacta al administrador. | La cuenta fue desactivada. | Pedir al administrador que la reactive. |
| El código es incorrecto, ya se usó o expiró. Solicita uno nuevo. | El código de recuperación no es válido. | Solicitar un código nuevo. |
| ¡Contraseña actualizada! | La contraseña se cambió correctamente. | Ingresar con la nueva contraseña. |

*Nota.* Textos tomados del archivo de traducción al español de la aplicación web.

**Tabla 12**

*Mensajes de Operación del Sistema*

| Mensaje o situación | Significado | Acción del usuario |
|---|---|---|
| Tu sesión expiró. Inicia sesión de nuevo. | Terminó la sesión de una hora. | Iniciar sesión de nuevo. |
| No tienes permiso para realizar esta acción | La acción pertenece a otro rol o a datos de otra persona. | Usar solo las opciones del rol. |
| Tu perfil de cliente aún no está listo. Intenta de nuevo en unos minutos. | El perfil de cliente se está creando después del registro. | Esperar un momento e intentar de nuevo. |
| Ya existe un vehículo registrado con esta placa | La placa pertenece a un vehículo activo. | Verificar la placa. |
| El formato de la placa no corresponde al tipo de vehículo | La placa no sigue el formato oficial del tipo elegido. | Corregir la placa o el tipo. |
| Esa hora ya se ocupó | El turno se tomó mientras se reservaba. | Elegir una de las horas sugeridas. |
| El lavadero no abre ese día. Elige otra fecha. | El día elegido está marcado como cerrado. | Elegir otra fecha. |
| A esa hora el servicio no cabe en el horario de atención. Elige otra hora. | El servicio terminaría después del cierre o cruza el descanso. | Elegir otra de las horas libres. |
| Esa hora ya pasó. Elige una hora más tarde. | La hora elegida ya pasó. | Elegir una hora más tarde. |
| Demasiados intentos fallidos. Tu cuenta quedó bloqueada 15 minutos... | Se escribió mal la contraseña cinco veces en menos de 15 minutos. | Esperar 15 minutos o usar ¿Olvidaste tu contraseña?. |
| Ese vehículo ya tiene una reserva a esa hora. | El vehículo ya está reservado en ese turno. | Elegir otra hora. |
| La fecha no es válida para reservar. | La fecha ya pasó o está fuera de la ventana de reservas. | Elegir una fecha válida. |
| Esta reserva ya no se puede cambiar. | La reserva ya empezó o se cerró. | Contactar al lavadero. |
| Archivo no válido | El comprobante no es una imagen JPG o PNG de hasta 10 MB. | Adjuntar una imagen válida. |
| Para confirmar el pago te falta: ... | Faltan datos del pago (comprobante, referencia o monto). | Completar los elementos listados bajo el botón. |
| Ese cupón no existe. | El código del cupón es incorrecto. | Revisar el código que aparece en el aviso del cupón. |
| Ese cupón no está vigente o todavía no acumulas los puntos necesarios. | El cupón está pausado, fuera de sus fechas o bloqueado. | Revisar los puntos en el panel. |
| Ya canjeaste este cupón en esta reserva. | El cupón ya se usó en esa reserva. | Pagar sin el cupón o usar otro. |
| Solo puedes calificar un servicio finalizado. / Este servicio ya fue calificado. | La calificación no está permitida. | Esperar a que el servicio termine; una reserva se califica una sola vez. |
| Primero debes iniciar el servicio. / Este servicio ya fue iniciado. | El operario intentó una acción fuera de orden. | Iniciar el servicio antes de finalizarlo. |
| No hay conexión con el servidor. Intenta de nuevo en un momento. | No hay conexión con el sistema. | Revisar la conexión a internet e intentar de nuevo. |

*Nota.* Textos tomados del archivo de traducción al español de la aplicación web.

## 12. Cierre de Sesión

Cerrar la sesión al terminar evita que otra persona use la cuenta, especialmente en computadores o teléfonos compartidos. Aunque la sesión vence automáticamente una hora después del ingreso, se recomienda cerrarla manualmente.

1. Ubicar la opción **Cerrar Sesión** en la parte inferior del menú lateral.
2. Hacer clic en **Cerrar Sesión**.
3. En la ventana "Cerrar sesión", hacer clic en **Sí, cerrar**.
4. Verificar que el sistema vuelva a la pantalla de inicio de sesión.

**Figura 32**

*Confirmación del Cierre de Sesión*

![Confirmación del Cierre de Sesión](capturas/usuario-32-confirmacion-del-cierre-de-sesion.jpg)

## 13. Preguntas Frecuentes

##### ¿Qué hago si olvidé mi contraseña?

En la pantalla de inicio de sesión, hacer clic en "¿Olvidaste tu contraseña?" y seguir los tres pasos de la sección 8.3. El código llega al correo registrado y es válido durante 15 minutos.

##### ¿Por qué el sistema no me deja registrarme?

El sistema solo acepta correos terminados en @gmail.com, y cada correo y cada número de documento pueden tener una sola cuenta. Además, se deben aceptar los dos documentos legales.

##### ¿Mi cuenta se puede bloquear por escribir mal la contraseña?

Sí. Después de cinco intentos fallidos en menos de 15 minutos, la cuenta queda bloqueada durante 15 minutos. Puede esperar ese tiempo o usar **¿Olvidaste tu contraseña?** para crear una contraseña nueva y entrar de inmediato.

##### ¿Cómo sé si mi reserva quedó confirmada?

Cuando la hora está libre, la reserva se confirma de inmediato: el sistema muestra "¡Reserva creada!", la reserva aparece en el panel y en el Historial con el estado Confirmada, y llega la confirmación por correo.

##### ¿Qué hago si la hora que quiero ya está ocupada?

La pantalla solo ofrece horas libres. Si otra persona toma la hora mientras usted reserva, el sistema sugiere las horas libres más cercanas del mismo día; elija una y confirme.

##### ¿Puedo elegir quién lava mi vehículo?

Sí, es opcional. Al reservar, en **Operario (opcional)** aparecen los operarios libres a esa hora. Si no elige ninguno, el sistema asigna uno libre automáticamente. Puede ver el operario asignado en el panel y recibe una notificación cuando se asigna o cambia.

##### ¿Cómo cambio la fecha de una reserva?

La aplicación web no permite cambiar la fecha ni la hora. Cancele la reserva antes de su hora de inicio y reserve de nuevo, o contacte al lavadero.

##### ¿Cómo pago mi servicio?

En Pagar servicio, elija el método. Con Nequi, Daviplata o Transferencia, escanee el código QR, transfiera el monto exacto y adjunte el comprobante con la referencia de la transacción; con Efectivo, pague en el lavadero.

##### ¿El sistema guarda los datos de mi tarjeta?

No. El sistema no solicita ni guarda datos de tarjetas.

##### ¿Por qué mi pago aparece "En revisión"?

Porque un administrador debe verificar que el dinero llegó a la cuenta del lavadero. Cuando lo apruebe o lo rechace, usted recibirá una notificación y un correo; también puede consultar el estado en el Historial.

##### ¿Puedo usar un código de promoción?

Sí. Cuando sus puntos desbloquean un cupón, usted recibe un aviso con su código. En Pagar servicio, escríbalo en Código del cupón y haga clic en Aplicar antes de confirmar el pago.

##### ¿Cómo gano puntos de fidelización?

Cada servicio suma los puntos que aparecen al reservar ("Suma N puntos"). Los puntos se acreditan cuando el administrador aprueba el pago de la reserva, y su progreso se ve en el panel. Los puntos no se gastan: desbloquean cupones.

##### ¿Cómo califico un servicio?

Cuando la reserva esté Completada, abra el Historial, haga clic en "Calificar Servicio", elija de una a cinco estrellas y, si lo desea, escriba un comentario. Cada reserva se puede calificar una sola vez.

##### ¿Puedo cambiar el idioma o los colores?

Sí. En Configuración puede elegir español, inglés, francés o portugués y uno de cuatro temas de color; la elección se guarda en su cuenta.

##### ¿Puedo eliminar o desactivar mi cuenta?

La opción **Desactivar mi cuenta** desactiva la cuenta, no la borra: no podrá ingresar, pero su historial se conserva. Para reactivarla, contacte al administrador. Las cuentas de administrador no tienen esta opción.

##### Soy operario y no puedo iniciar un servicio. ¿Por qué?

Un servicio solo se puede iniciar el día de la reserva, solo si está asignado a usted y solo cuando no tiene otro servicio en curso. Si el servicio es suyo y el problema continúa, informe al administrador.

## 14. Glosario

**Tabla 13**

*Glosario de Términos del Sistema*

| Término | Definición |
|---|---|
| Administrador | Rol que gestiona reservas, operarios, pagos, horarios, usuarios, promociones y reportes. |
| Asignación | Vínculo entre un operario y una reserva, hecho por el administrador. |
| Bahía (de lavado) | Puesto físico del lavadero donde se lava un vehículo. Dos reservas no pueden ocupar la misma bahía al mismo tiempo. |
| Calificación | Puntuación de una a cinco estrellas, con un comentario opcional, que el cliente da a un servicio completado. |
| Cliente | Persona que registra vehículos y reserva turnos. |
| Código QR | Código bidimensional que se escanea con el teléfono para pagar. |
| Comprobante | Imagen que demuestra que se hizo una transferencia. |
| Cupón | Código de descuento que el cliente desbloquea al acumular puntos de fidelización y canjea al pagar. |
| Dashboard (panel) | Pantalla de inicio que resume la información más importante de cada rol. |
| Notificación | Aviso dentro del sistema sobre un hecho relevante. |
| Operario | Empleado que lava los vehículos. |
| Puntos de fidelización | Puntos que suma cada servicio cuando se aprueba su pago; desbloquean cupones y no se gastan. |
| Recordatorio | Aviso que el sistema envía 24 horas y 1 hora antes de una reserva. |
| Referencia de la transacción | Número que el banco imprime en el comprobante para identificar la transferencia. |
| Reserva | Bloque de tiempo apartado para lavar un vehículo. |
| Servicio de lavado | Tipo de lavado ofrecido (Básico, Premium o Completo), con su propia duración, precio y puntos. |
| Tema | Combinación de colores de la interfaz que cada persona puede elegir. |

*Nota.* Basado en el glosario de la documentación del proyecto.

## Referencias

Congreso de la República de Colombia. (2012). *Ley Estatutaria 1581 de 2012, por la cual se dictan disposiciones generales para la protección de datos personales*. http://www.secretariasenado.gov.co/senado/basedoc/ley_1581_2012.html

Equipo de Desarrollo Vehicle Washing. (2026a). *Vehicle washing management system: Project documentation* (vehicle-w-docs) [Documentación de proyecto no publicada]. GitHub. https://github.com/code-sena/vehicle-w-docs

Equipo de Desarrollo Vehicle Washing. (2026b). *Front-end-proyecto-web* (rama develop) [Software]. GitHub. https://github.com/BrayanCABRERA123/Front-end-proyecto-web

Servicio Nacional de Aprendizaje. (2026). *Guía para elaborar manuales de software: Manual de usuario, manual técnico, manual de instalación y manual de administrador* [Material de formación no publicado]. Programa Tecnólogo en Análisis y Desarrollo de Software.

## 15. Anexos

### Anexo A. Origen de las Capturas

Las figuras de este manual se tomaron el 16 de octubre de 2026 sobre la versión de la rama *develop*, con el sistema completo corriendo en Docker y la web en *http://localhost:4200*. Se usaron cuentas, vehículos, reservas y pagos de prueba creados solo para las capturas, por lo que no aparecen correos, documentos, teléfonos, placas ni cuentas bancarias reales. Si una pantalla cambia en una versión futura, la captura correspondiente se debe tomar de nuevo con el mismo nombre de archivo de la carpeta *capturas*.

### Anexo B. Lista de Verificación para la Entrega

**Tabla 14**

*Lista de Verificación del Manual de Usuario*

| Criterio | Cumple |
|---|---|
| Tiene portada completa (ficha, instructora y centro de formación) y versión | Sí / No |
| Incluye tabla de contenido con páginas actualizadas | Sí / No |
| Explica el objetivo y el alcance | Sí / No |
| El contenido coincide con el software de la versión final | Sí / No |
| Todas las figuras son capturas reales de la versión final | Sí / No |
| Los pasos son claros y ordenados | Sí / No |
| No contiene información sensible ni credenciales reales | Sí / No |
| Ortografía y formato APA revisados | Sí / No |
| Exportado a PDF con el nombre Manual_usuario_LavadoVehicular_3145556.pdf | Sí / No |

*Nota.* Adaptado de la lista de verificación de la guía para elaborar manuales de software (SENA, 2026).
