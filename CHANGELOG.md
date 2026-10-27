# Historial de cambios de la documentación / Documentation Changelog

Registro de los cambios de este repositorio de evidencias, del más reciente al más antiguo. Cada documento tiene además su propia tabla de control de versiones. Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).

*Changes to this evidence repository, newest first. Each document also has its own version control table. Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).*

## 2026-10-27 (noche) — Capturas de la aplicación móvil

- 09 Usuario del cliente 1.3: Figuras 26 a 32 de la app (ingreso, inicio, reservar con la forma de pago, pago con plazo, historial y menú Más); el cierre de sesión pasa a ser la Figura 33.
- 09 Usuario del operario 1.2: Figuras 15 a 18 de la app (inicio, agenda en vista Semana, servicios asignados y menú Más); el cierre de sesión pasa a ser la Figura 19.
- 09 Usuario 4.13: la sección 10.3 ya no dice que la app no tiene capturas y remite a los manuales por rol.
- Las capturas (11 por idioma) se tomaron el 27 de octubre con el código de la app (*develop*, 1.1.1) en el modo web de Expo, con tamaño y densidad de celular (393 × 852, densidad 2,5), contra el sistema local con cuentas de prueba; el Anexo A de cada manual lo explica.
- 11 Enlaces: conteo de capturas. PDF y Word de los manuales regenerados.

## 2026-10-27 (noche) — Generador de PDF y Word en el repositorio

- `_generador/`: el generador con el que se regeneraron todas las evidencias el 27 de octubre (`generar.py`, `generador_apa.py`, `apa.css` y las plantillas de estilos del Word), con sus instrucciones en `LEEME.md`. Lee las rutas del índice del README, convierte los diagramas Mermaid en imagen, muestra las imágenes dentro de tablas, conserva la tabla de la portada y no parte ninguna figura entre páginas.
- README: cómo regenerar el PDF y el Word.

## 2026-10-27 (tarde) — PDF y Word de todas las evidencias regenerados

**Contenido** (español e inglés).

- 08 Acciones 3.2 y 06 Pruebas: conteo del 27 de octubre (booking 137, customer-service 83: 1 311 con el mismo criterio) y pruebas de persistencia de payment en el CI.
- **PDF y Word de 01 a 09 y PDF de 11 regenerados** desde el Markdown actual (el artículo, 10, no cambió). Ya no quedan PDF ni Word desactualizados.
- Formato: el mismo generador APA de los manuales, con cuatro ajustes: los diagramas Mermaid se convierten en imagen; las capturas dentro de tablas (01 y 02) se muestran como imagen; la tabla de la portada de 11 se conserva; y ninguna imagen se parte entre páginas (las muy altas se reducen para que el título, la imagen y la nota queden en la misma página). 03 se regeneró solo por este último ajuste.

## 2026-10-27 — Cambios de booking, customer, payment e infra de la madrugada

**Contenido** (español e inglés). Verificado contra `develop` del 27 de octubre de 2026 (booking `c648730`, customer `c9ac51c`, payment `6cb806f`, infra `f9a44d0`) y en el entorno local con booking y customer reconstruidos.

- 09 Usuario del cliente 1.2: las horas alternativas de "Esa hora ya se ocupó" ya no incluyen las que se cruzan con otra reserva del mismo vehículo (10.3 y 13); Figura 16 nueva (ES y EN) tomada el 27 de octubre con el aviso, y las figuras siguientes renumeradas (17 a 26).
- 09 Usuario 4.12, Administrador 4.12 (máximo 10 servicios por reserva y alternativas) y Técnico 4.12 (`AvailabilityPolicy.withoutBusyTimes`, máximo 10 `serviceIds` sin nulos, 400 `VALIDATION_ERROR` en la semana del horario, `bookedBy` solo para el personal, consulta única de dueños en customer, job "Pruebas de integración" de payment y conteos: booking 137, customer 83).
- 06 Pruebas: pruebas de persistencia de payment en el CI y conteos del 27 de octubre.
- **PDF y Word regenerados** de los manuales técnico, de usuario, de usuario del cliente y de administrador. Siguen pendientes los de 01 a 08 y el PDF de 11.

## 2026-10-26 (cierre) — Despliegue continuo activo, APK 1.1.1, términos y Política de Datos, SonarCloud

**Contenido** (español e inglés). Verificado en GitHub Actions (`lavarapido-infra`, `deploy.yml`; `LavadoVehicular-Movil`, `cd.yml`), en `/app/version.json` del servidor público y en los archivos de traducción de la web.

- 07 Despliegue 1.11: subsección 1.3.12 (versiones `v1.1.0` y `v1.1.1`; payment-service desde `main`; primera corrida automática del despliegue continuo a las 22:19, hora de Colombia, y pedidos hasta las 22:48, todos en verde; publicación de `v1.1.0` del móvil fallida por falta de `EXPO_TOKEN` y APK `versionCode` 6 con la OTA publicada tras comparar la huella nativa; arreglos de SonarCloud); 4.3.4 "activo desde el 26-10-2026". 07 Procedimiento 2.9 (R-I04).
- 08 Acciones 3.1: ACO-19 cerrada como AC-90; ACO-24 queda solo con la protección de `develop`; Tabla 10: 90 de 106 (85 %), 16 abiertas; AM-17 implementada; H-15 corregido; Anexo C.
- 09 Técnico 4.11 (despliegue continuo comprobado y SonarCloud), Administrador 4.11, Usuario 4.11, Usuario del cliente 1.1 (Política de Datos con las fotografías de la inspección: apartados 4, 5 y 12; app 1.1.1, `versionCode` 6) y Usuario del operario 1.1 (app 1.1.1).
- 01 SRS 8.2 (RNF-002), 04 Diseño 1.10 y 05 Artefactos: despliegue continuo activo y servidor en `main`.
- 11 Enlaces: fila "Despliegue continuo".
- **PDF y Word regenerados** de los seis manuales. Siguen pendientes los de 01, 02, 04, 05, 06, 07 y 08 y el PDF de 11, que el equipo genera con otra variante del generador.

## 2026-10-26 (noche) — Manuales de usuario por rol (cliente y operario) y versiones v1.1.0 y v1.1.1

**Contenido** (español e inglés). Verificado contra `develop` del 26 de octubre de 2026 (web `dcfd2e2`, móvil `b921582`, infra `14cc594`) y las etiquetas `v1.1.0` (10 repositorios) y `v1.1.1` (web, móvil, payment-service e infra) de ese día.

- 09 **Manual de usuario del cliente 1.0** (nuevo): `manual-de-usuario-cliente.md` / `customer-user-manual.md`, con la plantilla mínima del manual de usuario de la guía del SENA y el formato de cada módulo (nombre, descripción, rol, ruta, pasos, captura, resultado y observaciones). Incluye el pago al reservar, las pantallas de pago digital (con plazo) y en efectivo (botón **Confirmar reserva**), las insignias del historial, el reporte de inspección público (`/report/:token`) que no estaba documentado, los términos y condiciones con el apartado 8 (informe de inspección y fotografías) y la app móvil 1.1.0. 25 figuras.
- 09 **Manual de usuario del operario 1.0** (nuevo): `manual-de-usuario-operario.md` / `operator-user-manual.md`, con permisos y responsabilidades del operario, primer ingreso con la contraseña temporal, forma de pago visible en el servicio y los interruptores de notificación y **Desactivar mi cuenta**, que el operario tiene en la web y no estaban documentados. 15 figuras.
- Capturas nuevas en español y en inglés (26 de octubre, sistema completo en Docker con datos de prueba): reserva con el paso "¿Cómo vas a pagar?", confirmación en efectivo, pago digital con plazo, pago en efectivo, QR y comprobante, historial con insignias, perfil y configuración del operario. Las demás figuras de los dos manuales nuevos son las capturas vigentes del manual de usuario, copiadas con nombres `cliente-*` / `customer-*` y `operario-*` / `operator-*`.
- 09 Usuario 4.10 (se conserva como referencia conjunta; perfil y configuración del operario corregidos; app 1.1.0 publicada), Técnico 4.10, Instalación 4.9 y Administrador 4.10: versiones `v1.1.0` y `v1.1.1` del 26 de octubre; payment-service se despliega desde `main` desde infra `v1.1.1`.
- README: índice con los dos manuales nuevos, versiones de los manuales y tabla de repositorios con las versiones del 26 de octubre.
- **PDF y Word regenerados** de los seis manuales (técnico, instalación, usuario, usuario del cliente, usuario del operario y administrador) en los dos idiomas.

## 2026-10-26 — Pago al reservar: modo de pago, efectivo con límite y vencimiento del pago digital

**Contenido** (español e inglés). Mitigación de reservas masivas, a partir de la pregunta de la preparación de la sustentación (¿qué impide que un bot o una persona bloquee la agenda?) y de la recomendación del instructor. Verificado contra `develop` del 26 de octubre de 2026: booking `db156cb`, payment `d94cde5`, web `7f8aca5`, móvil `acf4e6d` e infra `0f949e5`. Desplegado en Azure ese día hacia las 12:02 (hora de Colombia): booking-service, payment-service y la web.

- 01 SRS 8.1: RF-005 con `paymentMode` (400 `INVALID_PAYMENT_MODE`), el límite de efectivo (409 `CASH_BOOKING_LIMIT`) y el plazo del pago digital (`PAYMENT_TIMEOUT`); RF-013 y RF-033; reglas RN-BOOK-02 a RN-BOOK-04; RNF-004 con la mitigación de reservas masivas y RNF-009 con el paso de la forma de pago.
- 02 Análisis 2.7: secuencias 2.2 y 2.5 con el modo de pago y `payment.reported`; secuencia nueva 2.11 (vencimiento del pago digital, con la consulta a payment antes de cancelar); actividad 3.2 y estados 4.1.
- 04 Diseño 1.9: llamada interna booking → payment (Tabla 6); `payment.reported` y `payment.confirmed` consumidos por booking en `booking.payment-events` (Tabla 7); `PaymentDeadlineJob`; columnas de la migración 049 y motivo de la semilla 117 en el diccionario; adaptadores y puertos nuevos; transición por pago vencido.
- 06 Pruebas: sección 3.4 con la prueba en vivo del 26 de octubre en local (Tabla 5e, con las dos fallas simuladas) y en producción; conteos nuevos (Tabla 5f: booking 133, payment 247 sin las de integración, web 239 y móvil 100); defecto 13 y brechas 9 y 10.
- 07 Despliegue 1.10: subsección 1.3.11 con el despliegue del 26 de octubre y sus verificaciones; variables nuevas de booking e `INTERNAL_API_KEY` obligatoria en payment (3.3.2). 07 Procedimiento 2.8: Tabla 6 con las mismas variables.
- 08 Acciones 3.0: AC-88 (preventiva y de mejora: mitigación de reservas masivas) y AC-89 (el evento perdido canceló una reserva pagada; ahora booking le pregunta a payment antes de cancelar) cerradas; ACO-41 abierta (tolerancia por retraso en el efectivo); Tabla 10: 89 de 106 (84 %), sin P0 ni P1; lección L-20; Anexo C.
- 09 Usuario 4.9 (paso "¿Cómo vas a pagar?", plazo de 30 minutos, límite de efectivo, mensajes y pregunta frecuente), Administrador 4.9 (forma de pago en el detalle, efectivo registrado por el administrador, `PAYMENT_TIMEOUT`), Técnico 4.9 (ruta interna, cola, eventos, reglas, códigos y numeración: estructura 049 → siguiente 050, semillas 117 → siguiente 118) e Instalación 4.8 (variables, changelogs y `RABBITMQ_HOST=127.0.0.1` para payment fuera de Docker en Windows).
- La app móvil tiene el cambio en `develop`, pero todavía no llega a los celulares: sale por OTA al fusionar a `main` (*v1.1.0*).
- **PDF y Word: pendientes de regenerar** para 01, 02, 04, 06, 07 (procedimiento y despliegue), 08 y 09 (los cuatro manuales). Esta entrada solo cambia los Markdown.

## 2026-10-24 (tarde) — Migración 048 de notification-service

**Contenido** (español e inglés). Corrección encontrada al probar producción después del despliegue de las 15:10: notification-service no podía leer `notification.pending_delivery` (migración 047), porque `channel` y `language` eran VARCHAR y Hibernate (`use_nationalized_character_data: true`) las lee como NCHAR, y no envió push ni correos hasta la migración 048 (NVARCHAR; commit `612417a`, merge `3f99df4`), desplegada sola el 24 de octubre a las 17:12 UTC; las 2 entregas atascadas salieron a las 17:13.

- 08 Acciones 2.9: AC-87 cerrada (detección, causa, corrección, despliegue y verificación); Tabla 10: 87 de 103 (84 %); lección L-19 (pruebas de integración contra SQL Server, RNF-003); Anexo C con AC-87 en R-003.
- 07 Despliegue 1.9: subsección 1.3.10 con la actualización de notification de las 17:12 UTC y su resultado; última actualización (1.1.2).
- 06 Pruebas: brecha 9 con la 048 y la falla de la 047 que no vieron las pruebas unitarias.
- 04 Diseño 1.8: `pending_delivery` con `channel` y `language` NVARCHAR desde la 048.
- **PDF y Word: pendientes de regenerar** para 04, 06, 07 (despliegue) y 08. Esta entrada solo cambia los Markdown.

## 2026-10-24 — Correcciones del 24 de octubre en producción, despliegue con reversión y no conformidades cerradas

**Contenido** (español e inglés). Revisión contra `develop` del 24 de octubre de 2026 en los 10 repositorios de código (128 ramas fusionadas ese día, CI en verde) y contra el despliegue en Azure de ese día; fuentes: la auditoría de cierre del 24 de octubre, los informes por área de la flota del 23 y el 24 de octubre y el último CI de `develop`.

- Versiones: `v1.0.0` en 9 repositorios (payment-service desde el 24 de octubre, con su PR #2 fusionado y la etiqueta sobre `main` `2deac9e`); la app móvil tiene abierto el PR #1 «Release v1.1.0». `develop` va adelante en los otros 8 a la espera de `v1.1.0`.
- Despliegue del 24 de octubre (07 Despliegue 1.8, 07 Procedimiento 2.7, Administrador 4.8, Técnico 4.8, Diseño 1.7, Evidencias, README): `develop` en dos corridas por SSH (la primera con los scripts viejos; la segunda con `BRANCH=develop`), espera de salud de hasta 8 minutos, imágenes `:prev` y `rollback.sh`, `restore-db.sh` con candado y `payment-migrate`, retención de respaldos, protección que impide bajar de versión (`setup-server.sh`), web sin `root` en el puerto 8080 detrás de Caddy, 11 contenedores sanos y migraciones 044, 045, 113, 047, 116, 022 y 023 aplicadas. Despliegue continuo fusionado en `develop` (job "Pedir despliegue" en 8 repositorios y `cd.yml` con la OTA del móvil), a falta de crear `AZURE_SSH_KEY`, `DEPLOY_DISPATCH_TOKEN` y `EXPO_TOKEN`.
- Variables nuevas (07, Instalación 4.7, Administrador, Técnico, 05): `AUTH_RATE_LIMIT_*`, `TRUSTED_PROXIES`, `ROUTE_CONNECT_TIMEOUT`, `ROUTE_READ_TIMEOUT` y `START_LATE_LIMIT` (con valor por defecto y todavía fuera del compose y de `.env.example`), `INTERNAL_API_KEY` y `BOOKING_SERVICE_URL` en customer-service, y `BOOKING_EXPIRY_CHECK_*` sin efecto (se quitó la tarea, B-07).
- 08 Acciones 2.8: ACO-15 a ACO-18, ACO-20 a ACO-23, ACO-27, ACO-29, ACO-31 y ACO-32 cerradas como AC-73 a AC-84 con su repositorio y su commit de `develop`; AC-85 (protección contra bajar de versión) y AC-86 (web sin `root`); ACO-13, ACO-19, ACO-24 a ACO-26 y ACO-28 actualizadas; ACO-33 a ACO-40 abiertas con los pendientes de la revisión cruzada (la cola de pagos de la web sin paginar es la más importante). Tabla 10: 86 de 102 (84 %), ninguna P0 ni P1, así que **el criterio E6 vuelve a cumplirse**. AP-11 cerrada, AP-02 y AP-08 actualizadas, lecciones L-17 y L-18 y Anexo D (H-01 a H-25: 9 corregidos, 8 parciales, 6 abiertos, 1 aceptado y 1 que no se puede corregir).
- 01 SRS 8.0: pasan a Implementado RF-001, RF-016, RF-018, RF-024, RF-025, RF-027, RF-028 y RF-030, cada uno con su evidencia; quedan parciales RF-005, RF-015 y RF-023 (38 de 41 implementados); RF-012b con la ventana de 4 horas y las notas; RF-029 de solo lectura; RNF-002, 003, 004, 010 y 012 actualizados.
- 06 Pruebas y conteos (01 Tabla 58, 08 Tabla 10, Técnico §16.5, 07, artículos y Evidencias): último CI de `develop` del 24 de octubre con 1 192 pruebas (web 212 en 66 archivos, gateway 62, security 200, customer 82, booking 95, operations 110, notification 133, payment 225 con 11 omitidas y 73 de la app móvil en 25 suites); inventario de 1 036 métodos; batería e2e remota de 44 casos, todavía sin correr contra Azure.
- 09 Usuario 4.8: el cupón y el monto vienen del servidor y se conservan al recargar; las pantallas se actualizan solas; el operario ve las notas y puede iniciar hasta 4 horas después de la hora de fin; mensajes de error nuevos; avisos de pago de reserva cancelada y permisos de solo lectura (app del administrador); el inicio de sesión acepta cualquier dominio y el registro solo gmail.com.
- 09 Administrador 4.8: permisos de solo lectura, límite de solicitudes y tope de intentos, cambios de horario y bahías que chocan con reservas, precio mayor que 0, aviso al cambiar servicios con pago, `AMOUNT_CHANGED`, reserva cancelada, efectivo inactivo en caja, descuento fijo, `:prev` y `rollback.sh`.
- 02 Análisis 2.6 y 04 Diseño 1.7: matriz de permisos de solo lectura, sin la cancelación automática de reservas programadas; filtros nuevos del gateway, eventos `booking.status_changed` y `execution.operator_unassigned`, cola de errores de operations y entregas pendientes de notification.
- 10 Artículos (APA 7, IEEE y ACM) y 11 Evidencias: estado de los requisitos, pruebas, controles OWASP (A07 aplicado), versiones, despliegue y seguridad al 24 de octubre; tabla de repositorios con el `develop` de ese día.
- **PDF y Word: pendientes de regenerar** con el generador APA 7 del equipo para 01, 02, 04, 05, 06, 07 (procedimiento y despliegue), 08, 09 (los cuatro manuales), 10 (los tres artículos) y 11 (solo PDF), además de los de 03 Propuesta técnica, que siguen en la 1.3. Esta entrada solo cambia los Markdown.

## 2026-10-23 — Versión v1.0.0, arreglos del 23 de octubre, despliegue continuo y no conformidades reales

**Contenido** (español e inglés). Revisión contra `develop` del 23 de octubre de 2026, la versión `v1.0.0` y la revisión del sistema de ese día. Incluye y traduce al inglés el contenido de las ramas `fix/*` que Merari Urbano subió ese día a este repositorio (A-01, A-03 a A-08, A-15, B-02, C-01, D-01, E-02, E-07 y E-20), corregido donde el código ya había cambiado (por ejemplo, el botón "Desplegar en Azure" ya existe en `main` y `v1.0.0` ya existe en 8 repositorios); esas ramas quedan sustituidas por `docs/update-october-23`.

- Versiones y ramas: `v1.0.0` el 23 de octubre en 8 repositorios (web, api-gateway, security, customer, booking, operations, notification e infra); payment-service y la app móvil sin versión; `develop` otra vez adelante con los arreglos del día, que saldrán en `v1.1.0` (07 Despliegue 1.7, 09 Instalación 4.6, 09 Técnico 4.7, 11 Evidencias, README).
- Despliegue: el servidor se actualizó por última vez el 22 de octubre (semilla 112 y migraciones 040 y 041); el despliegue continuo quedó preparado en ramas locales de `lavarapido-infra` y de cinco repositorios, **sin fusionar ni probar en vivo** (07 Despliegue §4.3.4, Procedimiento, Manual de Administrador §14.6, Manual Técnico §15.4, Diseño, Evidencias, README).
- Comandos que funcionan: clonado de payment-service desde `develop`, reversión sin la etiqueta inexistente `v0.9.0` ni `update-server.sh`, respaldo sin `WITH COMPRESSION` (SQL Server Express no la admite) remitiendo a `backup-db.sh` y `verify-backup.sh`, tarea de `cron` que no depende de `DB_PASSWORD` ni pasa la contraseña con `-P`, perfil `preview` de EAS y script SQL global que no existe (07 Procedimiento 2.6, 09 Administrador 4.7, 09 Instalación 4.6).
- 08 Acciones 2.7: ACO-14 cerrada (AC-55); arreglos del 23 de octubre cerrados con su commit (AC-56 a AC-71) y documentación (AC-72); ACO-15 a ACO-32 abiertas (entre ellas SEC-01, BIZ-01, BIZ-02, OPS-01, CD-01 y las salvedades de los arreglos del día); Tabla 10 recalculada (72 de 92; dos P1 abiertas, así que el criterio E6 no se cumple); mejoras AM-17 y AM-18; Anexo D con los 25 hallazgos del instructor y su estado.
- 01 SRS 7.9: 11 RF y 9 RNF parciales, con su motivo (Tabla 57 y tablas de requisitos); RF-001 con `ALLOWED_EMAIL_DOMAINS`; RF-004 y CU04 con la revocación de sesiones; el 01 es el SRS vigente y `SRS_V4.docx` es la versión anterior V4 del 8 de octubre.
- 06 Pruebas y conteos: último CI de `develop` del 23 de octubre con 838 pruebas (web 146, gateway 39, security 171, customer 71, booking 60, operations 72, notification 115, payment 151 con 7 omitidas, y 13 de la app móvil); inventario de 735 métodos; matriz de trazabilidad con los parciales (06, 01 Tabla 58, 08 Tabla 10, 09 Técnico §16.5, artículos).
- 09 Usuario 4.7: capítulo nuevo de la app móvil Android para los tres roles (sección 10.3), hecho con las 31 pantallas de la app; regla del operario (desde 15 minutos antes, sin límite posterior) y quitar el cupón.
- 09 Técnico 4.7 y 04 Diseño 1.6: patrón MVVM de la web (36 ViewModels), capas y actualizaciones (APK obligatorio y EAS Update) de la app móvil, "una base `LavaRapido` con un esquema por servicio" en lugar de "base de datos por servicio", candado del login y chequeo de sesión con *fail-open* y SEC-01.
- "Por cerrar" de 28 días (`FOLLOW_UP_LOOK_BACK_DAYS`), cierre de sesiones al cambiar o recuperar la contraseña y candado del login, y las variables que ya pasa el compose (`FOLLOW_UP_LOOK_BACK_DAYS`, `ALLOWED_EMAIL_DOMAINS`, `DEMO_*_PASSWORD`, `INTERNAL_API_KEY` obligatoria para el operario, `ADMIN_DOCUMENT` y `ADMIN_PHONE`) en los manuales, el procedimiento, el despliegue y el diseño.
- 11 Evidencias: tabla de repositorios con su versión, `main` y `develop`; nota de seguridad corregida (quedan secretos antiguos, sin copiarlos); marcadores "[Completar]" llenados o con su responsable; lista de verificación con su estado.
- Otros: ancla rota del Manual de Administrador (10.3), nota que explica la numeración que empieza en 4 (procedimiento, 08 y los cuatro manuales), Node.js 22 en 05 Artefactos, 02 Análisis 2.5 (recuperación que revoca sesiones y *fail-open*), artículos con `v1.0.0`, Tablas 4 y 5 al día y versiones citadas, e índice de este README.
- **PDF y Word: pendientes de regenerar** con el generador APA 7 del equipo para 01, 02, 04, 05, 06, 07 (procedimiento y despliegue), 08, 09 (los cuatro manuales), 10 (los tres artículos) y 11 (solo PDF). Los de 03 Propuesta técnica siguen en la 1.3 aunque el Markdown está en la 1.4. Esta entrada solo cambia los Markdown.

## 2026-10-21 — Código del 21 de octubre, servidor con respaldos y pruebas del día

**Contenido** (español e inglés)

- Código del 21 de octubre: el token de una sesión cerrada deja de servir (security-service y API Gateway); la reserva programada que sigue sin confirmarse una hora después de su hora de fin se cancela sola (motivo `EXPIRED`); la asignación manual y la automática usan el mismo candado y hay un solo conteo de reservas sin operario; el comprobante pesa como máximo 2 MB; Efectivo solo aparece con su cuenta activa; la sesión de la web se sincroniza entre pestañas; los reportes cuentan solo reservas completadas; la pestaña de roles dice que el acceso lo decide el rol; la app exige instalar el APK nuevo cuando se publica. Se documentó en 01 SRS 7.7, 02 Análisis 2.4, 04 Diseño 1.5, 05 Artefactos, 09 Manuales (técnico 4.5, instalación 4.4, usuario 4.5 y administrador 4.5) y 10 Artículos.
- Servidor (20 y 21 de octubre): respaldos diarios y antes de cada actualización, verificados con una restauración de prueba; modelo de recuperación SIMPLE; encabezados de seguridad y CSP en Caddy; chequeos de salud y registros limitados en todos los contenedores; se descartó el VPS de Hostinger. Se documentó en 03 Propuesta 1.4, 07 Despliegue 1.5 (con la actualización del 21 de octubre y los cambios del código que faltan por desplegar), 07 Procedimiento 2.4 y los manuales de instalación y de administrador.
- Cambios de la noche del 21 de octubre, después de la revisión del equipo: la primera versión del cierre automático dejaba en "No asistió" toda reserva confirmada que nadie inició, aunque el operario la hubiera atendido y solo olvidara darle "Iniciar". Ahora el sistema solo decide cuando está seguro: cancela la programada que venció sin confirmarse, deja en "No asistió" la confirmada que nunca tuvo operario (operations-service la pide por la ruta interna `POST /internal/v1/bookings/{id}/no-show`) y manda la que tenía operario y nadie inició o finalizó a la lista "Por cerrar" del administrador, en la web y en la app móvil, que la cierra como "Se atendió" o "No asistió" (`GET /api/v1/admin/assignments/to-close`, `POST /api/v1/admin/assignments/{bookingId}/attended`). Se agregaron los eventos `execution.service_not_started` y `execution.service_not_finished`, los avisos `OPERATOR_SERVICE_NOT_REGISTERED` y `ADMIN_SERVICE_NOT_REGISTERED`, las migraciones 040 (operations) y 041 (notification) y las variables `FOLLOW_UP_ENABLED` y `FOLLOW_UP_INTERVAL`. La app móvil usa la misma regla de "sin asignar" que la web, y un campo `null` en un evento ya no manda el mensaje a la cola de errores de notification-service. Se documentó en 02 Análisis (estados 4.1 y 4.3), 04 Diseño (pantallas, comunicación entre servicios, modelo de datos, clases y estados), 05 Artefactos (commits, tamaño de los clientes y variables), 07 Procedimiento 2.5 (prueba de humo H11) y Despliegue 1.6, y 11 Evidencias.
- 06 Pruebas: dos ejecuciones el 21 de octubre, la de la madrugada con 689 pruebas automatizadas y la final de la noche con 707 (+18: web 62, booking-service 50, operations-service 67 y notification-service 114), las dos con las 19 de punta a punta aprobadas; inventario de 602 métodos de prueba, clases nuevas `FollowUpPolicyTest`, `FollowUpServiceTest` y `DomainEventEnvelopeTest`, prueba en vivo de "Por cerrar" en la web y en la app móvil, defectos 11 y 12, trazabilidad y brechas.
- 08 Acciones 2.5: correctivas AC-44 a AC-52 cerradas y ACO-14 abierta (variables nuevas que no están en `.env.example` ni en el compose); preventivas AP-04 y AP-16 a AP-18 cerradas; mejora AM-16. Las mejoras del 17 de octubre que repetían los identificadores AM-07 y AM-08 pasan a ser AM-14 y AM-15.
- 08 Acciones 2.6: AC-45 ajustada; correctivas AC-53 (riesgo de registrar como "No asistió" un servicio que sí se hizo, encontrado en la revisión del equipo y corregido con la lista "Por cerrar") y AC-54 (campo `null` que mandaba el evento a la cola de errores) cerradas; preventiva AP-19 y lección L-16; ACO-14 con las variables `FOLLOW_UP_*`; indicadores con las 707 pruebas.
- Correcciones encontradas en la revisión: rutas que faltaban en la tabla del gateway y numeración de los changelogs (manual técnico), fecha y versión de la portada de los manuales de usuario y de administrador, 24 tipos de notificación y líneas de código citadas (diseño), y referencias de los artículos con las versiones vigentes de los documentos.
- 11 Evidencias: estado del servidor y pruebas del 21 de octubre (707 automatizadas en la ejecución final).
- Versiones de la noche del 21 de octubre: 01 SRS 7.8, 07 Procedimiento 2.5 y Despliegue 1.6, 08 Acciones 2.6 y manuales técnico, de usuario y de administrador 4.6 y de instalación 4.5 (el índice del README quedó una versión atrás y se corrigió el 23 de octubre).
- PDF y Word: el equipo los regeneró con su generador después de esta entrada, salvo los de 03 Propuesta técnica, que quedaron en la 1.3.

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
