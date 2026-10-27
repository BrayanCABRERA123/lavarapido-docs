# Evidence Links of the Training Project — LavaRápido (Vehicle Washing)

**Web and mobile booking and management platform for a car wash**

| Field | Value |
|---|---|
| Program / group | Technologist in Software Analysis and Development (ADSO), group 3145556 |
| Center | Centro de la Industria, la Empresa y los Servicios — SENA, Huila Region |
| Training project | Vehicle Washing Management System (Vehicle Washing / LavaRápido), as it appears on the cover of the deliverables. To be confirmed with the instructor whether the ficha records it under another name (owner: Brayan Cabrera) |
| Work team | Vehicle Washing Development Team (team 8 in the instructor's evaluation of 10/21/2026) |
| Members | Juan Camilo Guilombo Osorio, Brayan Estiven Patiño Cabrera, Merari Urbano Quintero |
| Instructor | Karol Daniela Correa |
| Delivery date | Final presentation planned for the week of October 27, 2026; the instructor confirms the exact date (owner of confirming it: Brayan Cabrera) |
| Last update of this document | October 27, 2026 |

---

## Contents

1. [Evidence matrix](#1-evidence-matrix)
2. [Source code repositories](#2-source-code-repositories)
3. [Deployment and technical verification](#3-deployment-and-technical-verification)
4. [Accessibility and quality checklist](#4-accessibility-and-quality-checklist)
5. [Acceptance criteria](#5-acceptance-criteria)
6. [Delivery](#6-delivery)
7. [Security note](#7-security-note)
8. [Reference resources](#8-reference-resources)
9. [Reminder for the team](#9-reminder-for-the-team)

---

## 1. Evidence Matrix

**Documentation repositories used in the matrix**

- **`lavarapido-docs`** (public, `main` branch): https://github.com/BrayanCABRERA123/lavarapido-docs
- **`vehicle-w-docs`** (private, `code-sena` organization, `docs` branch): https://github.com/code-sena/vehicle-w-docs/tree/docs. It is the source technical documentation of the project (SDD); the documents in `lavarapido-docs` are derived from it. Each evidence links the equivalent public section first, so there is always an accessible link.

Structure of `lavarapido-docs`: the [general index (README)](https://github.com/BrayanCABRERA123/lavarapido-docs#readme) links every evidence and the [change history (CHANGELOG)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/CHANGELOG.md) records each version. Each evidence has a numbered folder (`01_` to `11_`) and, inside it, `ES/` and `EN/`, each with `MD/` (Markdown and its `capturas/` screenshots), `PDF/`, and `WORD/`; the article (10) is bilingual in a single file, and this matrix (11) has Markdown and PDF. The matrix links the English Markdown version; the PDF and Word files are in the neighboring folders.

| # | Evidence | Minimum verifiable content | Direct link | Access status | Remarks |
|---|---|---|---|---|---|
| 1 | Requirements specification report | Functional and non-functional requirements, user stories, acceptance criteria, traceability | [SRS v8.0 (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/EN/MD/requirements-specification-report.md) · [Functional requirements (SRS §5)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/EN/MD/requirements-specification-report.md#5-functional-requirements) · [Non-functional requirements (SRS §6)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/EN/MD/requirements-specification-report.md#6-non-functional-requirements) · [User stories per requirement (SRS §10)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/EN/MD/requirements-specification-report.md#10-traceability-matrix) · Source in `vehicle-w-docs`: [Functional requirements](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/functional.md) · [Non-functional requirements](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/non-functional.md) · [User stories](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/user-stories.md) | Public / Pending permissions (`vehicle-w-docs`) | The SRS follows IEEE 830 and ISO/IEC/IEEE 29148 and covers 41 functional requirements (RF-001 to RF-038) and use cases CU01 to CU32. Spanish version: `01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/ES/`. |
| 2 | Software analysis | Dynamic views, processes, use cases, sequence and state diagrams | [Dynamic views analysis (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/02_DOCUMENTACION_DE_ANALISIS_DEL_SOFTWARE/EN/MD/software-analysis-documentation.md) · [Sequence, activity, and state diagrams](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/02_DOCUMENTACION_DE_ANALISIS_DEL_SOFTWARE/EN/MD/software-analysis-documentation.md#2-sequence-diagrams) · Source in `vehicle-w-docs`: [UML diagrams (sources)](https://github.com/code-sena/vehicle-w-docs/tree/docs/08-uml/diagrams/source) | Public / Pending permissions (`vehicle-w-docs`) | The screenshots are in `02_DOCUMENTACION_DE_ANALISIS_DEL_SOFTWARE/EN/MD/capturas/`. The diagrams include the booking, payment, registration, reminder, assignment, and inspection sequences, and the booking and payment states. |
| 3 | Technical proposal of the software | Selected alternative, technologies, justification, scope, and constraints | [Technical proposal (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/03_PROPUESTA_TECNICA_DEL_SOFTWARE/EN/MD/software-technical-proposal.md) · [Design decisions (SRS §3.6)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/EN/MD/requirements-specification-report.md#36-design-decisions) · [Alternatives considered](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/03_PROPUESTA_TECNICA_DEL_SOFTWARE/EN/MD/software-technical-proposal.md#3-alternatives-considered) · Source in `vehicle-w-docs`: [Architecture decisions (ADR-001 to ADR-015)](https://github.com/code-sena/vehicle-w-docs/tree/docs/05-architecture/decisions/records) | Public / Pending permissions (`vehicle-w-docs`) | The ADRs justify the microservices architecture, the database, the API Gateway, JWT, and the use of .NET for the payment service. |
| 4 | Software design | Graphical interfaces, architecture, patterns, data model, and diagrams | [Software design (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/04_DOCUMENTACION_DE_DISENO_DEL_SOFTWARE/EN/MD/software-design-documentation.md) · [Architectural model](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/04_DOCUMENTACION_DE_DISENO_DEL_SOFTWARE/EN/MD/software-design-documentation.md#3-architectural-model) · [Data model](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/04_DOCUMENTACION_DE_DISENO_DEL_SOFTWARE/EN/MD/software-design-documentation.md#5-data-model) · [API and system routes (technical manual §13)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/EN/MD/technical-manual.md#13-api-or-system-routes) · Source in `vehicle-w-docs`: [Architecture](https://github.com/code-sena/vehicle-w-docs/tree/docs/05-architecture) · [Data model](https://github.com/code-sena/vehicle-w-docs/tree/docs/06-data) · [OpenAPI contracts](https://github.com/code-sena/vehicle-w-docs/tree/docs/07-api/contracts/openapi) | Public / Pending permissions (`vehicle-w-docs`) | Hexagonal architecture pattern (ADR-007). Section 2.5 describes the responsive design. The screenshots are in `04_DOCUMENTACION_DE_DISENO_DEL_SOFTWARE/EN/MD/capturas/`. |
| 5 | Source code and software artifacts | Repositories of the web frontend, mobile app, backend, infrastructure, and database, with their branches | [Code artifacts (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/05_ARTEFACTOS_DE_CODIGO/EN/MD/code-artifacts.md) · see [section 2](#2-source-code-repositories) | Public | The integration branch is `develop`. `main` is behind in every repository (see section 2). |
| 6 | Test documentation | Plan, test cases, results, execution evidence, defects, and fixes | [Test documentation (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/06_DOCUMENTACION_DE_PRUEBAS/EN/MD/test-documentation.md) · [E2E tests](https://github.com/BrayanCABRERA123/lavarapido-infra/tree/develop/e2e) · [Test plan](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/06_DOCUMENTACION_DE_PRUEBAS/EN/MD/test-documentation.md#1-test-plan) · Source in `vehicle-w-docs`: [Testing strategy](https://github.com/code-sena/vehicle-w-docs/blob/docs/11-quality/testing-strategy.md) | Public / Pending permissions (`vehicle-w-docs`) | Follows ISO/IEC/IEEE 29119-3. Automated (689) and end-to-end (19) tests run on 10/21/2026; functional (42), performance, and responsive design tests on 10/19/2026 (§3). The traceability matrix is in §5 and the findings in §6. |
| 7 | Implementation procedure | Reproducible installation, configuration, deployment, and verification | [Implementation procedure (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/EN/MD/implementation-procedure.md) · [Azure deployment document (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/EN/MD/deployment-document.md) · Support: [Infrastructure README](https://github.com/BrayanCABRERA123/lavarapido-infra/blob/develop/README.md) · [Team guide](https://github.com/BrayanCABRERA123/lavarapido-infra/blob/develop/GUIA-EQUIPO.md) | Public | Available in Markdown, PDF, and Word (ES and EN) in `07_PROCEDIMIENTO_DE_IMPLEMENTACION/`. The deployment document records the deployment of 10/16/2026 on Azure with its evidence screenshots. |
| 8 | Corrective, preventive, and improvement actions | Findings, priority, owner, applied action, and closing evidence | [Corrective, preventive, and improvement actions (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/08_ACCIONES_CORRECTIVAS_PREVENTIVAS_Y_DE_MEJORA/EN/MD/corrective-preventive-and-improvement-actions.md) · Support: [Preventive actions](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/08_ACCIONES_CORRECTIVAS_PREVENTIVAS_Y_DE_MEJORA/EN/MD/corrective-preventive-and-improvement-actions.md#11-register-of-preventive-actions) · [Traceability between actions, risks, and technical debt](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/08_ACCIONES_CORRECTIVAS_PREVENTIVAS_Y_DE_MEJORA/EN/MD/corrective-preventive-and-improvement-actions.md#annex-c-traceability-between-actions-risks-and-technical-debt) · Source in `vehicle-w-docs`: [Risks](https://github.com/code-sena/vehicle-w-docs/blob/docs/15-project-control/risks.md) · [Technical backlog](https://github.com/code-sena/vehicle-w-docs/blob/docs/15-project-control/technical-backlog.md) | Public / Pending permissions (`vehicle-w-docs`) | Available in Markdown, PDF, and Word (ES and EN) in `08_ACCIONES_CORRECTIVAS_PREVENTIVAS_Y_DE_MEJORA/`. |
| 9 | Technical, installation, and user manuals | Prerequisites, configuration, use, and troubleshooting | [Technical manual (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/EN/MD/technical-manual.md) · [Installation manual (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/EN/MD/installation-manual.md) · [User manual (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/EN/MD/user-manual.md) · [Customer user manual (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/EN/MD/customer-user-manual.md) · [Operator user manual (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/EN/MD/operator-user-manual.md) · [Administrator manual (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/EN/MD/administrator-manual.md) · [PDF of the manuals](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/09_MANUALES/EN/PDF) · Source in `vehicle-w-docs`: [User manual](https://github.com/code-sena/vehicle-w-docs/blob/docs/14-training/user-manual.md) | Public / Pending permissions (`vehicle-w-docs`) | Each manual is in Markdown, PDF, and Word (ES and EN), in the `09_MANUALES/` folder. Six manuals: technical, installation, administrator, user (customer and operator together) and, since 10/26/2026, one user manual per role (customer and operator, version 1.0), as the SENA manuals guide recommends. All have real screenshots of the system; the `.env` secrets appear masked. |
| 10 | Project article | Problem, objectives, solution, methodology, results, and conclusions | [APA 7 article (ES/EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/10_ARTICULO_DEL_PROYECTO/MD/articulo-del-proyecto-apa7.md) · [APA 7 PDF](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/10_ARTICULO_DEL_PROYECTO/PDF/10_Articulo_Del_Proyecto_APA7.pdf) · [IEEE version](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/10_ARTICULO_DEL_PROYECTO/PDF/10_Articulo_Del_Proyecto_IEEE.pdf) · [ACM version](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/10_ARTICULO_DEL_PROYECTO/PDF/10_Articulo_Del_Proyecto_ACM.pdf) | Public | The three versions (APA 7, IEEE, and ACM) are in Markdown, PDF, and Word in the `10_ARTICULO_DEL_PROYECTO/` folder. Each file is bilingual (ES and EN in the same document), which is why this folder is not split by language. |
| 11 | Deployed application or demo | Access URL or demo environment and verification instructions | [Application in production](https://lavarapidovehicular.northcentralus.cloudapp.azure.com) · [Android app download](https://lavarapidovehicular.northcentralus.cloudapp.azure.com/app/LavaRapidoVehicular.apk) · [Deployment document (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/EN/MD/deployment-document.md) | Public | Deployed on 10/16/2026 on an Azure virtual machine (Docker Compose, Caddy with Let's Encrypt HTTPS) and last updated on 10/22/2026 with the changes of 10/21/2026 (migrations 112, 040, and 041). The machine is turned on on demand: if the URL does not answer, it is off. The smoke tests and screenshots are in [section 5 of the deployment document](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/EN/MD/deployment-document.md#5-verification-testing-and-evidence-plan-smoke-tests). The credentials are delivered through a private channel (see section 7). |
| 12 | Traceability and integration of evidence | Relationship between requirements, user stories, modules, tests, and versions | [Traceability matrix (SRS §10)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/EN/MD/requirements-specification-report.md#10-traceability-matrix) · [Requirements–tests traceability (§5)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/06_DOCUMENTACION_DE_PRUEBAS/EN/MD/test-documentation.md#5-traceability-matrix) · Source in `vehicle-w-docs`: [Traceability matrix](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/traceability-matrix.md) | Public / Pending permissions (`vehicle-w-docs`) | There are no release tags, so traceability to versions is done by branch (`develop`) and by commit. |

---

## 2. Source Code Repositories

Status as of 10/27/2026, taken from the repositories: on 10/27/2026 **`v1.1.2`** of the web, the mobile app, payment-service, and infra and **`v1.1.1`** of customer-service and booking-service shipped, and payment-service **`v1.1.3`** was approved (PR #16, pending publication: that is why its `develop` is ahead). on 10/26/2026 **`v1.1.0`** shipped in the 10 repositories (the mobile app got its first version) and that same day **`v1.1.1`** in the web, the mobile app, payment-service, and infra (terms and conditions in the third person with the inspection report section, test counts, and payment-service deployed from `main`). In all of them, `main` is the latest tag and `develop` has no pending code changes (the "`develop` ahead" column only counts commits that are not in `main`). The previous version, `v1.0.0`, is from 10/23/2026 (10/24/2026 in payment-service).

| Component | Technology | Repository | Version | `main` | `develop` (last commit) | `develop` ahead of `main` | Access |
|---|---|---|---|---|---|---|---|
| Web frontend | Angular | [Front-end-proyecto-web](https://github.com/BrayanCABRERA123/Front-end-proyecto-web) | [`v1.1.2`](https://github.com/BrayanCABRERA123/Front-end-proyecto-web/tree/v1.1.2) | `acea5e3` (= `v1.1.2`) | `f25d407` | 0 commits (`main` includes it) | Public |
| Mobile app | React Native (Expo) | [LavadoVehicular-Movil](https://github.com/merari0322/LavadoVehicular-Movil) | [`v1.1.2`](https://github.com/merari0322/LavadoVehicular-Movil/tree/v1.1.2) | `f8300d6` (= `v1.1.2`) | `f8300d6` | 0 commits (`main` includes it) | Public |
| API Gateway | Spring Boot | [lavarapido-api-gateway](https://github.com/BrayanCABRERA123/lavarapido-api-gateway) | [`v1.1.0`](https://github.com/BrayanCABRERA123/lavarapido-api-gateway/tree/v1.1.0) | `6961feb` (= `v1.1.0`) | `97dbf39` | 0 commits (`main` includes it) | Public |
| Security (authentication, JWT, roles) | Spring Boot | [lavarapido-security-service](https://github.com/BrayanCABRERA123/lavarapido-security-service) | [`v1.1.0`](https://github.com/BrayanCABRERA123/lavarapido-security-service/tree/v1.1.0) | `391fb1f` (= `v1.1.0`) | `0a664a9` | 0 commits (`main` includes it) | Public |
| Customers and vehicles | Spring Boot | [lavarapido-customer-service](https://github.com/camiloguilombo12/lavarapido-customer-service) | [`v1.1.1`](https://github.com/camiloguilombo12/lavarapido-customer-service/tree/v1.1.1) | `83d322e` (= `v1.1.1`) | `83d322e` | 0 commits (`main` includes it) | Public |
| Catalog and bookings | Spring Boot | [lavarapido-booking-service](https://github.com/camiloguilombo12/lavarapido-booking-service) | [`v1.1.1`](https://github.com/camiloguilombo12/lavarapido-booking-service/tree/v1.1.1) | `506feca` (= `v1.1.1`) | `506feca` | 0 commits (`main` includes it) | Public |
| Operations (operators and bays) | Spring Boot | [lavarapido-operation-service](https://github.com/BrayanCABRERA123/lavarapido-operation-service) | [`v1.1.0`](https://github.com/BrayanCABRERA123/lavarapido-operation-service/tree/v1.1.0) | `9511328` (= `v1.1.0`) | `15ff0f4` | 0 commits (`main` includes it) | Public |
| Payments and loyalty | .NET Core | [lavarapido-payment-service](https://github.com/merari0322/lavarapido-payment-service) | [`v1.1.2`](https://github.com/merari0322/lavarapido-payment-service/tree/v1.1.2) | `42dac3d` (= `v1.1.2`) | `4ccc52e` | 10 commits (`v1.1.3` approved in PR #16, pending publication) | Public |
| Notifications | Spring Boot | [lavarapido-notification-service](https://github.com/BrayanCABRERA123/lavarapido-notification-service) | [`v1.1.0`](https://github.com/BrayanCABRERA123/lavarapido-notification-service/tree/v1.1.0) | `7fdfd1e` (= `v1.1.0`) | `fd8eec7` | 0 commits (`main` includes it) | Public |
| Infrastructure (Docker, database, E2E tests) | Docker, SQL Server, RabbitMQ | [lavarapido-infra](https://github.com/BrayanCABRERA123/lavarapido-infra) | [`v1.1.2`](https://github.com/BrayanCABRERA123/lavarapido-infra/tree/v1.1.2) | `682f629` (= `v1.1.2`) | `682f629` | 0 commits (`main` includes it) | Public |
| Technical documentation (SDD) | Markdown, OpenAPI | [vehicle-w-docs](https://github.com/code-sena/vehicle-w-docs/tree/docs) (`docs` branch) | — | 483 commits behind `docs` | `ba7dde6` (`docs` branch, 10/27/2026) | — | Pending permissions |
| Documentary evidence | Markdown | [lavarapido-docs](https://github.com/BrayanCABRERA123/lavarapido-docs) (`main` branch) | — | working branch | — | — | Public |

**Database:** a single `LavaRapido` database on SQL Server 2022 (Express in production and Developer locally), with one schema per service (ADR-003, ADR-009). Each Spring Boot service manages its migrations with Liquibase. The payment service migrations are in [`lavarapido-payment-service/db`](https://github.com/merari0322/lavarapido-payment-service/tree/develop/db).

> Recommendation: tell the evaluator that the delivered version is the latest tag of each repository on `main` (`v1.1.1` in the web, the mobile app, payment-service, and infra, and `v1.1.0` in the others); `develop` has the same code.

---

## 3. Deployment and Technical Verification

| Aspect | Value |
|---|---|
| Version (release tag) | `v1.1.2` of the web, the mobile app, payment-service, and infra and `v1.1.1` of customer-service and booking-service (10/27/2026); `v1.1.0` in api-gateway, security, operations, and notification (10/26/2026). payment-service `v1.1.3` approved and pending publication (section 2). The first version, `v1.0.0`, is from 10/23/2026 |
| Environment | Academic production on Azure (Ubuntu 24.04 VM, Docker Compose with `docker-compose.prod.yml`), deployed on 10/16/2026 and last updated on 10/24/2026 with that day's `develop` code (two runs over SSH; 11 healthy containers, migrations 044, 045, 113, 047, 116, 022, and 023 applied, and 0 errors in the logs), with `:prev` images to go back with `rollback.sh` and the protection that prevents downgrading. Until `v1.1.0` (10/26/2026) the server was updated with `BRANCH=develop`; since `lavarapido-infra` `v1.1.1`, `setup-server.sh` pulls `main` in every repository, payment-service included. For development: local with Docker (`docker compose --profile app up -d --build` from `lavarapido-infra`). Details in the [deployment document](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/EN/MD/deployment-document.md). |
| Public demo environment | https://lavarapidovehicular.northcentralus.cloudapp.azure.com |
| Continuous deployment | Active since 10/26/2026: with the secrets created, merging "Release v1.1.1" into `main` of `lavarapido-infra` deployed on its own at 22:19 (Colombia time) and the requests from the other repositories kept coming until 22:48, all green (healthy services and web and API at 200); payment-service is also deployed from `main`. In the mobile app, APK `versionCode` 6 and the over-the-air update were published after checking that the native fingerprint matched. Details in the [deployment document, sections 1.3.12 and 4.3.4](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/EN/MD/deployment-document.md) |

### 3.1 Role Matrix

| Role | Main functions | Client where it is used |
|---|---|---|
| Administrator | Users and roles, catalog, promotions, schedules and bays, operators, bookings, inspection report, payments, reports | Web and mobile |
| Customer | Registration, vehicles, bookings, payments by QR or transfer, history, ratings, notifications | Web and mobile |
| Operator | Assigned services, schedule, execution, history, ratings received | Web and mobile |

### 3.2 Health Endpoints (verified on 10/16/2026 in the local environment)

| Service | Port | Endpoint | Result |
|---|---|---|---|
| API Gateway | 8080 | `/actuator/health` | `UP` |
| security-service | 3001 | `/actuator/health` | `UP` |
| customer-service | 3002 | `/actuator/health` | `UP` |
| booking-service | 3003 | `/actuator/health` | `UP` |
| operations-service | 3004 | `/actuator/health` | `UP` |
| payment-service | 3005 | `/health` | `ok` (checks SQL Server; answers 503 when the database does not respond) |
| notification-service | 3006 | `/actuator/health` | `UP` |

### 3.3 Interactive API Documentation (Swagger/OpenAPI)

- **Spring Boot services (ports 3001–3004 and 3006):** `http://localhost:<port>/swagger-ui/index.html` answered `200` on 10/16/2026.
- **payment-service (.NET Core):** Swagger is only enabled in the `Development` environment. Under Docker it is not exposed (`404`). To see it, run the service with `ASPNETCORE_ENVIRONMENT=Development`.
- **Versioned contracts:** [`07-api/contracts/openapi`](https://github.com/code-sena/vehicle-w-docs/tree/docs/07-api/contracts/openapi) in `vehicle-w-docs` (private). Public version: [API and system routes](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/EN/MD/technical-manual.md#13-api-or-system-routes), in the technical manual.

### 3.4 Smoke Tests

| Test | Procedure | Result |
|---|---|---|
| Authentication | `POST http://localhost:8080/api/v1/auth/login` with a test user and check that it returns a JWT | 200 with `accessToken` (10/16/2026, test account of the *dev* profile) |
| Read | With the JWT, query the service catalog or the customer's bookings | `GET /api/v1/catalog/services` and `GET /api/v1/bookings/me` answered 200 (10/16/2026) |
| Write | Create a booking and check that it appears in the history and that the notification arrives | Covered by `full-flow.test.js`: booking created, automatically assigned to the chosen operator, payment approved, service started and finished, rating, and every notice in the customer inbox (10/16/2026) |
| Automated E2E flow | `node --test "e2e/*.test.js"` in `lavarapido-infra` (with `E2E_OPERATOR_ID=2` in the local database) | 19 of 19 tests passed in 11.2 s (10/19/2026); on 10/21/2026 all 19 passed again in the early morning and in the evening, with the gateway session check on |

### 3.5 Evidence Screenshots

| Screenshot | Description | Link |
|---|---|---|
| Web screens (login, admin, customer, operator) | 28 interface screenshots | [SRS `capturas` folder](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/EN/MD/capturas) |
| Dynamic views and modals | 41 screenshots | [Analysis `capturas` folder](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/02_DOCUMENTACION_DE_ANALISIS_DEL_SOFTWARE/EN/MD/capturas) |
| Design (landing, login, booking, payments) | Screenshots of the final design | [`capturas` folder](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/04_DOCUMENTACION_DE_DISENO_DEL_SOFTWARE/EN/MD/capturas) |
| Real screenshots of the manuals | 110 screenshots per language of the running system (10/16, 10/19, 10/26, and 10/27/2026): screens of the three roles on the web and of the customer and operator in the mobile app (the customer and operator ones also with the `customer-*` and `operator-*` names of the role manuals), installation terminal, and data model diagram | [Manuals `capturas` folder](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/09_MANUALES/EN/MD/capturas) |
| Containers, logs, health checks, and migrations in production | Portainer, startup logs, `/actuator/health`, clean console, and Liquibase changesets (10/16/2026) | [Deployment `capturas` folder](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/EN/MD/capturas) |

---

## 4. Accessibility and Quality Checklist

Status as of 10/23/2026; unchecked boxes have their owner.

- [ ] Every link opens correctly, without 404 errors or denied access, tested from an account outside the team. *To be tested with an outside account (Brayan Cabrera). The internal links of the 31 Markdown files were reviewed on 10/23/2026 and the only broken one, in the Administrator Manual, was fixed.*
- [ ] The instructor has read permission on `code-sena/vehicle-w-docs` (private) and checked it with their account. *Pending (Brayan Cabrera); also, `main` of that repository is 366 commits behind `docs`.*
- [ ] Each evidence in `lavarapido-docs` has its Markdown, PDF, and Word in ES and EN, and the PDF and Word files open correctly. *The Markdown files are current as of 10/24/2026; the PDF and Word files of the documents changed on October 23 and 24, and those of the technical proposal (03), are still to be regenerated with the team's generator.*
- [x] The documents are readable: the Markdown renders on GitHub and the PDF files open without errors. *Checked on the version of 10/21/2026; repeat after regenerating.*
- [ ] Each repository identifies the project (README), the evaluated branch (`develop`), and the version (release tag). *`v1.0.0` in 9 of 10 repositories (payment-service since 10/24/2026); the mobile app is missing, with PR #1 open (Merari Urbano).*
- [ ] The documentation, repositories, and application are consistent: what the SRS and the manuals describe exists in the `develop` code. *Partial: SRS v8.0 marks 3 RF and 9 RNF as partial and the Corrective Actions document records what is still open (16 actions, none P0 or P1).*
- [ ] No simulations (mocks, `json-server`, sample data) are presented as real functionality. *Since 10/24/2026 the app and the web no longer show the business sample data (seed 113 removes it from the database); the app's legal texts still say "Express Car Wash S.A.S." (team decision).*
- [ ] There are no credentials or sensitive data: `.env` is not versioned (only `.env.example`) and there are no tokens or passwords in the history. *Partial: see the security criterion in section 5.*
- [ ] The exported PDF keeps the links active (click at least one per section). *Pending when the PDF is regenerated (Brayan Cabrera).*

---

## 5. Acceptance Criteria

| Criterion | Fulfillment condition | Result / remarks |
|---|---|---|
| Completeness | The 12 evidences have a direct and verifiable link | The 12 evidences have a link. Evidence 11 links the application deployed on Azure since 10/16/2026. |
| Accessibility | Every link opens for the instructor without asking for permissions | Partial: the links of `lavarapido-docs` and the code repositories are public (checked without logging in); those of `vehicle-w-docs` require giving the instructor read permission. |
| Traceability | Requirements → user stories → modules → tests → versions related | There is a matrix in §10 of the SRS (v8.0, with the partial requirements marked), another in §5 of the test document, and the source matrix in `vehicle-w-docs`. Version `v1.0.0` exists in 9 of 10 repositories. |
| Consistency | The documentation matches the code and the running application | Latest `develop` CI of 10/24/2026: 1,119 automated tests and 73 in the mobile app (1,192), all passed; that same code runs on the public server since that day. On 10/23/2026 there were 838. Tests of 10/21/2026 (final run, in the evening): 707 automated and 19 end-to-end tests passed; the early-morning run had 689. That day the administrator's "To close" list was also checked live on the web and in the mobile app. Local environment verified on 10/19/2026: every service `UP`, 42 functional cases passed, responsive design verified on 66 web screens and 15 app screens, and the screenshots of the manuals, SRS, analysis, and design taken again that day. |
| Security | No secrets or personal data exposed | Partial (reviewed on 10/24/2026 and updated on 10/26/2026): no repository versions `.env` and these documents contain no passwords. In `develop` the development passwords were removed from the code, the compose file, the READMEs and, since 10/24/2026, from `GUIA-EQUIPO.md` and the `payment-migrate` arguments, but these remain: the development `sa` password in `.env.example` of the `v1.0.0` tag of `lavarapido-infra` (since `v1.1.0`, `main` has `<cambia-esta-contraseña>`), the old SQL Server password in payment-service's Git history (its `main` reads it from `DB_PASSWORD`), and the Firebase key in the app's `google-services.json` (action ACO-25). The screenshots use test data. |
| Presentation | Navigable document, readable tables, and PDF with active links | Pending: the team regenerates the PDF with its APA 7 generator and checks one link per section (owner: Brayan Cabrera). |

---

## 6. Delivery

| Format | Suggested name |
|---|---|
| Markdown | `11_ENLACES_DE_EVIDENCIAS/EN/MD/Evidence_Links_Project_VehicleWashing.md` (in Spanish: `ES/MD/Enlaces_Evidencias_Proyecto_VehicleWashing.md`) |
| PDF | `11_ENLACES_DE_EVIDENCIAS/EN/PDF/Evidence_Links_Project_VehicleWashing.pdf`; to deliver it, copy it with the date, for example `Evidence_Links_Project_VehicleWashing_2026-10-17.pdf` |

The delivery channel (platform, email, shared folder, or other) is set by the instructor.

---

## 7. Security Note

- Do not include in this document or in the repositories passwords, tokens, API keys, the content of `.env`, connection strings, or real personal data.
- **Test credentials:** if the evaluator needs to log in, the team will deliver through a private channel (direct message or institutional platform) one test user per role (administrator, customer, and operator). Those accounts are created only for the evaluation and are deactivated afterwards.
- Do not use links to local files (`C:\...`, `file://`), expired links, or links that require unresolved permissions.
- **Public repositories:** review the history (`.env` files, JWT secrets, database passwords) before publishing or delivering them.
- **Private repositories** (`vehicle-w-docs`): give the instructor read permission and check the access with their account.

---

## 8. Reference Resources

- [GitHub Docs: About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)
- [GitHub Docs: Setting repository visibility](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility)

---

## 9. Reminder for the Team

> Update this matrix every time locations, branches, versions, or permissions change. After each change, export the PDF again and check the links again in the exported PDF.
