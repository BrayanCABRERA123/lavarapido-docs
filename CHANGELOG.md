# Historial de cambios de la documentación / Documentation Changelog

Registro de los cambios de este repositorio de evidencias, del más reciente al más antiguo. Cada documento tiene además su propia tabla de control de versiones. Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).

*Changes to this evidence repository, newest first. Each document also has its own version control table. Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).*

## 2026-10-21 — Código del 21 de octubre, servidor con respaldos y pruebas del día

**Contenido** (español e inglés)

- Código del 21 de octubre: el token de una sesión cerrada deja de servir (security-service y API Gateway); las reservas que nadie inicia se cierran solas una hora después de su hora de fin (motivo `EXPIRED`); la asignación manual y la automática usan el mismo candado y hay un solo conteo de reservas sin operario; el comprobante pesa como máximo 2 MB; Efectivo solo aparece con su cuenta activa; la sesión de la web se sincroniza entre pestañas; los reportes cuentan solo reservas completadas; la pestaña de roles dice que el acceso lo decide el rol; la app exige instalar el APK nuevo cuando se publica. Se documentó en 01 SRS 7.7, 02 Análisis 2.4, 04 Diseño 1.5, 05 Artefactos, 09 Manuales (técnico 4.5, instalación 4.4, usuario 4.5 y administrador 4.5) y 10 Artículos.
- Servidor (20 y 21 de octubre): respaldos diarios y antes de cada actualización, verificados con una restauración de prueba; modelo de recuperación SIMPLE; encabezados de seguridad y CSP en Caddy; chequeos de salud y registros limitados en todos los contenedores; se descartó el VPS de Hostinger. Se documentó en 03 Propuesta 1.4, 07 Despliegue 1.5 (con la actualización del 21 de octubre y los cambios del código que faltan por desplegar), 07 Procedimiento 2.4 y los manuales de instalación y de administrador.
- 06 Pruebas: ejecución del 21 de octubre con 689 pruebas automatizadas y 19 de punta a punta, inventario de 584 métodos de prueba, trazabilidad y brechas.
- 08 Acciones 2.5: correctivas AC-44 a AC-52 cerradas y ACO-14 abierta (variables nuevas que no están en `.env.example` ni en el compose); preventivas AP-04 y AP-16 a AP-18 cerradas; mejora AM-16. Las mejoras del 17 de octubre que repetían los identificadores AM-07 y AM-08 pasan a ser AM-14 y AM-15.
- Correcciones encontradas en la revisión: rutas que faltaban en la tabla del gateway y numeración de los changelogs (manual técnico), fecha y versión de la portada de los manuales de usuario y de administrador, 24 tipos de notificación y líneas de código citadas (diseño), y referencias de los artículos con las versiones vigentes de los documentos.
- 11 Evidencias: estado del servidor y pruebas del 21 de octubre.
- PDF y Word: pendientes de regenerar con el generador del equipo; esta entrada solo cambia los Markdown.

## 2026-10-20 — Revisión completa contra el código y diagramas sin cruces

**Contenido** (español e inglés)

- Se quitó el cambio de rol de una cuenta, que se retiró del backend, la web y la app: el rol se elige al crear la cuenta. Ajustes en 01 SRS 7.6 (RF-028, CU27), 06 Pruebas (CP-42), 09 Manuales técnico 4.4 y de administrador 4.4 y en los diagramas de 02 y 04.
- El cliente solo cancela, con una confirmación y sin motivo; la reprogramación la hace el administrador (RF-007, CU07, CU29, actividades y estados).
- 01 SRS 7.6: tipos de notificación, eventos que se publican y los que solo quedan en la bitácora, estados reales de la ejecución y despliegue en Azure.
- 02 Análisis 2.3 y 04 Diseño 1.4: secuencias, estados y modelo de datos corregidos contra el código; las figuras de servicios y puertos muestran las clases ordenadas y las dependencias en una lista.
- 03 Propuesta 1.3, 05 Artefactos, 07 Procedimiento 2.3 y Despliegue 1.4, 08 Acciones 2.4, 09 Manual de instalación 4.3 y de usuario 4.4, 10 Artículos y 11 Evidencias: cifras, fechas y textos al día.
- Diagramas: todos se dibujan con líneas rectas y codos de 90°; donde dos líneas no pueden dejar de cruzarse llevan un puente. Los casos de uso tienen la figura del actor y los óvalos alineados, y las actividades usan los símbolos UML de inicio y fin. La arquitectura y los estados de la reserva del manual técnico y de los artículos dejaron de ser imágenes SVG y pasaron a diagramas que se mantienen con el resto.
- Segunda revisión visual de los 116 diagramas de los documentos, uno por uno: ya no queda ningún cruce de líneas; los diagramas de actividades del 02 tienen un solo inicio y fines que no continúan; los mensajes largos de las secuencias van en dos líneas; las figuras 14, 16, 22, 25, 27 y 30 del 04 se reorganizaron (la 27 quedó en dos partes: pagos, y promociones y fidelización).
- Capturas de la lista de usuarios tomadas de nuevo el 20 de octubre (01, 02, 04 y manual de administrador).
- PDF y Word regenerados para todos los documentos.

## 2026-10-19 — Despliegue, integración continua, casos de uso y pruebas del día

**Contenido** (español e inglés)

- 07 Documento de despliegue 1.3: actualización del servidor del 19 de octubre (migración 039, APK 1.1.0), acceso de cada integrante con su propia llave SSH, despliegue desde GitHub Actions y evidencias nuevas del servidor.
- Integración continua con GitHub Actions en los 10 repositorios: SRS, procedimiento de implementación 2.2, acciones 2.2 (AP-01 cerrada), manuales de instalación y técnico 4.2 y artículos.
- 01 SRS 7.3 a 7.5: cambio de rol de una cuenta y reglas de las cuentas de administrador (RF-027, RF-028, CU27); nuevos casos de uso CU31 (cuenta propia) y CU32 (procesos automáticos), con lo que pasan a ser 32; pruebas del 19 de octubre.
- 02 Análisis 2.2: CU31 y CU32, secuencia de recuperación de la contraseña y estados de la cuenta de usuario.
- 06 Pruebas: ejecución del 19 de octubre con 655 pruebas automatizadas (incluidas las 7 de persistencia de payment-service), 19 de punta a punta, 42 casos funcionales (CP-34 a CP-42 nuevos), rendimiento (RNF-001) y diseño adaptable en 66 pantallas web y 15 de la app, con siete figuras de evidencia. Se corrigió el conteo de customer-service: son 69 pruebas, no 68.
- 09 Manuales: cambio de tipo de usuario desde la tabla de usuarios y datos del negocio por completar (administrador 4.2 y 4.3); todas las capturas de los manuales de usuario y de administrador tomadas de nuevo (4.3).
- 01, 02 y 04: capturas del sistema tomadas de nuevo con datos de demostración (las anteriores mostraban la marca vieja y correos reales).
- PDF y Word regenerados para todos los documentos que cambiaron.

## 2026-10-17 — Actualización contra el código del 17 de octubre

**Organización**

- Nuevo índice general bilingüe ([README.md](README.md)) con versión, fecha y enlaces a MD, PDF y Word de cada evidencia, la estructura de carpetas, las convenciones de nombres y la guía de git del equipo.
- Nuevo historial de cambios (este archivo).
- La matriz de enlaces (11) se separó en `ES/` y `EN/` y tiene versión en inglés (`Evidence_Links_Project_VehicleWashing.md`).

**Contenido** (español e inglés)

- 01 SRS 7.1: RF-036 (informe de inspección) también desde la aplicación móvil; RNF-008 con la verificación de 60 pantallas web y 26 de la app.
- 02 Análisis 2.1: consentimiento de los documentos legales en el registro (2.1) e inspección desde la app móvil (2.9).
- 03 Propuesta técnica 1.2: seguimiento del despliegue real en Azure y bibliotecas de fotos de la app.
- 04 Diseño 1.2: 35 pantallas web (página no encontrada) y 31 de la app (inspección); nueva sección 2.5 de diseño adaptable.
- 05 Artefactos de código: commits, archivos y líneas al 17 de octubre; `eas.json` y scripts de publicación del APK; endpoints de salud de payment-service.
- 06 Pruebas: sección 3.2 con la verificación de diseño adaptable y del informe de inspección móvil; defectos 7 a 10 de la Tabla 9.
- 07 Procedimiento de implementación 2.1: la nueva versión de la app exige un APK nuevo.
- 08 Acciones 2.1: correctivas AC-40 a AC-43, preventiva AP-15 y mejoras AM-07 y AM-08.
- 09 Manuales 4.1: inspección desde la app (administrador), página de inicio con preguntas frecuentes y uso en celular (usuario), módulo de inspección móvil y cliente HTTP (técnico), `EXPO_PUBLIC_WEB_URL` y dependencias nativas nuevas (instalación).
- PDF (formato APA 7) y Word regenerados para todos los documentos que cambiaron.

## 2026-10-16 — Revisión con el sistema en ejecución y despliegue en Azure

- Documento de despliegue en Azure (07) en español e inglés, con capturas de evidencia, en MD, PDF y Word.
- Manuales 4.0 con capturas reales del sistema funcionando.
- SRS 7.0, pruebas del 16 de octubre (639 automatizadas y 19 de punta a punta), acciones 2.0, procedimiento 2.0 y artículos actualizados.
- Matriz de enlaces con la aplicación desplegada, pruebas de humo, chequeos de salud y revisión de seguridad.

## 2026-10-15 — Estructura de carpetas por evidencia

- Estructura `NN_EVIDENCIA/ES|EN/MD|PDF|WORD` para las evidencias 01 a 11.
- Se agregaron los manuales, el artículo (APA 7, IEEE y ACM), el procedimiento de implementación y las acciones correctivas.
- PDF en formato APA 7 y Word para todos los documentos.
- Matriz de enlaces de evidencias (11) con enlaces públicos y a `vehicle-w-docs`.

## 2026-10-09 a 2026-10-13 — Primeras evidencias

- Informe de especificación de requisitos, análisis de vistas dinámicas, propuesta técnica, diseño, artefactos de código y documentación de pruebas.
