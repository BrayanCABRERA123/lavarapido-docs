# Enlaces de evidencias del proyecto formativo — LavaRápido (Vehicle Washing)

**Plataforma web y móvil de reservas y gestión para un lavadero de vehículos**

| Campo | Dato |
|---|---|
| Programa / ficha | Tecnólogo en Análisis y Desarrollo de Software (ADSO), ficha 3145556 |
| Centro | Centro de la Industria, la Empresa y los Servicios — SENA, Regional Huila |
| Proyecto formativo | [Completar: nombre oficial del proyecto formativo] |
| Equipo de trabajo | Equipo de Desarrollo Vehicle Washing ([Completar: confirmar nombre oficial del equipo]) |
| Integrantes | Juan Camilo Guilombo Osorio, Brayan Estiven Patiño Cabrera, Merari Urbano Quintero |
| Instructores | José de Jesús Motta Vargas, Karol Daniela Correa |
| Fecha de entrega | [Completar] |
| Fecha de actualización de este documento | 15 de octubre de 2026 |

---

## Contenido

1. [Matriz de evidencias](#1-matriz-de-evidencias)
2. [Repositorios de código fuente](#2-repositorios-de-código-fuente)
3. [Despliegue y verificación técnica](#3-despliegue-y-verificación-técnica)
4. [Lista de verificación de accesibilidad y calidad](#4-lista-de-verificación-de-accesibilidad-y-calidad)
5. [Criterios de aceptación](#5-criterios-de-aceptación)
6. [Entrega](#6-entrega)
7. [Nota de seguridad](#7-nota-de-seguridad)
8. [Recursos de consulta](#8-recursos-de-consulta)
9. [Recordatorio para el equipo](#9-recordatorio-para-el-equipo)

---

## 1. Matriz de evidencias

**Repositorios de documentación usados en la matriz**

- **`lavarapido-docs`** (público, rama `main`): https://github.com/BrayanCABRERA123/lavarapido-docs
- **`vehicle-w-docs`** (privado, organización `code-sena`, rama `docs`): https://github.com/code-sena/vehicle-w-docs/tree/docs

Cada evidencia tiene su versión en español (`ES/`) y en inglés (`EN/`). La matriz enlaza la versión en español.

| # | Evidencia | Contenido mínimo verificable | Enlace directo | Estado de acceso | Observaciones |
|---|---|---|---|---|---|
| 1 | Informe de especificación de requisitos | RF y RNF, historias de usuario, criterios de aceptación, trazabilidad | [SRS v6.0 (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01-informe-especificacion-requisitos/ES/informe-especificacion-requisitos.md) · [Requisitos funcionales](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/functional.md) · [Requisitos no funcionales](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/non-functional.md) · [Historias de usuario](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/user-stories.md) | Público (SRS) / Pendiente de permisos (`vehicle-w-docs`) | El SRS sigue IEEE 830 e ISO/IEC/IEEE 29148 y recoge RF-001 a RF-035 y CU1 a CU29. Versión en inglés: `01-informe-especificacion-requisitos/EN/`. |
| 2 | Análisis del software | Vistas dinámicas, procesos, casos de uso, diagramas de secuencia y estados | [Análisis de vistas dinámicas (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/02-analisis-vistas-dinamicas/ES/analisis-vistas-dinamicas.md) · [Diagramas UML (fuentes)](https://github.com/code-sena/vehicle-w-docs/tree/docs/08-uml/diagrams/source) | Público / Pendiente de permisos | Las capturas están en `02-analisis-vistas-dinamicas/assets/`. Los diagramas incluyen secuencias de reserva, pago, registro, recordatorio y asignación, y estados de reserva y pago. |
| 3 | Propuesta técnica del software | Alternativa seleccionada, tecnologías, justificación, alcance y restricciones | [Propuesta técnica (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/03-propuesta-tecnica/ES/propuesta-tecnica.md) · [Decisiones de arquitectura (ADR-001 a ADR-015)](https://github.com/code-sena/vehicle-w-docs/tree/docs/05-architecture/decisions/records) | Público / Pendiente de permisos | Los ADR justifican la arquitectura de microservicios, la base de datos, el API Gateway, JWT y el uso de .NET para el servicio de pagos. |
| 4 | Diseño del software | Interfaces gráficas, arquitectura, patrones, modelo de datos y diagramas | [Diseño del software (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/Diseno-del-Software/ES/Diseno-del-Software.md) · [Arquitectura](https://github.com/code-sena/vehicle-w-docs/tree/docs/05-architecture) · [Modelo de datos](https://github.com/code-sena/vehicle-w-docs/tree/docs/06-data) · [Contratos OpenAPI](https://github.com/code-sena/vehicle-w-docs/tree/docs/07-api/contracts/openapi) | Público / Pendiente de permisos | Patrón de arquitectura hexagonal (ADR-007). Las capturas están en `Diseno-del-Software/capturas/`. |
| 5 | Código fuente y artefactos de software | Repositorios de frontend web, app móvil, backend, infraestructura y base de datos, con sus ramas | [Artefactos de código (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/Artefactos-de-Codigo/ES/Artefactos-de-Codigo.md) · ver la [sección 2](#2-repositorios-de-código-fuente) | Público | La rama de integración es `develop`. `main` va atrasada en todos los repositorios (ver la sección 2). |
| 6 | Documentación de pruebas | Plan, casos de prueba, resultados, evidencias de ejecución, defectos y correcciones | [Documentación de pruebas (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/Documentacion-de-Pruebas/ES/Documentacion-de-Pruebas.md) · [Pruebas E2E](https://github.com/BrayanCABRERA123/lavarapido-infra/tree/develop/e2e) · [Estrategia de pruebas](https://github.com/code-sena/vehicle-w-docs/blob/docs/11-quality/testing-strategy.md) | Público / Pendiente de permisos | Sigue ISO/IEC/IEEE 29119-3. Pruebas automatizadas ejecutadas el 15/10/2026 y casos funcionales el 09/10/2026. La matriz de trazabilidad está en la §5 y los hallazgos en la §6. |
| 7 | Procedimiento de implementación | Instalación, configuración, despliegue y verificación reproducibles | [Agregar enlace](URL) · Apoyo: [README de infraestructura](https://github.com/BrayanCABRERA123/lavarapido-infra/blob/develop/README.md) · [Guía del equipo](https://github.com/BrayanCABRERA123/lavarapido-infra/blob/develop/GUIA-EQUIPO.md) | No disponible | `Procedimiento_implementacion_LavadoVehicular_3145556_ES.md` solo existe en el equipo local, en la carpeta `Lavado vhecular--Documentacion`. Falta subirlo a `lavarapido-docs`. |
| 8 | Acciones correctivas, preventivas y de mejora | Hallazgos, prioridad, responsable, acción aplicada y evidencia de cierre | [Agregar enlace](URL) · Apoyo: [Riesgos](https://github.com/code-sena/vehicle-w-docs/blob/docs/15-project-control/risks.md) · [Backlog técnico](https://github.com/code-sena/vehicle-w-docs/blob/docs/15-project-control/technical-backlog.md) | No disponible | `Acciones_correctivas_preventivas_mejora_LavadoVehicular_3145556_ES.md` solo existe en el equipo local. Falta subirlo. |
| 9 | Manual técnico, de instalación y de usuario | Requisitos previos, configuración, uso y solución de problemas | [Agregar enlace: manual técnico](URL) · [Agregar enlace: manual de instalación](URL) · [Agregar enlace: manual de usuario](URL) · [Agregar enlace: manual de administrador](URL) · Apoyo: [Manual de usuario en `vehicle-w-docs`](https://github.com/code-sena/vehicle-w-docs/blob/docs/14-training/user-manual.md) | No disponible | Los cuatro manuales (MD y PDF) solo existen en el equipo local, en `Lavado vhecular--Documentacion`. Falta subirlos. |
| 10 | Artículo del proyecto | Problema, objetivos, solución, metodología, resultados y conclusiones | [Agregar enlace](URL) | No disponible | Existen versiones APA, ACM e IEEE (MD y PDF) solo en el equipo local, en `LavadoRapido-Documentos patra el articulo`. Falta subirlas. |
| 11 | Aplicación desplegada o demostración | URL de acceso o entorno de demostración e instrucciones de verificación | [Agregar enlace](URL) | No disponible | No hay despliegue público (VPS, staging o producción). Se verificó un entorno local con Docker el 15/10/2026 (ver la [sección 3](#3-despliegue-y-verificación-técnica)). Si no habrá despliegue público, acordar con el instructor una demostración en vivo o un video. |
| 12 | Trazabilidad e integración de evidencias | Relación entre requisitos, HU, módulos, pruebas y versiones | [Matriz de trazabilidad](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/traceability-matrix.md) · [Trazabilidad requisitos–pruebas (§5)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/Documentacion-de-Pruebas/ES/Documentacion-de-Pruebas.md#5-matriz-de-trazabilidad) | Pendiente de permisos / Público | No hay release tags, así que la trazabilidad hacia las versiones se hace por rama (`develop`) y por commit. |

---

## 2. Repositorios de código fuente

Rama de trabajo: **`develop`** en todos los repositorios de código. No hay release tags. Las columnas «Último commit» y «`main` atrasada» se tomaron el 15/10/2026.

| Componente | Tecnología | Repositorio (rama `develop`) | Último commit | `main` atrasada | Acceso |
|---|---|---|---|---|---|
| Frontend web | Angular | [Front-end-proyecto-web](https://github.com/BrayanCABRERA123/Front-end-proyecto-web/tree/develop) | `0def742` | 323 commits | Público |
| Aplicación móvil | React Native (Expo) | [LavadoVehicular-Movil](https://github.com/merari0322/LavadoVehicular-Movil/tree/develop) | `a3b98a3` | 123 commits | Público |
| API Gateway | Spring Boot | [lavarapido-api-gateway](https://github.com/BrayanCABRERA123/lavarapido-api-gateway/tree/develop) | `d752e5e` | 10 commits | Público |
| Seguridad (autenticación, JWT, roles) | Spring Boot | [lavarapido-security-service](https://github.com/BrayanCABRERA123/lavarapido-security-service/tree/develop) | `dab7cb2` | 37 commits | Público |
| Clientes y vehículos | Spring Boot | [lavarapido-customer-service](https://github.com/camiloguilombo12/lavarapido-customer-service/tree/develop) | `4e9f280` | 2 commits | Público |
| Catálogo y reservas | Spring Boot | [lavarapido-booking-service](https://github.com/camiloguilombo12/lavarapido-booking-service/tree/develop) | `1eca172` | 39 commits | Público |
| Operación (operarios y bahías) | Spring Boot | [lavarapido-operation-service](https://github.com/BrayanCABRERA123/lavarapido-operation-service/tree/develop) | `0906cdb` | 24 commits | Público |
| Pagos y fidelización | .NET Core | [lavarapido-payment-service](https://github.com/merari0322/lavarapido-payment-service/tree/develop) | `d10577a` | 32 commits | Público |
| Notificaciones | Spring Boot | [lavarapido-notification-service](https://github.com/BrayanCABRERA123/lavarapido-notification-service/tree/develop) | `524014c` | 23 commits | Público |
| Infraestructura (Docker, base de datos, pruebas E2E) | Docker, SQL Server, RabbitMQ | [lavarapido-infra](https://github.com/BrayanCABRERA123/lavarapido-infra/tree/develop) | `28c4a80` | 22 commits | Público |
| Documentación técnica (SDD) | Markdown, OpenAPI | [vehicle-w-docs](https://github.com/code-sena/vehicle-w-docs/tree/docs) (rama `docs`) | `b47be20` | 278 commits | Pendiente de permisos |
| Evidencias documentales | Markdown | [lavarapido-docs](https://github.com/BrayanCABRERA123/lavarapido-docs) (rama `main`) | `e4aa504` | — | Público |

**Base de datos:** SQL Server 2022 compartido, con un esquema por servicio (ADR-003, ADR-009). Cada servicio Spring Boot gestiona sus migraciones con Liquibase. Las migraciones del servicio de pagos están en [`lavarapido-payment-service/db`](https://github.com/merari0322/lavarapido-payment-service/tree/develop/db).

> Recomendación: antes de entregar, fusionar `develop` en `main` en cada repositorio, o indicar al evaluador que revise `develop`, para que la versión evaluada sea coherente.

---

## 3. Despliegue y verificación técnica

| Aspecto | Valor |
|---|---|
| Versión (release tag) | No hay. [Completar: crear un tag, por ejemplo `v1.0.0`, en cada repositorio antes de la entrega] |
| Entorno | Local con Docker (`docker compose --profile app up -d --build` desde `lavarapido-infra`). No hay VPS, staging ni producción. |
| Entorno de demostración público | [Agregar enlace](URL) |

### 3.1 Matriz de roles

| Rol | Funciones principales | Cliente donde se usa |
|---|---|---|
| Administrador | Usuarios y roles, catálogo, promociones, horarios y bahías, operarios, reservas, pagos, reportes | Web y móvil |
| Cliente | Registro, vehículos, reservas, pagos por QR o transferencia, historial, calificaciones, notificaciones | Web y móvil |
| Operario | Servicios asignados, horario, ejecución, historial, calificaciones recibidas | Web y móvil |

### 3.2 Endpoints de salud (verificados el 15/10/2026 en el entorno local)

| Servicio | Puerto | Endpoint | Resultado |
|---|---|---|---|
| API Gateway | 8080 | `/actuator/health` | `UP` |
| security-service | 3001 | `/actuator/health` | `UP` |
| customer-service | 3002 | `/actuator/health` | `UP` |
| booking-service | 3003 | `/actuator/health` | `UP` |
| operations-service | 3004 | `/actuator/health` | `UP` |
| payment-service | 3005 | `/health` | `UP` |
| notification-service | 3006 | `/actuator/health` | `UP` |

### 3.3 Documentación interactiva de la API (Swagger/OpenAPI)

- **Servicios Spring Boot (puertos 3001–3004 y 3006):** `http://localhost:<puerto>/swagger-ui/index.html` respondió `200` el 15/10/2026.
- **payment-service (.NET Core):** Swagger solo se activa en el entorno `Development`. Bajo Docker no está expuesto (`404`). Para verlo, ejecutar el servicio con `ASPNETCORE_ENVIRONMENT=Development`.
- **Contratos versionados:** [`07-api/contracts/openapi`](https://github.com/code-sena/vehicle-w-docs/tree/docs/07-api/contracts/openapi) en `vehicle-w-docs`.

### 3.4 Pruebas de humo

| Prueba | Procedimiento | Resultado |
|---|---|---|
| Autenticación | `POST http://localhost:8080/api/v1/auth/login` con un usuario de prueba y comprobar que devuelve un JWT | [Completar] |
| Lectura | Con el JWT, consultar el catálogo de servicios o las reservas del cliente | [Completar] |
| Escritura | Crear una reserva y comprobar que aparece en el historial y que llega la notificación a Mailpit (`http://localhost:8025`) | [Completar] |
| Flujo E2E automatizado | `lavarapido-infra/e2e/booking-flow.test.js` | [Completar] |

### 3.5 Capturas de evidencia

| Captura | Descripción | Enlace |
|---|---|---|
| Pantallas web (login, admin, cliente, operario) | 28 capturas de la interfaz | [Carpeta `assets` del SRS](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/01-informe-especificacion-requisitos/assets) |
| Vistas dinámicas y modales | 41 capturas | [Carpeta `assets` del análisis](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/02-analisis-vistas-dinamicas/assets) |
| Diseño (landing, login, reservar, pagos) | Capturas del diseño final | [Carpeta `capturas`](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/Diseno-del-Software/capturas) |
| Ejecución E2E | Capturas generadas por las pruebas E2E | [Agregar enlace](URL): la carpeta `e2e/shots` existe solo en local (no está versionada) |
| Contenedores y health checks | `docker ps` y respuestas de `/actuator/health` | [Agregar enlace](URL) |

---

## 4. Lista de verificación de accesibilidad y calidad

- [ ] Todos los enlaces abren correctamente, sin errores 404 ni accesos denegados, probados desde una cuenta que no pertenezca al equipo.
- [ ] El instructor tiene permiso de lectura en `code-sena/vehicle-w-docs` (privado) y lo comprobó con su cuenta.
- [ ] Los documentos de las evidencias 7, 8, 9 y 10 están subidos y sus enlaces reemplazan los `[Agregar enlace](URL)`.
- [ ] Los documentos son legibles: el Markdown se renderiza en GitHub y los PDF abren sin errores.
- [ ] Cada repositorio identifica el proyecto (README), la rama evaluada (`develop`) y la versión (release tag).
- [ ] La documentación, los repositorios y la aplicación son coherentes: lo que describen el SRS y los manuales existe en el código de `develop`.
- [ ] No se presentan simulaciones (mocks, `json-server`, datos de ejemplo) como funcionalidades reales.
- [ ] No hay credenciales ni datos sensibles: `.env` no está versionado (solo `.env.example`) y no hay tokens ni contraseñas en el historial.
- [ ] El PDF exportado conserva los enlaces activos (hacer clic en al menos uno por sección).

---

## 5. Criterios de aceptación

| Criterio | Condición de cumplimiento | Resultado / observaciones |
|---|---|---|
| Completitud | Las 12 evidencias tienen un enlace directo y verificable | Parcial: las evidencias 7, 8, 9, 10 y 11 no tienen enlace público todavía. |
| Accesibilidad | Todos los enlaces abren para el instructor sin solicitar permisos | Parcial: `vehicle-w-docs` es privado y está pendiente de otorgar acceso. |
| Trazabilidad | Requisitos → HU → módulos → pruebas → versiones relacionados | Existe una matriz en `vehicle-w-docs` y otra en la §5 del documento de pruebas. Faltan release tags. |
| Coherencia | La documentación coincide con el código y con la aplicación en ejecución | Entorno local verificado el 15/10/2026 (todos los servicios `UP`). `main` está atrasada frente a `develop`. |
| Seguridad | Sin secretos ni datos personales expuestos | [Completar después de revisar los repositorios públicos] |
| Presentación | Documento navegable, tablas legibles y PDF con enlaces activos | [Completar después de exportar el PDF] |

---

## 6. Entrega

| Formato | Nombre sugerido |
|---|---|
| Markdown | `Enlaces_Evidencias_Proyecto_VehicleWashing.md` |
| PDF | `Enlaces_Evidencias_Proyecto_VehicleWashing_[Fecha].pdf` (por ejemplo, `..._2026-10-15.pdf`) |

El medio de entrega (plataforma, correo, carpeta compartida u otro) lo indica el instructor.

---

## 7. Nota de seguridad

- No incluir en este documento ni en los repositorios contraseñas, tokens, llaves API, el contenido de `.env`, cadenas de conexión ni datos personales reales.
- **Credenciales de prueba:** si el evaluador necesita iniciar sesión, el equipo le entregará por un canal privado (mensaje directo o plataforma institucional) un usuario de prueba por rol (administrador, cliente y operario). Esas cuentas se crean solo para la evaluación y se desactivan después.
- No usar enlaces a archivos locales (`C:\...`, `file://`), enlaces vencidos ni enlaces que requieran permisos sin resolver.
- **Repositorios públicos:** revisar el historial (archivos `.env`, secretos de JWT, contraseñas de base de datos) antes de publicarlos o de entregar.
- **Repositorios privados** (`vehicle-w-docs`): otorgar al instructor permiso de lectura y comprobar el acceso con su cuenta.

---

## 8. Recursos de consulta

- [GitHub Docs: Acerca de los repositorios](https://docs.github.com/es/repositories/creating-and-managing-repositories/about-repositories)
- [GitHub Docs: Configurar la visibilidad de un repositorio](https://docs.github.com/es/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility)

---

## 9. Recordatorio para el equipo

> Actualicen esta matriz cada vez que cambien ubicaciones, ramas, versiones o permisos. Después de cada cambio, reexporten el PDF y vuelvan a comprobar los enlaces en el PDF exportado.
