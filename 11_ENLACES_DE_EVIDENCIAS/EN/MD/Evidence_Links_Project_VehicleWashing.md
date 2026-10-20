# Evidence Links of the Training Project — LavaRápido (Vehicle Washing)

**Web and mobile booking and management platform for a car wash**

| Field | Value |
|---|---|
| Program / group | Technologist in Software Analysis and Development (ADSO), group 3145556 |
| Center | Centro de la Industria, la Empresa y los Servicios — SENA, Huila Region |
| Training project | [To complete: official name of the training project] |
| Work team | Vehicle Washing Development Team ([To complete: confirm the official team name]) |
| Members | Juan Camilo Guilombo Osorio, Brayan Estiven Patiño Cabrera, Merari Urbano Quintero |
| Instructor | Karol Daniela Correa |
| Delivery date | [To complete] |
| Last update of this document | October 20, 2026 |

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
| 1 | Requirements specification report | Functional and non-functional requirements, user stories, acceptance criteria, traceability | [SRS v7.6 (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/EN/MD/requirements-specification-report.md) · [Functional requirements (SRS §5)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/EN/MD/requirements-specification-report.md#5-functional-requirements) · [Non-functional requirements (SRS §6)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/EN/MD/requirements-specification-report.md#6-non-functional-requirements) · [User stories per requirement (SRS §10)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/EN/MD/requirements-specification-report.md#10-traceability-matrix) · Source in `vehicle-w-docs`: [Functional requirements](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/functional.md) · [Non-functional requirements](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/non-functional.md) · [User stories](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/user-stories.md) | Public / Pending permissions (`vehicle-w-docs`) | The SRS follows IEEE 830 and ISO/IEC/IEEE 29148 and covers 41 functional requirements (RF-001 to RF-038) and use cases CU01 to CU32. Spanish version: `01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/ES/`. |
| 2 | Software analysis | Dynamic views, processes, use cases, sequence and state diagrams | [Dynamic views analysis (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/02_DOCUMENTACION_DE_ANALISIS_DEL_SOFTWARE/EN/MD/software-analysis-documentation.md) · [Sequence, activity, and state diagrams](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/02_DOCUMENTACION_DE_ANALISIS_DEL_SOFTWARE/EN/MD/software-analysis-documentation.md#2-sequence-diagrams) · Source in `vehicle-w-docs`: [UML diagrams (sources)](https://github.com/code-sena/vehicle-w-docs/tree/docs/08-uml/diagrams/source) | Public / Pending permissions (`vehicle-w-docs`) | The screenshots are in `02_DOCUMENTACION_DE_ANALISIS_DEL_SOFTWARE/EN/MD/capturas/`. The diagrams include the booking, payment, registration, reminder, assignment, and inspection sequences, and the booking and payment states. |
| 3 | Technical proposal of the software | Selected alternative, technologies, justification, scope, and constraints | [Technical proposal (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/03_PROPUESTA_TECNICA_DEL_SOFTWARE/EN/MD/software-technical-proposal.md) · [Design decisions (SRS §3.6)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/EN/MD/requirements-specification-report.md#36-design-decisions) · [Alternatives considered](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/03_PROPUESTA_TECNICA_DEL_SOFTWARE/EN/MD/software-technical-proposal.md#3-alternatives-considered) · Source in `vehicle-w-docs`: [Architecture decisions (ADR-001 to ADR-015)](https://github.com/code-sena/vehicle-w-docs/tree/docs/05-architecture/decisions/records) | Public / Pending permissions (`vehicle-w-docs`) | The ADRs justify the microservices architecture, the database, the API Gateway, JWT, and the use of .NET for the payment service. |
| 4 | Software design | Graphical interfaces, architecture, patterns, data model, and diagrams | [Software design (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/04_DOCUMENTACION_DE_DISENO_DEL_SOFTWARE/EN/MD/software-design-documentation.md) · [Architectural model](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/04_DOCUMENTACION_DE_DISENO_DEL_SOFTWARE/EN/MD/software-design-documentation.md#3-architectural-model) · [Data model](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/04_DOCUMENTACION_DE_DISENO_DEL_SOFTWARE/EN/MD/software-design-documentation.md#5-data-model) · [API and system routes (technical manual §13)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/EN/MD/technical-manual.md#13-api-or-system-routes) · Source in `vehicle-w-docs`: [Architecture](https://github.com/code-sena/vehicle-w-docs/tree/docs/05-architecture) · [Data model](https://github.com/code-sena/vehicle-w-docs/tree/docs/06-data) · [OpenAPI contracts](https://github.com/code-sena/vehicle-w-docs/tree/docs/07-api/contracts/openapi) | Public / Pending permissions (`vehicle-w-docs`) | Hexagonal architecture pattern (ADR-007). Section 2.5 describes the responsive design. The screenshots are in `04_DOCUMENTACION_DE_DISENO_DEL_SOFTWARE/EN/MD/capturas/`. |
| 5 | Source code and software artifacts | Repositories of the web frontend, mobile app, backend, infrastructure, and database, with their branches | [Code artifacts (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/05_ARTEFACTOS_DE_CODIGO/EN/MD/code-artifacts.md) · see [section 2](#2-source-code-repositories) | Public | The integration branch is `develop`. `main` is behind in every repository (see section 2). |
| 6 | Test documentation | Plan, test cases, results, execution evidence, defects, and fixes | [Test documentation (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/06_DOCUMENTACION_DE_PRUEBAS/EN/MD/test-documentation.md) · [E2E tests](https://github.com/BrayanCABRERA123/lavarapido-infra/tree/develop/e2e) · [Test plan](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/06_DOCUMENTACION_DE_PRUEBAS/EN/MD/test-documentation.md#1-test-plan) · Source in `vehicle-w-docs`: [Testing strategy](https://github.com/code-sena/vehicle-w-docs/blob/docs/11-quality/testing-strategy.md) | Public / Pending permissions (`vehicle-w-docs`) | Follows ISO/IEC/IEEE 29119-3. Automated (655), end-to-end (19), functional (42), performance, and responsive design tests run on 10/19/2026 (§3). The traceability matrix is in §5 and the findings in §6. |
| 7 | Implementation procedure | Reproducible installation, configuration, deployment, and verification | [Implementation procedure (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/EN/MD/implementation-procedure.md) · [Azure deployment document (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/EN/MD/deployment-document.md) · Support: [Infrastructure README](https://github.com/BrayanCABRERA123/lavarapido-infra/blob/develop/README.md) · [Team guide](https://github.com/BrayanCABRERA123/lavarapido-infra/blob/develop/GUIA-EQUIPO.md) | Public | Available in Markdown, PDF, and Word (ES and EN) in `07_PROCEDIMIENTO_DE_IMPLEMENTACION/`. The deployment document records the deployment of 10/16/2026 on Azure with its evidence screenshots. |
| 8 | Corrective, preventive, and improvement actions | Findings, priority, owner, applied action, and closing evidence | [Corrective, preventive, and improvement actions (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/08_ACCIONES_CORRECTIVAS_PREVENTIVAS_Y_DE_MEJORA/EN/MD/corrective-preventive-and-improvement-actions.md) · Support: [Preventive actions](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/08_ACCIONES_CORRECTIVAS_PREVENTIVAS_Y_DE_MEJORA/EN/MD/corrective-preventive-and-improvement-actions.md#11-register-of-preventive-actions) · [Traceability between actions, risks, and technical debt](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/08_ACCIONES_CORRECTIVAS_PREVENTIVAS_Y_DE_MEJORA/EN/MD/corrective-preventive-and-improvement-actions.md#annex-c-traceability-between-actions-risks-and-technical-debt) · Source in `vehicle-w-docs`: [Risks](https://github.com/code-sena/vehicle-w-docs/blob/docs/15-project-control/risks.md) · [Technical backlog](https://github.com/code-sena/vehicle-w-docs/blob/docs/15-project-control/technical-backlog.md) | Public / Pending permissions (`vehicle-w-docs`) | Available in Markdown, PDF, and Word (ES and EN) in `08_ACCIONES_CORRECTIVAS_PREVENTIVAS_Y_DE_MEJORA/`. |
| 9 | Technical, installation, and user manuals | Prerequisites, configuration, use, and troubleshooting | [Technical manual (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/EN/MD/technical-manual.md) · [Installation manual (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/EN/MD/installation-manual.md) · [User manual (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/EN/MD/user-manual.md) · [Administrator manual (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/09_MANUALES/EN/MD/administrator-manual.md) · [PDF of the manuals](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/09_MANUALES/EN/PDF) · Source in `vehicle-w-docs`: [User manual](https://github.com/code-sena/vehicle-w-docs/blob/docs/14-training/user-manual.md) | Public / Pending permissions (`vehicle-w-docs`) | Each manual is in Markdown, PDF, and Word (ES and EN), in the `09_MANUALES/` folder. Version 4.3 or later (see each manual's version control), with real screenshots of the system; the `.env` secrets appear masked. |
| 10 | Project article | Problem, objectives, solution, methodology, results, and conclusions | [APA 7 article (ES/EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/10_ARTICULO_DEL_PROYECTO/MD/articulo-del-proyecto-apa7.md) · [APA 7 PDF](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/10_ARTICULO_DEL_PROYECTO/PDF/10_Articulo_Del_Proyecto_APA7.pdf) · [IEEE version](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/10_ARTICULO_DEL_PROYECTO/PDF/10_Articulo_Del_Proyecto_IEEE.pdf) · [ACM version](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/10_ARTICULO_DEL_PROYECTO/PDF/10_Articulo_Del_Proyecto_ACM.pdf) | Public | The three versions (APA 7, IEEE, and ACM) are in Markdown, PDF, and Word in the `10_ARTICULO_DEL_PROYECTO/` folder. Each file is bilingual (ES and EN in the same document), which is why this folder is not split by language. |
| 11 | Deployed application or demo | Access URL or demo environment and verification instructions | [Application in production](https://lavarapidovehicular.northcentralus.cloudapp.azure.com) · [Android app download](https://lavarapidovehicular.northcentralus.cloudapp.azure.com/app/LavaRapidoVehicular.apk) · [Deployment document (EN)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/EN/MD/deployment-document.md) | Public | Deployed on 10/16/2026 on an Azure virtual machine (Docker Compose, Caddy with Let's Encrypt HTTPS). The smoke tests and screenshots are in [section 5 of the deployment document](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/EN/MD/deployment-document.md#5-verification-testing-and-evidence-plan-smoke-tests). The credentials are delivered through a private channel (see section 7). |
| 12 | Traceability and integration of evidence | Relationship between requirements, user stories, modules, tests, and versions | [Traceability matrix (SRS §10)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/EN/MD/requirements-specification-report.md#10-traceability-matrix) · [Requirements–tests traceability (§5)](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/06_DOCUMENTACION_DE_PRUEBAS/EN/MD/test-documentation.md#5-traceability-matrix) · Source in `vehicle-w-docs`: [Traceability matrix](https://github.com/code-sena/vehicle-w-docs/blob/docs/04-requirements/traceability-matrix.md) | Public / Pending permissions (`vehicle-w-docs`) | There are no release tags, so traceability to versions is done by branch (`develop`) and by commit. |

---

## 2. Source Code Repositories

Working branch: **`develop`** in every code repository. There are no release tags. The "Last commit" and "`main` behind" columns were taken on 10/20/2026.

| Component | Technology | Repository (`develop` branch) | Last commit | `main` behind | Access |
|---|---|---|---|---|---|
| Web frontend | Angular | [Front-end-proyecto-web](https://github.com/BrayanCABRERA123/Front-end-proyecto-web/tree/develop) | `9115315` | 448 commits | Public |
| Mobile application | React Native (Expo) | [LavadoVehicular-Movil](https://github.com/merari0322/LavadoVehicular-Movil/tree/develop) | `37ae4e2` | 219 commits | Public |
| API Gateway | Spring Boot | [lavarapido-api-gateway](https://github.com/BrayanCABRERA123/lavarapido-api-gateway/tree/develop) | `755106d` | 16 commits | Public |
| Security (authentication, JWT, roles) | Spring Boot | [lavarapido-security-service](https://github.com/BrayanCABRERA123/lavarapido-security-service/tree/develop) | `a636381` | 59 commits | Public |
| Customers and vehicles | Spring Boot | [lavarapido-customer-service](https://github.com/camiloguilombo12/lavarapido-customer-service/tree/develop) | `fa56995` | 10 commits | Public |
| Catalog and bookings | Spring Boot | [lavarapido-booking-service](https://github.com/camiloguilombo12/lavarapido-booking-service/tree/develop) | `5c33ced` | 53 commits | Public |
| Operations (operators and bays) | Spring Boot | [lavarapido-operation-service](https://github.com/BrayanCABRERA123/lavarapido-operation-service/tree/develop) | `7df32dc` | 41 commits | Public |
| Payments and loyalty | .NET Core | [lavarapido-payment-service](https://github.com/merari0322/lavarapido-payment-service/tree/develop) | `e98e97d` | 45 commits | Public |
| Notifications | Spring Boot | [lavarapido-notification-service](https://github.com/BrayanCABRERA123/lavarapido-notification-service/tree/develop) | `2e8cb77` | 38 commits | Public |
| Infrastructure (Docker, database, E2E tests) | Docker, SQL Server, RabbitMQ | [lavarapido-infra](https://github.com/BrayanCABRERA123/lavarapido-infra/tree/develop) | `61d8b72` | 63 commits | Public |
| Technical documentation (SDD) | Markdown, OpenAPI | [vehicle-w-docs](https://github.com/code-sena/vehicle-w-docs/tree/docs) (`docs` branch) | `2ded624` | 344 commits | Pending permissions |
| Documentary evidence | Markdown | [lavarapido-docs](https://github.com/BrayanCABRERA123/lavarapido-docs) (`main` branch) | last commit of `main` | — | Public |

**Database:** shared SQL Server 2022, with one schema per service (ADR-003, ADR-009). Each Spring Boot service manages its migrations with Liquibase. The payment service migrations are in [`lavarapido-payment-service/db`](https://github.com/merari0322/lavarapido-payment-service/tree/develop/db).

> Recommendation: before delivering, merge `develop` into `main` in each repository, or tell the evaluator to review `develop`, so that the evaluated version is consistent.

---

## 3. Deployment and Technical Verification

| Aspect | Value |
|---|---|
| Version (release tag) | `v1.0.0` pending. [To complete: create the tag in each repository when moving `develop` to `main`] |
| Environment | Academic production on Azure (Ubuntu 24.04 VM, Docker Compose with `docker-compose.prod.yml`), deployed on 10/16/2026. For development: local with Docker (`docker compose --profile app up -d --build` from `lavarapido-infra`). Details in the [deployment document](https://github.com/BrayanCABRERA123/lavarapido-docs/blob/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/EN/MD/deployment-document.md). |
| Public demo environment | https://lavarapidovehicular.northcentralus.cloudapp.azure.com |

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
| Automated E2E flow | `node --test "e2e/*.test.js"` in `lavarapido-infra` (with `E2E_OPERATOR_ID=2` in the local database) | 19 of 19 tests passed in 11.2 s (10/19/2026) |

### 3.5 Evidence Screenshots

| Screenshot | Description | Link |
|---|---|---|
| Web screens (login, admin, customer, operator) | 28 interface screenshots | [SRS `capturas` folder](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/01_INFORME_DE_ESPECIFICACION_DE_REQUISITOS/EN/MD/capturas) |
| Dynamic views and modals | 41 screenshots | [Analysis `capturas` folder](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/02_DOCUMENTACION_DE_ANALISIS_DEL_SOFTWARE/EN/MD/capturas) |
| Design (landing, login, booking, payments) | Screenshots of the final design | [`capturas` folder](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/04_DOCUMENTACION_DE_DISENO_DEL_SOFTWARE/EN/MD/capturas) |
| Real screenshots of the manuals | 56 screenshots per language of the running system (10/16/2026): screens of the three roles, installation terminal, and data model diagram | [Manuals `capturas` folder](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/09_MANUALES/EN/MD/capturas) |
| Containers, logs, health checks, and migrations in production | Portainer, startup logs, `/actuator/health`, clean console, and Liquibase changesets (10/16/2026) | [Deployment `capturas` folder](https://github.com/BrayanCABRERA123/lavarapido-docs/tree/main/07_PROCEDIMIENTO_DE_IMPLEMENTACION/EN/MD/capturas) |

---

## 4. Accessibility and Quality Checklist

- [ ] Every link opens correctly, without 404 errors or denied access, tested from an account outside the team.
- [ ] The instructor has read permission on `code-sena/vehicle-w-docs` (private) and checked it with their account.
- [ ] Each evidence in `lavarapido-docs` has its Markdown, PDF, and Word in ES and EN, and the PDF and Word files open correctly.
- [ ] The documents are readable: the Markdown renders on GitHub and the PDF files open without errors.
- [ ] Each repository identifies the project (README), the evaluated branch (`develop`), and the version (release tag).
- [ ] The documentation, repositories, and application are consistent: what the SRS and the manuals describe exists in the `develop` code.
- [ ] No simulations (mocks, `json-server`, sample data) are presented as real functionality.
- [ ] There are no credentials or sensitive data: `.env` is not versioned (only `.env.example`) and there are no tokens or passwords in the history.
- [ ] The exported PDF keeps the links active (click at least one per section).

---

## 5. Acceptance Criteria

| Criterion | Fulfillment condition | Result / remarks |
|---|---|---|
| Completeness | The 12 evidences have a direct and verifiable link | The 12 evidences have a link. Evidence 11 links the application deployed on Azure since 10/16/2026. |
| Accessibility | Every link opens for the instructor without asking for permissions | Partial: the links of `lavarapido-docs` and the code repositories are public (checked without logging in); those of `vehicle-w-docs` require giving the instructor read permission. |
| Traceability | Requirements → user stories → modules → tests → versions related | There is a matrix in §10 of the SRS, another in §5 of the test document, and the source matrix in `vehicle-w-docs`. Release tags are missing. |
| Consistency | The documentation matches the code and the running application | Local environment verified on 10/19/2026: every service `UP`, 655 automated tests, 19 end-to-end tests, and 42 functional cases passed, responsive design verified on 66 web screens and 15 app screens, and the screenshots of the manuals, SRS, analysis, and design taken again that day. |
| Security | No secrets or personal data exposed | Reviewed on 10/16/2026: no repository has `.env` files in its history and the versioned files only contain sample values (`.env.example`). The screenshots use test data. |
| Presentation | Navigable document, readable tables, and PDF with active links | [To complete after exporting the PDF] |

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
