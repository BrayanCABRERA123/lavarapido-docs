# Enlaces de evidencias del proyecto formativo — LavaRápido (Vehicle Washing)

**Plataforma web y móvil de reservas y gestión para un lavadero de vehículos**

| Campo | Dato |
|---|---|
| Programa / ficha | Tecnólogo en Análisis y Desarrollo de Software (ADSO), ficha 3145556 |
| Centro | Centro de la Industria, la Empresa y los Servicios — SENA, Regional Huila |
| Proyecto formativo | [Completar: nombre oficial del proyecto formativo] |
| Equipo de trabajo | Equipo de Desarrollo Vehicle Washing ([Completar: confirmar nombre oficial del equipo]) |
| Integrantes | Juan Camilo Guilombo Osorio, Brayan Estiven Patiño Cabrera, Merari Urbano Quintero |
| Instructora | Karol Daniela Correa |
| Fecha de entrega | [Completar] |
| Fecha de actualización de este documento | 16 de octubre de 2026 |

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
- **`vehicle-w-docs`** (privado, organización `code-sena`, rama `docs`): https://github.com/code-sena/vehicle-w-docs/tree/docs. Es la documentación técnica fuente del proyecto (SDD); los documentos de `lavarapido-docs` se derivan de ella. Cada evidencia enlaza primero la sección pública equivalente, para que siempre haya un enlace accesible.

Estructura de `lavarapido-docs`: cada evidencia tiene una carpeta numerada (`01_` a `11_`) y, dentro, `ES/` y `EN/`, cada uno con `MD/` (Markdown y sus `capturas/`), `PDF/` y `WORD/`. La matriz enlaza la versión en español en Markdown; el PDF y el Word están en las carpetas vecinas.

| # | Evidencia | Contenido mínimo verificable | Enlace directo | Estado de acceso | Observaciones |
|---|---|---|---|---|---|
| 1 | Informe de especificación de requisitos | RF y RNF, historias de usuario, criterios de aceptación, trazabilidad | [SRS v7.0 (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/ES/MD/informe-de-especificacion-de-requisitos.md) · [Requisitos funcionales (SRS §5)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/ES/MD/informe-de-especificacion-de-requisitos.md#5-requisitos-funcionales) · [Requisitos no funcionales (SRS §6)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/ES/MD/informe-de-especificacion-de-requisitos.md#6-requisitos-no-funcionales) · [Historias de usuario por requisito (SRS §10)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/ES/MD/informe-de-especificacion-de-requisitos.md#10-matriz-de-trazabilidad) · Fuente en `vehicle-w-docs`: [Requisitos funcionales](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/functional.md) · [Requisitos no funcionales](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/non-functional.md) · [Historias de usuario](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/user-stories.md) | Público / Pendiente de permisos (`vehicle-w-docs`) | El SRS sigue IEEE 830 e ISO/IEC/IEEE 29148 y recoge RF-001 a RF-035 y CU1 a CU29. Versión en inglés: `01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/EN/`. |
| 2 | Análisis del software | Vistas dinámicas, procesos, casos de uso, diagramas de secuencia y estados | [Análisis de vistas dinámicas (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/02_DOCUMENTACION_DE_ANALISIS_DEL_SOFTWARE/ES/MD/documentacion-de-analisis-del-software.md) · [Diagramas de secuencia, actividades y estados](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/02_DOCUMENTACION_DE_ANALISIS_DEL_SOFTWARE/ES/MD/documentacion-de-analisis-del-software.md#2-diagramas-de-secuencia) · Fuente en `vehicle-w-docs`: [Diagramas UML (fuentes)](https://github.com/code-sena/vehicle-w-docs/tree/docs/08-uml/diagrams/source) | Público / Pendiente de permisos (`vehicle-w-docs`) | Las capturas están en `02_DOCUMENTACION_DE_ANALISIS_DEL_SOFTWARE/ES/MD/capturas/`. Los diagramas incluyen secuencias de reserva, pago, registro, recordatorio y asignación, y estados de reserva y pago. |
| 3 | Propuesta técnica del software | Alternativa seleccionada, tecnologías, justificación, alcance y restricciones | [Propuesta técnica (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/03_PROPUESTA_TECNICA_DEL_SOFTWARE/ES/MD/propuesta-tecnica-del-software.md) · [Decisiones de diseño (SRS §3.6)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/ES/MD/informe-de-especificacion-de-requisitos.md#36-decisiones-de-diseño) · [Alternativas consideradas](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/03_PROPUESTA_TECNICA_DEL_SOFTWARE/ES/MD/propuesta-tecnica-del-software.md#3-alternativas-consideradas) · Fuente en `vehicle-w-docs`: [Decisiones de arquitectura (ADR-001 a ADR-015)](https://github.com/code-sena/vehicle-w-docs/tree/docs/05-architecture/decisions/records) | Público / Pendiente de permisos (`vehicle-w-docs`) | Los ADR justifican la arquitectura de microservicios, la base de datos, el API Gateway, JWT y el uso de .NET para el servicio de pagos. |
| 4 | Diseño del software | Interfaces gráficas, arquitectura, patrones, modelo de datos y diagramas | [Diseño del software (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/04_DOCUMENTACION_DE_DISENO_DEL_SOFTWARE/ES/MD/documentacion-de-diseno-del-software.md) · [Modelo arquitectónico](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/04_DOCUMENTACION_DE_DISENO_DEL_SOFTWARE/ES/MD/documentacion-de-diseno-del-software.md#3-modelo-arquitectónico) · [Modelo de datos](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/04_DOCUMENTACION_DE_DISENO_DEL_SOFTWARE/ES/MD/documentacion-de-diseno-del-software.md#5-modelo-de-datos) · [API y rutas del sistema (manual técnico §13)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/ES/MD/manual-tecnico.md#13-api-o-rutas-del-sistema) · Fuente en `vehicle-w-docs`: [Arquitectura](https://github.com/code-sena/vehicle-w-docs/tree/docs/05-architecture) · [Modelo de datos](https://github.com/code-sena/vehicle-w-docs/tree/docs/06-data) · [Contratos OpenAPI](https://github.com/code-sena/vehicle-w-docs/tree/docs/07-api/contracts/openapi) | Público / Pendiente de permisos (`vehicle-w-docs`) | Patrón de arquitectura hexagonal (ADR-007). Las capturas están en `04_DOCUMENTACION_DE_DISENO_DEL_SOFTWARE/ES/MD/capturas/`. |
| 5 | Código fuente y artefactos de software | Repositorios de frontend web, app móvil, backend, infraestructura y base de datos, con sus ramas | [Artefactos de código (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/05_ARTEFACTOS_DE_CODIGO/ES/MD/artefactos-de-codigo.md) · ver la [sección 2](#2-repositorios-de-código-fuente) | Público | La rama de integración es `develop`. `main` va atrasada en todos los repositorios (ver la sección 2). |
| 6 | Documentación de pruebas | Plan, casos de prueba, resultados, evidencias de ejecución, defectos y correcciones | [Documentación de pruebas (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/06_DOCUMENTACION_DE_PRUEBAS/ES/MD/documentacion-de-pruebas.md) · [Pruebas E2E](https://github.com/BrayanCABRERA123/lavarapido-infra/tree/develop/e2e) · [Plan de pruebas](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/06_DOCUMENTACION_DE_PRUEBAS/ES/MD/documentacion-de-pruebas.md#1-plan-de-pruebas) · Fuente en `vehicle-w-docs`: [Estrategia de pruebas](https://github.com/code-sena/vehicle-w-docs/blob/docs/11-quality/testing-strategy.md) | Público / Pendiente de permisos (`vehicle-w-docs`) | Sigue ISO/IEC/IEEE 29119-3. Pruebas automatizadas ejecutadas el 15/10/2026 y casos funcionales el 09/10/2026. La matriz de trazabilidad está en la §5 y los hallazgos en la §6. |
| 7 | Procedimiento de implementación | Instalación, configuración, despliegue y verificación reproducibles | [Procedimiento de implementación (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/ES/MD/procedimiento-de-implementacion.md) · [Documento de despliegue en Azure (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/ES/MD/documento-de-despliegue.md) · Apoyo: [README de infraestructura](https://github.com/BrayanCABRERA123/lavarapido-infra/blob/develop/README.md) · [Guía del equipo](https://github.com/BrayanCABRERA123/lavarapido-infra/blob/develop/GUIA-EQUIPO.md) | Público | Disponible en Markdown, PDF y Word (ES y EN) en `07_PROCEDIMIENTO_DE_IMPLEMENTACION/`. El documento de despliegue registra el despliegue del 16/10/2026 en Azure con sus capturas de evidencia. |
| 8 | Acciones correctivas, preventivas y de mejora | Hallazgos, prioridad, responsable, acción aplicada y evidencia de cierre | [Acciones correctivas, preventivas y de mejora (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/08_ACCIONES_CORRECTIVAS_PREVENTIVAS_Y_DE_MEJORA/ES/MD/acciones-correctivas-preventivas-y-de-mejora.md) · Apoyo: [Acciones preventivas](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/08_ACCIONES_CORRECTIVAS_PREVENTIVAS_Y_DE_MEJORA/ES/MD/acciones-correctivas-preventivas-y-de-mejora.md#11-registro-de-acciones-preventivas) · [Trazabilidad entre acciones, riesgos y deuda técnica](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/08_ACCIONES_CORRECTIVAS_PREVENTIVAS_Y_DE_MEJORA/ES/MD/acciones-correctivas-preventivas-y-de-mejora.md#anexo-c-trazabilidad-entre-acciones-riesgos-y-deuda-técnica) · Fuente en `vehicle-w-docs`: [Riesgos](https://github.com/code-sena/vehicle-w-docs/blob/docs/15-project-control/risks.md) · [Backlog técnico](https://github.com/code-sena/vehicle-w-docs/blob/docs/15-project-control/technical-backlog.md) | Público / Pendiente de permisos (`vehicle-w-docs`) | Disponible en Markdown, PDF y Word (ES y EN) en `08_ACCIONES_CORRECTIVAS_PREVENTIVAS_Y_DE_MEJORA/`. |
| 9 | Manual técnico, de instalación y de usuario | Requisitos previos, configuración, uso y solución de problemas | [Manual técnico (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/ES/MD/manual-tecnico.md) · [Manual de instalación (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/ES/MD/manual-de-instalacion.md) · [Manual de usuario (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/ES/MD/manual-de-usuario.md) · [Manual de administrador (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/ES/MD/manual-de-administrador.md) · [PDF de los manuales](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/09_MANUALES/ES/PDF) · Fuente en `vehicle-w-docs`: [Manual de usuario](https://github.com/code-sena/vehicle-w-docs/blob/docs/14-training/user-manual.md) | Público / Pendiente de permisos (`vehicle-w-docs`) | Cada manual está en Markdown, PDF y Word (ES y EN), en la carpeta `09_MANUALES/`. Los secretos del `.env` aparecen enmascarados. Algunas capturas siguen marcadas como «Captura por insertar». |
| 10 | Artículo del proyecto | Problema, objetivos, solución, metodología, resultados y conclusiones | [Artículo APA 7 (ES/EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/10_ARTICULO_DEL_PROYECTO/MD/articulo-del-proyecto-apa7.md) · [PDF APA 7](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/10_ARTICULO_DEL_PROYECTO/PDF/10_Articulo_Del_Proyecto_APA7.pdf) · [Versión IEEE](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/10_ARTICULO_DEL_PROYECTO/PDF/10_Articulo_Del_Proyecto_IEEE.pdf) · [Versión ACM](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/10_ARTICULO_DEL_PROYECTO/PDF/10_Articulo_Del_Proyecto_ACM.pdf) | Público | Las tres versiones (APA 7, IEEE y ACM) están en Markdown, PDF y Word, en la carpeta `10_ARTICULO_DEL_PROYECTO/`. Cada archivo es bilingüe (ES y EN en el mismo documento), por eso esta carpeta no se divide por idioma. |
| 11 | Aplicación desplegada o demostración | URL de acceso o entorno de demostración e instrucciones de verificación | [Aplicación en producción](https://lavarapidovehicular.northcentralus.cloudapp.azure.com) · [Descarga de la app Android](https://lavarapidovehicular.northcentralus.cloudapp.azure.com/app/LavaRapidoVehicular.apk) · [Documento de despliegue (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/ES/MD/documento-de-despliegue.md) | Público | Desplegada el 16/10/2026 en una máquina virtual de Azure (Docker Compose, Caddy con HTTPS de Let's Encrypt). Las pruebas de humo y las capturas están en la [sección 5 del documento de despliegue](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/ES/MD/documento-de-despliegue.md#5-plan-de-verificación-pruebas-y-evidencias-smoke-tests). Las credenciales se entregan por un canal privado (ver la sección 7). |
| 12 | Trazabilidad e integración de evidencias | Relación entre requisitos, HU, módulos, pruebas y versiones | [Matriz de trazabilidad (SRS §10)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/ES/MD/informe-de-especificacion-de-requisitos.md#10-matriz-de-trazabilidad) · [Trazabilidad requisitos–pruebas (§5)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/06_DOCUMENTACION_DE_PRUEBAS/ES/MD/documentacion-de-pruebas.md#5-matriz-de-trazabilidad) · Fuente en `vehicle-w-docs`: [Matriz de trazabilidad](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/traceability-matrix.md) | Público / Pendiente de permisos (`vehicle-w-docs`) | No hay release tags, así que la trazabilidad hacia las versiones se hace por rama (`develop`) y por commit. |

---

## 2. Repositorios de código fuente

Rama de trabajo: **`develop`** en todos los repositorios de código. No hay release tags. Las columnas «Último commit» y «`main` atrasada» se tomaron el 16/10/2026.

| Componente | Tecnología | Repositorio (rama `develop`) | Último commit | `main` atrasada | Acceso |
|---|---|---|---|---|---|
| Frontend web | Angular | [Front-end-proyecto-web](https://github.com/BrayanCABRERA123/Front-end-proyecto-web/tree/develop) | `ec72d23` | 394 commits | Público |
| Aplicación móvil | React Native (Expo) | [LavadoVehicular-Movil](https://github.com/merari0322/LavadoVehicular-Movil/tree/develop) | `1cdd392` | 171 commits | Público |
| API Gateway | Spring Boot | [lavarapido-api-gateway](https://github.com/BrayanCABRERA123/lavarapido-api-gateway/tree/develop) | `d752e5e` | 10 commits | Público |
| Seguridad (autenticación, JWT, roles) | Spring Boot | [lavarapido-security-service](https://github.com/BrayanCABRERA123/lavarapido-security-service/tree/develop) | `0c6e37f` | 47 commits | Público |
| Clientes y vehículos | Spring Boot | [lavarapido-customer-service](https://github.com/camiloguilombo12/lavarapido-customer-service/tree/develop) | `971655c` | 4 commits | Público |
| Catálogo y reservas | Spring Boot | [lavarapido-booking-service](https://github.com/camiloguilombo12/lavarapido-booking-service/tree/develop) | `5ae7ed3` | 43 commits | Público |
| Operación (operarios y bahías) | Spring Boot | [lavarapido-operation-service](https://github.com/BrayanCABRERA123/lavarapido-operation-service/tree/develop) | `438f605` | 33 commits | Público |
| Pagos y fidelización | .NET Core | [lavarapido-payment-service](https://github.com/merari0322/lavarapido-payment-service/tree/develop) | `3c3b0a6` | 37 commits | Público |
| Notificaciones | Spring Boot | [lavarapido-notification-service](https://github.com/BrayanCABRERA123/lavarapido-notification-service/tree/develop) | `6462b51` | 32 commits | Público |
| Infraestructura (Docker, base de datos, pruebas E2E) | Docker, SQL Server, RabbitMQ | [lavarapido-infra](https://github.com/BrayanCABRERA123/lavarapido-infra/tree/develop) | `c6259b5` | 52 commits | Público |
| Documentación técnica (SDD) | Markdown, OpenAPI | [vehicle-w-docs](https://github.com/code-sena/vehicle-w-docs/tree/docs) (rama `docs`) | `f73c5ac` | 299 commits | Pendiente de permisos |
| Evidencias documentales | Markdown | [lavarapido-docs](https://github.com/BrayanCABRERA123/lavarapido-docs) (rama `main`) | último commit de `main` | — | Público |

**Base de datos:** SQL Server 2022 compartido, con un esquema por servicio (ADR-003, ADR-009). Cada servicio Spring Boot gestiona sus migraciones con Liquibase. Las migraciones del servicio de pagos están en [`lavarapido-payment-service/db`](https://github.com/merari0322/lavarapido-payment-service/tree/develop/db).

> Recomendación: antes de entregar, fusionar `develop` en `main` en cada repositorio, o indicar al evaluador que revise `develop`, para que la versión evaluada sea coherente.

---

## 3. Despliegue y verificación técnica

| Aspecto | Valor |
|---|---|
| Versión (release tag) | `v1.0.0` pendiente. [Completar: crear el tag en cada repositorio al pasar `develop` a `main`] |
| Entorno | Producción académica en Azure (VM Ubuntu 24.04, Docker Compose con `docker-compose.prod.yml`), desplegada el 16/10/2026. Para desarrollo: local con Docker (`docker compose --profile app up -d --build` desde `lavarapido-infra`). Detalle en el [documento de despliegue](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/ES/MD/documento-de-despliegue.md). |
| Entorno de demostración público | https://lavarapidovehicular.northcentralus.cloudapp.azure.com |

### 3.1 Matriz de roles

| Rol | Funciones principales | Cliente donde se usa |
|---|---|---|
| Administrador | Usuarios y roles, catálogo, promociones, horarios y bahías, operarios, reservas, pagos, reportes | Web y móvil |
| Cliente | Registro, vehículos, reservas, pagos por QR o transferencia, historial, calificaciones, notificaciones | Web y móvil |
| Operario | Servicios asignados, horario, ejecución, historial, calificaciones recibidas | Web y móvil |

### 3.2 Endpoints de salud (verificados el 16/10/2026 en el entorno local)

| Servicio | Puerto | Endpoint | Resultado |
|---|---|---|---|
| API Gateway | 8080 | `/actuator/health` | `UP` |
| security-service | 3001 | `/actuator/health` | `UP` |
| customer-service | 3002 | `/actuator/health` | `UP` |
| booking-service | 3003 | `/actuator/health` | `UP` |
| operations-service | 3004 | `/actuator/health` | `UP` |
| payment-service | 3005 | `/health` | `ok` (consulta SQL Server; responde 503 si la base no contesta) |
| notification-service | 3006 | `/actuator/health` | `UP` |

### 3.3 Documentación interactiva de la API (Swagger/OpenAPI)

- **Servicios Spring Boot (puertos 3001–3004 y 3006):** `http://localhost:<puerto>/swagger-ui/index.html` respondió `200` el 16/10/2026.
- **payment-service (.NET Core):** Swagger solo se activa en el entorno `Development`. Bajo Docker no está expuesto (`404`). Para verlo, ejecutar el servicio con `ASPNETCORE_ENVIRONMENT=Development`.
- **Contratos versionados:** [`07-api/contracts/openapi`](https://github.com/code-sena/vehicle-w-docs/tree/docs/07-api/contracts/openapi) en `vehicle-w-docs` (privado). Versión pública: [API y rutas del sistema](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/ES/MD/manual-tecnico.md#13-api-o-rutas-del-sistema), en el manual técnico.

### 3.4 Pruebas de humo

| Prueba | Procedimiento | Resultado |
|---|---|---|
| Autenticación | `POST http://localhost:8080/api/v1/auth/login` con un usuario de prueba y comprobar que devuelve un JWT | 200 con `accessToken` (16/10/2026, cuenta de prueba del perfil *dev*) |
| Lectura | Con el JWT, consultar el catálogo de servicios o las reservas del cliente | `GET /api/v1/catalog/services` y `GET /api/v1/bookings/me` respondieron 200 (16/10/2026) |
| Escritura | Crear una reserva y comprobar que aparece en el historial y que llega la notificación | Cubierta por `full-flow.test.js`: reserva creada, asignada sola al operario elegido, pago aprobado, servicio iniciado y terminado, calificación y cada aviso en la bandeja del cliente (16/10/2026) |
| Flujo E2E automatizado | `node --test "e2e/*.test.js"` en `lavarapido-infra` (con `E2E_OPERATOR_ID=2` en la base local) | 19 de 19 pruebas aprobadas en 7,3 s (16/10/2026) |

### 3.5 Capturas de evidencia

| Captura | Descripción | Enlace |
|---|---|---|
| Pantallas web (login, admin, cliente, operario) | 28 capturas de la interfaz | [Carpeta `assets` del SRS](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/ES/MD/capturas) |
| Vistas dinámicas y modales | 41 capturas | [Carpeta `assets` del análisis](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/02_DOCUMENTACION_DE_ANALISIS_DEL_SOFTWARE/ES/MD/capturas) |
| Diseño (landing, login, reservar, pagos) | Capturas del diseño final | [Carpeta `capturas`](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/04_DOCUMENTACION_DE_DISENO_DEL_SOFTWARE/ES/MD/capturas) |
| Capturas reales de los manuales | 56 capturas por idioma del sistema funcionando (16/10/2026): pantallas de los tres roles, terminal de instalación y diagrama del modelo de datos | [Carpeta `capturas` de los manuales](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/09_MANUALES/ES/MD/capturas) |
| Contenedores, logs, health checks y migraciones en producción | Portainer, logs de arranque, `/actuator/health`, consola limpia y changesets de Liquibase (16/10/2026) | [Carpeta `capturas` del despliegue](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/ES/MD/capturas) |

---

## 4. Lista de verificación de accesibilidad y calidad

- [ ] Todos los enlaces abren correctamente, sin errores 404 ni accesos denegados, probados desde una cuenta que no pertenezca al equipo.
- [ ] El instructor tiene permiso de lectura en `code-sena/vehicle-w-docs` (privado) y lo comprobó con su cuenta.
- [ ] Cada evidencia de `lavarapido-docs` tiene su Markdown, PDF y Word en ES y EN, y los PDF y Word abren correctamente.
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
| Completitud | Las 12 evidencias tienen un enlace directo y verificable | Las 12 evidencias tienen enlace. La evidencia 11 enlaza la aplicación desplegada en Azure desde el 16/10/2026. |
| Accesibilidad | Todos los enlaces abren para el instructor sin solicitar permisos | Parcial: los enlaces de `lavarapido-docs` y de los repositorios de código son públicos (comprobado sin iniciar sesión); los de `vehicle-w-docs` requieren dar permiso de lectura al instructor. |
| Trazabilidad | Requisitos → HU → módulos → pruebas → versiones relacionados | Existe una matriz en la §10 del SRS, otra en la §5 del documento de pruebas y la matriz fuente en `vehicle-w-docs`. Faltan release tags. |
| Coherencia | La documentación coincide con el código y con la aplicación en ejecución | Entorno local verificado el 16/10/2026: todos los servicios `UP`, 639 pruebas automatizadas y 19 pruebas de punta a punta aprobadas, y los manuales 4.0 revisados contra el código. `main` está atrasada frente a `develop`. |
| Seguridad | Sin secretos ni datos personales expuestos | Revisado el 16/10/2026: ningún repositorio tiene archivos `.env` en su historial y los archivos versionados solo traen valores de ejemplo (`.env.example`). Las capturas usan datos de prueba. |
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
