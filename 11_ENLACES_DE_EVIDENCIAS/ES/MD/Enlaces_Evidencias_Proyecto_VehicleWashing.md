# Enlaces de evidencias del proyecto formativo — LavaRápido (Vehicle Washing)

**Plataforma web y móvil de reservas y gestión para un lavadero de vehículos**

| Campo | Dato |
|---|---|
| Programa / ficha | Tecnólogo en Análisis y Desarrollo de Software (ADSO), ficha 3145556 |
| Centro | Centro de la Industria, la Empresa y los Servicios — SENA, Regional Huila |
| Proyecto formativo | Sistema de Gestión de Lavado Vehicular (Vehicle Washing / LavaRápido), como figura en la portada de los entregables. Pendiente confirmar con la instructora si la ficha lo registra con otro nombre (responsable: Brayan Cabrera) |
| Equipo de trabajo | Equipo de Desarrollo Vehicle Washing (equipo 8 en la evaluación del instructor del 21/10/2026) |
| Integrantes | Juan Camilo Guilombo Osorio, Brayan Estiven Patiño Cabrera, Merari Urbano Quintero |
| Instructora | Karol Daniela Correa |
| Fecha de entrega | Exposición final prevista para la semana del 27 de octubre de 2026; la fecha exacta la confirma la instructora (responsable de confirmarla: Brayan Cabrera) |
| Fecha de actualización de este documento | 24 de octubre de 2026 |

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

Estructura de `lavarapido-docs`: el [índice general (README)](https://github.com/BrayanCABRERA123/lavarapido-docs#readme) enlaza todas las evidencias y el [historial de cambios (CHANGELOG)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/CHANGELOG.md) registra cada versión. Cada evidencia tiene una carpeta numerada (`01_` a `11_`) y, dentro, `ES/` y `EN/`, cada uno con `MD/` (Markdown y sus `capturas/`), `PDF/` y `WORD/`; el artículo (10) es bilingüe en un solo archivo y esta matriz (11) tiene Markdown y PDF. La matriz enlaza la versión en español en Markdown; el PDF y el Word están en las carpetas vecinas.

| # | Evidencia | Contenido mínimo verificable | Enlace directo | Estado de acceso | Observaciones |
|---|---|---|---|---|---|
| 1 | Informe de especificación de requisitos | RF y RNF, historias de usuario, criterios de aceptación, trazabilidad | [SRS v8.0 (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/ES/MD/informe-de-especificacion-de-requisitos.md) · [Requisitos funcionales (SRS §5)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/ES/MD/informe-de-especificacion-de-requisitos.md#5-requisitos-funcionales) · [Requisitos no funcionales (SRS §6)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/ES/MD/informe-de-especificacion-de-requisitos.md#6-requisitos-no-funcionales) · [Historias de usuario por requisito (SRS §10)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/ES/MD/informe-de-especificacion-de-requisitos.md#10-matriz-de-trazabilidad) · Fuente en `vehicle-w-docs`: [Requisitos funcionales](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/functional.md) · [Requisitos no funcionales](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/non-functional.md) · [Historias de usuario](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/user-stories.md) | Público / Pendiente de permisos (`vehicle-w-docs`) | El SRS sigue IEEE 830 e ISO/IEC/IEEE 29148 y recoge 41 requisitos funcionales (RF-001 a RF-038) y los casos de uso CU01 a CU32. Versión en inglés: `01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/EN/`. |
| 2 | Análisis del software | Vistas dinámicas, procesos, casos de uso, diagramas de secuencia y estados | [Análisis de vistas dinámicas (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/02_DOCUMENTACION_DE_ANALISIS_DEL_SOFTWARE/ES/MD/documentacion-de-analisis-del-software.md) · [Diagramas de secuencia, actividades y estados](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/02_DOCUMENTACION_DE_ANALISIS_DEL_SOFTWARE/ES/MD/documentacion-de-analisis-del-software.md#2-diagramas-de-secuencia) · Fuente en `vehicle-w-docs`: [Diagramas UML (fuentes)](https://github.com/code-sena/vehicle-w-docs/tree/docs/08-uml/diagrams/source) | Público / Pendiente de permisos (`vehicle-w-docs`) | Las capturas están en `02_DOCUMENTACION_DE_ANALISIS_DEL_SOFTWARE/ES/MD/capturas/`. Los diagramas incluyen secuencias de reserva, pago, registro, recordatorio y asignación, y estados de reserva y pago. |
| 3 | Propuesta técnica del software | Alternativa seleccionada, tecnologías, justificación, alcance y restricciones | [Propuesta técnica (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/03_PROPUESTA_TECNICA_DEL_SOFTWARE/ES/MD/propuesta-tecnica-del-software.md) · [Decisiones de diseño (SRS §3.6)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/ES/MD/informe-de-especificacion-de-requisitos.md#36-decisiones-de-diseño) · [Alternativas consideradas](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/03_PROPUESTA_TECNICA_DEL_SOFTWARE/ES/MD/propuesta-tecnica-del-software.md#3-alternativas-consideradas) · Fuente en `vehicle-w-docs`: [Decisiones de arquitectura (ADR-001 a ADR-015)](https://github.com/code-sena/vehicle-w-docs/tree/docs/05-architecture/decisions/records) | Público / Pendiente de permisos (`vehicle-w-docs`) | Los ADR justifican la arquitectura de microservicios, la base de datos, el API Gateway, JWT y el uso de .NET para el servicio de pagos. |
| 4 | Diseño del software | Interfaces gráficas, arquitectura, patrones, modelo de datos y diagramas | [Diseño del software (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/04_DOCUMENTACION_DE_DISENO_DEL_SOFTWARE/ES/MD/documentacion-de-diseno-del-software.md) · [Modelo arquitectónico](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/04_DOCUMENTACION_DE_DISENO_DEL_SOFTWARE/ES/MD/documentacion-de-diseno-del-software.md#3-modelo-arquitectónico) · [Modelo de datos](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/04_DOCUMENTACION_DE_DISENO_DEL_SOFTWARE/ES/MD/documentacion-de-diseno-del-software.md#5-modelo-de-datos) · [API y rutas del sistema (manual técnico §13)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/ES/MD/manual-tecnico.md#13-api-o-rutas-del-sistema) · Fuente en `vehicle-w-docs`: [Arquitectura](https://github.com/code-sena/vehicle-w-docs/tree/docs/05-architecture) · [Modelo de datos](https://github.com/code-sena/vehicle-w-docs/tree/docs/06-data) · [Contratos OpenAPI](https://github.com/code-sena/vehicle-w-docs/tree/docs/07-api/contracts/openapi) | Público / Pendiente de permisos (`vehicle-w-docs`) | Patrón de arquitectura hexagonal (ADR-007). Las capturas están en `04_DOCUMENTACION_DE_DISENO_DEL_SOFTWARE/ES/MD/capturas/`. |
| 5 | Código fuente y artefactos de software | Repositorios de frontend web, app móvil, backend, infraestructura y base de datos, con sus ramas | [Artefactos de código (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/05_ARTEFACTOS_DE_CODIGO/ES/MD/artefactos-de-codigo.md) · ver la [sección 2](#2-repositorios-de-código-fuente) | Público | La rama de integración es `develop`. `main` va atrasada en todos los repositorios (ver la sección 2). |
| 6 | Documentación de pruebas | Plan, casos de prueba, resultados, evidencias de ejecución, defectos y correcciones | [Documentación de pruebas (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/06_DOCUMENTACION_DE_PRUEBAS/ES/MD/documentacion-de-pruebas.md) · [Pruebas E2E](https://github.com/BrayanCABRERA123/lavarapido-infra/tree/develop/e2e) · [Plan de pruebas](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/06_DOCUMENTACION_DE_PRUEBAS/ES/MD/documentacion-de-pruebas.md#1-plan-de-pruebas) · Fuente en `vehicle-w-docs`: [Estrategia de pruebas](https://github.com/code-sena/vehicle-w-docs/blob/docs/11-quality/testing-strategy.md) | Público / Pendiente de permisos (`vehicle-w-docs`) | Sigue ISO/IEC/IEEE 29119-3. Pruebas automatizadas (689) y de punta a punta (19) ejecutadas el 21/10/2026; casos funcionales (42), rendimiento y diseño adaptable, el 19/10/2026 (§3). La matriz de trazabilidad está en la §5 y los hallazgos en la §6. |
| 7 | Procedimiento de implementación | Instalación, configuración, despliegue y verificación reproducibles | [Procedimiento de implementación (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/ES/MD/procedimiento-de-implementacion.md) · [Documento de despliegue en Azure (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/ES/MD/documento-de-despliegue.md) · Apoyo: [README de infraestructura](https://github.com/BrayanCABRERA123/lavarapido-infra/blob/develop/README.md) · [Guía del equipo](https://github.com/BrayanCABRERA123/lavarapido-infra/blob/develop/GUIA-EQUIPO.md) | Público | Disponible en Markdown, PDF y Word (ES y EN) en `07_PROCEDIMIENTO_DE_IMPLEMENTACION/`. El documento de despliegue registra el despliegue del 16/10/2026 en Azure con sus capturas de evidencia. |
| 8 | Acciones correctivas, preventivas y de mejora | Hallazgos, prioridad, responsable, acción aplicada y evidencia de cierre | [Acciones correctivas, preventivas y de mejora (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/08_ACCIONES_CORRECTIVAS_PREVENTIVAS_Y_DE_MEJORA/ES/MD/acciones-correctivas-preventivas-y-de-mejora.md) · Apoyo: [Acciones preventivas](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/08_ACCIONES_CORRECTIVAS_PREVENTIVAS_Y_DE_MEJORA/ES/MD/acciones-correctivas-preventivas-y-de-mejora.md#11-registro-de-acciones-preventivas) · [Trazabilidad entre acciones, riesgos y deuda técnica](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/08_ACCIONES_CORRECTIVAS_PREVENTIVAS_Y_DE_MEJORA/ES/MD/acciones-correctivas-preventivas-y-de-mejora.md#anexo-c-trazabilidad-entre-acciones-riesgos-y-deuda-técnica) · Fuente en `vehicle-w-docs`: [Riesgos](https://github.com/code-sena/vehicle-w-docs/blob/docs/15-project-control/risks.md) · [Backlog técnico](https://github.com/code-sena/vehicle-w-docs/blob/docs/15-project-control/technical-backlog.md) | Público / Pendiente de permisos (`vehicle-w-docs`) | Disponible en Markdown, PDF y Word (ES y EN) en `08_ACCIONES_CORRECTIVAS_PREVENTIVAS_Y_DE_MEJORA/`. |
| 9 | Manual técnico, de instalación y de usuario | Requisitos previos, configuración, uso y solución de problemas | [Manual técnico (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/ES/MD/manual-tecnico.md) · [Manual de instalación (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/ES/MD/manual-de-instalacion.md) · [Manual de usuario (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/ES/MD/manual-de-usuario.md) · [Manual de administrador (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/ES/MD/manual-de-administrador.md) · [PDF de los manuales](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/09_MANUALES/ES/PDF) · Fuente en `vehicle-w-docs`: [Manual de usuario](https://github.com/code-sena/vehicle-w-docs/blob/docs/14-training/user-manual.md) | Público / Pendiente de permisos (`vehicle-w-docs`) | Cada manual está en Markdown, PDF y Word (ES y EN), en la carpeta `09_MANUALES/`. Versión 4.3 o posterior (ver el control de versiones de cada manual), con capturas reales del sistema; los secretos del `.env` aparecen enmascarados. |
| 10 | Artículo del proyecto | Problema, objetivos, solución, metodología, resultados y conclusiones | [Artículo APA 7 (ES/EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/10_ARTICULO_DEL_PROYECTO/MD/articulo-del-proyecto-apa7.md) · [PDF APA 7](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/10_ARTICULO_DEL_PROYECTO/PDF/10_Articulo_Del_Proyecto_APA7.pdf) · [Versión IEEE](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/10_ARTICULO_DEL_PROYECTO/PDF/10_Articulo_Del_Proyecto_IEEE.pdf) · [Versión ACM](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/10_ARTICULO_DEL_PROYECTO/PDF/10_Articulo_Del_Proyecto_ACM.pdf) | Público | Las tres versiones (APA 7, IEEE y ACM) están en Markdown, PDF y Word, en la carpeta `10_ARTICULO_DEL_PROYECTO/`. Cada archivo es bilingüe (ES y EN en el mismo documento), por eso esta carpeta no se divide por idioma. |
| 11 | Aplicación desplegada o demostración | URL de acceso o entorno de demostración e instrucciones de verificación | [Aplicación en producción](https://lavarapidovehicular.northcentralus.cloudapp.azure.com) · [Descarga de la app Android](https://lavarapidovehicular.northcentralus.cloudapp.azure.com/app/LavaRapidoVehicular.apk) · [Documento de despliegue (ES)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/ES/MD/documento-de-despliegue.md) | Público | Desplegada el 16/10/2026 en una máquina virtual de Azure (Docker Compose, Caddy con HTTPS de Let's Encrypt) y actualizada por última vez el 22/10/2026 con los cambios del 21/10/2026 (migraciones 112, 040 y 041). La máquina se enciende bajo demanda: si la URL no responde, está apagada. Las pruebas de humo y las capturas están en la [sección 5 del documento de despliegue](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/ES/MD/documento-de-despliegue.md#5-plan-de-verificación-pruebas-y-evidencias-smoke-tests). Las credenciales se entregan por un canal privado (ver la sección 7). |
| 12 | Trazabilidad e integración de evidencias | Relación entre requisitos, HU, módulos, pruebas y versiones | [Matriz de trazabilidad (SRS §10)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/ES/MD/informe-de-especificacion-de-requisitos.md#10-matriz-de-trazabilidad) · [Trazabilidad requisitos–pruebas (§5)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/06_DOCUMENTACION_DE_PRUEBAS/ES/MD/documentacion-de-pruebas.md#5-matriz-de-trazabilidad) · Fuente en `vehicle-w-docs`: [Matriz de trazabilidad](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/traceability-matrix.md) | Público / Pendiente de permisos (`vehicle-w-docs`) | No hay release tags, así que la trazabilidad hacia las versiones se hace por rama (`develop`) y por commit. |

---

## 2. Repositorios de código fuente

Estado al 24/10/2026, tomado con `gh api`: la versión **`v1.0.0`** existe en 9 repositorios y su `main` es esa versión (payment-service desde el 24/10/2026, con su PR #2 fusionado); **la app móvil todavía no tiene versión** (PR #1 «Release v1.1.0» abierto) y se evalúa en `develop`. Después de la etiqueta, `develop` volvió a avanzar con los arreglos del 23 y del 24/10/2026 (columna «`develop` adelante»), que saldrán en `v1.1.0`; ese `develop` es lo que corre en el servidor público desde el 24/10/2026.

| Componente | Tecnología | Repositorio | Versión | `main` | `develop` (último commit) | `develop` adelante de `main` | Acceso |
|---|---|---|---|---|---|---|---|
| Frontend web | Angular | [Front-end-proyecto-web](https://github.com/BrayanCABRERA123/Front-end-proyecto-web) | [`v1.0.0`](https://github.com/BrayanCABRERA123/Front-end-proyecto-web/tree/v1.0.0) | `d699e92` (= `v1.0.0`) | `ba2c93a` | 66 commits | Público |
| Aplicación móvil | React Native (Expo) | [LavadoVehicular-Movil](https://github.com/merari0322/LavadoVehicular-Movil) | Sin versión (PR #1 «Release v1.1.0» abierto) | `a416aa7` (06/07/2026) | `e5d7d67` | 294 commits | Público |
| API Gateway | Spring Boot | [lavarapido-api-gateway](https://github.com/BrayanCABRERA123/lavarapido-api-gateway) | [`v1.0.0`](https://github.com/BrayanCABRERA123/lavarapido-api-gateway/tree/v1.0.0) | `016e239` (= `v1.0.0`) | `c8b607a` | 18 commits | Público |
| Seguridad (autenticación, JWT, roles) | Spring Boot | [lavarapido-security-service](https://github.com/BrayanCABRERA123/lavarapido-security-service) | [`v1.0.0`](https://github.com/BrayanCABRERA123/lavarapido-security-service/tree/v1.0.0) | `a64cc5c` (= `v1.0.0`) | `b5fe56e` | 32 commits | Público |
| Clientes y vehículos | Spring Boot | [lavarapido-customer-service](https://github.com/camiloguilombo12/lavarapido-customer-service) | [`v1.0.0`](https://github.com/camiloguilombo12/lavarapido-customer-service/tree/v1.0.0) | `b819d4f` (= `v1.0.0`) | `3181cae` | 18 commits | Público |
| Catálogo y reservas | Spring Boot | [lavarapido-booking-service](https://github.com/camiloguilombo12/lavarapido-booking-service) | [`v1.0.0`](https://github.com/camiloguilombo12/lavarapido-booking-service/tree/v1.0.0) | `938223b` (= `v1.0.0`) | `5dd6794` | 40 commits | Público |
| Operación (operarios y bahías) | Spring Boot | [lavarapido-operation-service](https://github.com/BrayanCABRERA123/lavarapido-operation-service) | [`v1.0.0`](https://github.com/BrayanCABRERA123/lavarapido-operation-service/tree/v1.0.0) | `19ce32e` (= `v1.0.0`) | `37e32ff` | 40 commits | Público |
| Pagos y fidelización | .NET Core | [lavarapido-payment-service](https://github.com/merari0322/lavarapido-payment-service) | [`v1.0.0`](https://github.com/merari0322/lavarapido-payment-service/tree/v1.0.0) | `2deac9e` (= `v1.0.0`, PR #2 fusionado el 24/10/2026) | `3b8730e` | 0 commits (`main` lo incluye) | Público |
| Notificaciones | Spring Boot | [lavarapido-notification-service](https://github.com/BrayanCABRERA123/lavarapido-notification-service) | [`v1.0.0`](https://github.com/BrayanCABRERA123/lavarapido-notification-service/tree/v1.0.0) | `2ead588` (= `v1.0.0`) | `c5429ad` | 22 commits | Público |
| Infraestructura (Docker, base de datos, pruebas E2E) | Docker, SQL Server, RabbitMQ | [lavarapido-infra](https://github.com/BrayanCABRERA123/lavarapido-infra) | [`v1.0.0`](https://github.com/BrayanCABRERA123/lavarapido-infra/tree/v1.0.0) | `a19c6cb` (= `v1.0.0`) | `cf28ed0` | 61 commits | Público |
| Documentación técnica (SDD) | Markdown, OpenAPI | [vehicle-w-docs](https://github.com/code-sena/vehicle-w-docs/tree/docs) (rama `docs`) | — | 366 commits atrás de `docs` | `9d5ba51` (rama `docs`, 21/10/2026) | — | Pendiente de permisos |
| Evidencias documentales | Markdown | [lavarapido-docs](https://github.com/BrayanCABRERA123/lavarapido-docs) (rama `main`) | — | rama de trabajo | — | — | Público |

**Base de datos:** una sola base `LavaRapido` en SQL Server 2022 (Express en producción y Developer en local), con un esquema por servicio (ADR-003, ADR-009). Cada servicio Spring Boot gestiona sus migraciones con Liquibase. Las migraciones del servicio de pagos están en [`lavarapido-payment-service/db`](https://github.com/merari0322/lavarapido-payment-service/tree/develop/db).

> Recomendación: indicar al evaluador que la versión entregada es `v1.0.0` (rama `main`) y que lo más reciente está en `develop`; en la app móvil, revisar `develop` hasta que tenga su versión (acción ACO-24 del documento de Acciones Correctivas).

---

## 3. Despliegue y verificación técnica

| Aspecto | Valor |
|---|---|
| Versión (release tag) | `v1.0.0`, creada el 23/10/2026 en 8 repositorios (sección 2); payment-service la tiene desde el 24/10/2026 (PR #2 fusionado) y la app móvil todavía no (PR #1 abierto). Los arreglos del 23/10/2026 y las 128 ramas del 24/10/2026 están en `develop` para `v1.1.0` |
| Entorno | Producción académica en Azure (VM Ubuntu 24.04, Docker Compose con `docker-compose.prod.yml`), desplegada el 16/10/2026 y actualizada por última vez el 24/10/2026 con el código de `develop` de ese día (dos corridas por SSH; 11 contenedores sanos, migraciones 044, 045, 113, 047, 116, 022 y 023 aplicadas y 0 errores en los registros), con imágenes `:prev` para volver atrás con `rollback.sh` y la protección que impide bajar de versión. Hasta liberar `v1.1.0` el servidor se actualiza con `BRANCH=develop`. Para desarrollo: local con Docker (`docker compose --profile app up -d --build` desde `lavarapido-infra`). Detalle en el [documento de despliegue](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/ES/MD/documento-de-despliegue.md). |
| Entorno de demostración público | https://lavarapidovehicular.northcentralus.cloudapp.azure.com |
| Despliegue continuo | Fusionado en `develop` el 24/10/2026 (cada fusión aprobada a `main` desplegará sola y, al encender la máquina, se desplegará lo pendiente; la app móvil publica su actualización por internet con `cd.yml`), pero **todavía no ha corrido solo**: faltan los secretos de GitHub (`AZURE_SSH_KEY`, `DEPLOY_DISPATCH_TOKEN` y `EXPO_TOKEN`) y llega a `main` con `v1.1.0`. Hoy se despliega con `update-server.sh` por SSH. Detalle en el [documento de despliegue, sección 4.3.4](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/ES/MD/documento-de-despliegue.md) |

### 3.1 Matriz de roles

| Rol | Funciones principales | Cliente donde se usa |
|---|---|---|
| Administrador | Usuarios y roles, catálogo, promociones, horarios y bahías, operarios, reservas, informe de inspección, pagos, reportes | Web y móvil |
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
| Flujo E2E automatizado | `node --test "e2e/*.test.js"` en `lavarapido-infra` (con `E2E_OPERATOR_ID=2` en la base local) | 19 de 19 pruebas aprobadas en 11,2 s (19/10/2026); el 21/10/2026 pasaron de nuevo las 19 en la madrugada y en la noche, con el chequeo de sesión del gateway activo |

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

Estado al 23/10/2026; las casillas sin marcar tienen su responsable.

- [ ] Todos los enlaces abren correctamente, sin errores 404 ni accesos denegados, probados desde una cuenta que no pertenezca al equipo. *Pendiente de probar con una cuenta ajena (Brayan Cabrera). Los enlaces internos de los 31 Markdown se revisaron el 23/10/2026 y el único roto, en el Manual de Administrador, se corrigió.*
- [ ] El instructor tiene permiso de lectura en `code-sena/vehicle-w-docs` (privado) y lo comprobó con su cuenta. *Pendiente (Brayan Cabrera); además, `main` de ese repositorio va 366 commits atrás de `docs`.*
- [ ] Cada evidencia de `lavarapido-docs` tiene su Markdown, PDF y Word en ES y EN, y los PDF y Word abren correctamente. *Los Markdown están al 24/10/2026; los PDF y Word de los documentos cambiados el 23 y el 24 de octubre, y los de la propuesta técnica (03), quedan por regenerar con el generador del equipo.*
- [x] Los documentos son legibles: el Markdown se renderiza en GitHub y los PDF abren sin errores. *Comprobado en la versión del 21/10/2026; repetir al regenerar.*
- [ ] Cada repositorio identifica el proyecto (README), la rama evaluada (`develop`) y la versión (release tag). *`v1.0.0` en 9 de 10 repositorios (payment-service desde el 24/10/2026); falta la app móvil, con el PR #1 abierto (Merari Urbano).*
- [ ] La documentación, los repositorios y la aplicación son coherentes: lo que describen el SRS y los manuales existe en el código de `develop`. *Parcial: el SRS v8.0 marca 3 RF y 9 RNF como parciales y el documento de Acciones Correctivas registra lo que sigue abierto (16 acciones, ninguna P0 ni P1).*
- [ ] No se presentan simulaciones (mocks, `json-server`, datos de ejemplo) como funcionalidades reales. *Desde el 24/10/2026 la app y la web ya no muestran los datos de ejemplo de la sede (la semilla 113 los borra de la base); los textos legales de la app todavía dicen "Express Car Wash S.A.S." (decisión del equipo).*
- [ ] No hay credenciales ni datos sensibles: `.env` no está versionado (solo `.env.example`) y no hay tokens ni contraseñas en el historial. *Parcial: ver el criterio de seguridad de la sección 5.*
- [ ] El PDF exportado conserva los enlaces activos (hacer clic en al menos uno por sección). *Pendiente al regenerar el PDF (Brayan Cabrera).*

---

## 5. Criterios de aceptación

| Criterio | Condición de cumplimiento | Resultado / observaciones |
|---|---|---|
| Completitud | Las 12 evidencias tienen un enlace directo y verificable | Las 12 evidencias tienen enlace. La evidencia 11 enlaza la aplicación desplegada en Azure desde el 16/10/2026. |
| Accesibilidad | Todos los enlaces abren para el instructor sin solicitar permisos | Parcial: los enlaces de `lavarapido-docs` y de los repositorios de código son públicos (comprobado sin iniciar sesión); los de `vehicle-w-docs` requieren dar permiso de lectura al instructor. |
| Trazabilidad | Requisitos → HU → módulos → pruebas → versiones relacionados | Existe una matriz en la §10 del SRS (v8.0, con los requisitos parciales marcados), otra en la §5 del documento de pruebas y la matriz fuente en `vehicle-w-docs`. La versión `v1.0.0` existe en 9 de 10 repositorios. |
| Coherencia | La documentación coincide con el código y con la aplicación en ejecución | Último CI de `develop` del 24/10/2026: 1 119 pruebas automatizadas y 73 de la app móvil (1 192), todas aprobadas; ese mismo código corre en el servidor público desde ese día. El 23/10/2026 eran 838. Pruebas del 21/10/2026 (ejecución final, en la noche): 707 automatizadas y 19 de punta a punta aprobadas; en la madrugada fueron 689. Ese día también se comprobó en vivo la lista "Por cerrar" del administrador en la web y en la app móvil. Entorno local verificado el 19/10/2026: todos los servicios `UP`, 42 casos funcionales aprobados, diseño adaptable verificado en 66 pantallas web y 15 de la app, y capturas de los manuales, del SRS, del análisis y del diseño tomadas de nuevo ese día. |
| Seguridad | Sin secretos ni datos personales expuestos | Parcial (revisado el 24/10/2026): ningún repositorio versiona `.env` y estos documentos no traen contraseñas. En `develop` las contraseñas de desarrollo salieron del código, del compose, de los README y, desde el 24/10/2026, de `GUIA-EQUIPO.md` y de los argumentos de `payment-migrate`, pero quedan: la contraseña de desarrollo de `sa` en `.env.example` de `main` (`v1.0.0`) de `lavarapido-infra` hasta liberar `v1.1.0`, la contraseña antigua de SQL Server en el historial de Git y en `main` de payment-service y la clave de Firebase en `google-services.json` de la app (acción ACO-25). Las capturas usan datos de prueba. |
| Presentación | Documento navegable, tablas legibles y PDF con enlaces activos | Pendiente: el equipo regenera el PDF con su generador APA 7 y comprueba un enlace por sección (responsable: Brayan Cabrera). |

---

## 6. Entrega

| Formato | Nombre sugerido |
|---|---|
| Markdown | `11_ENLACES_DE_EVIDENCIAS/ES/MD/Enlaces_Evidencias_Proyecto_VehicleWashing.md` (en inglés: `EN/MD/Evidence_Links_Project_VehicleWashing.md`) |
| PDF | `11_ENLACES_DE_EVIDENCIAS/ES/PDF/Enlaces_Evidencias_Proyecto_VehicleWashing.pdf`; para entregar, copiarlo con la fecha, por ejemplo `Enlaces_Evidencias_Proyecto_VehicleWashing_2026-10-17.pdf` |

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
