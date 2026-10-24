<!-- running-head: CORRECTIVE, PREVENTIVE, AND IMPROVEMENT ACTIONS: VEHICLE WASHING SYSTEM -->

# Documentation of Corrective, Preventive, and Improvement Actions for the Software

Vehicle Washing Management System (Vehicle Washing)

Management Procedure, Action Register, Root Cause Analysis, Follow-Up, and Lessons Learned

Brayan Estiven Patiño Cabrera (Project Leader), Juan Camilo Guilombo Osorio (Frontend Leader), and Merari Urbano Quintero (Backend Leader)

Technologist in Software Analysis and Development (ADSO), Servicio Nacional de Aprendizaje (SENA), Training Center: Industria

Ficha 3145556

Instructor: Karol Daniela Correa

October 23, 2026

Document Type: Register of Corrective, Preventive, and Improvement Actions (Development Team and Instructor) · Version 2.7

## Version Control

Table 1 records the change history of this document. The action register (sections 9 to 12) is a living document: each time an action is opened, updated, or closed, the row of the action is modified and, at least once per sprint, a row is added to this table.

**Table 1**

*Version History of the Actions Document*

| Version | Date | Description of the change | Responsible |
|---|---|---|---|
| 1.0 | 2026-10-09 | Creation of the document (in Spanish and English). The management procedure is defined, and 23 closed corrective actions, 13 open corrective actions, 14 preventive actions, and 13 improvement actions are recorded, verified against the code of the eleven repositories (*develop* branch as of October 9, 2026), the Git history, the risk register, and the technical backlog of the project. | Development team |
| 2.0 | 2026-10-16 | Review against the code of October 16, 2026. Eleven open corrective actions were closed (ACO-01 to ACO-03 and ACO-05 to ACO-12, now AC-24 to AC-34) and five improvement actions (AM-01, AM-04, AM-08, AM-10, and AM-11); five nonconformities found in the complete review of the system were recorded and closed (AC-35 to AC-39); the preventive actions, indicators, lessons learned, and traceability were updated. | Development team |
| 2.1 | 2026-10-17 | Review against the code of October 17, 2026. Corrective actions AC-40 to AC-43 were closed (expired session notice when logging out, screens overflowing on phones, squashed filter inputs in the app, and service progress before it started), preventive action AP-15 was added (responsive design check before merging), and improvements AM-07 (inspection report in the mobile app) and AM-08 (frequently asked questions on the home page) were closed. | Development team |
| 2.2 | 2026-10-19 | Preventive action AP-01 was closed with continuous integration in GitHub Actions in the 10 repositories. | Development team |
| 2.3 | 2026-10-19 | Test indicator with the run of October 19 (655 automated, 19 end-to-end, and 42 functional cases). | Development team |
| 2.4 | 2026-10-20 | Review against the code of October 20, 2026: the register is still current (AM-03, rescheduling from the web and the app, and AM-12, the pause and issue states, remain open); the backend leader's full name was completed. | Development team |
| 2.5 | 2026-10-21 | Review against the code of October 21, 2026. Corrective actions AC-44 to AC-52 were recorded and closed (a token that kept working after logout, bookings nobody closed, an operator assigned twice, receipts with no size limit, cash visible although it was disabled, reports counting unfinished bookings, misleading roles screen text, tabs out of step with the session, and a database transaction log with no limit); preventive action AP-04 (verified daily backups) was closed, corrective action ACO-14 (new variables missing from *.env.example* and the compose file) was opened, AP-16 to AP-18 (container logs, security headers, and health checks) and improvement AM-16 (mandatory APK update) were added and closed; the improvements of October 17 that repeated the identifiers AM-07 and AM-08 become AM-14 (inspection report in the app) and AM-15 (frequently asked questions); indicators with the tests of October 21. | Development team |
| 2.6 | 2026-10-21 | Review against the code of the evening of October 21, 2026. AC-45 was adjusted and corrective actions AC-53 (the first version of the automatic close could record as "No-show" a service that was actually done) and AC-54 (a `null` field in an event sent the message to notification-service's dead-letter queue) were recorded and closed; preventive action AP-19 and lesson L-16 were added; ACO-14 includes the operations-service *FOLLOW_UP_\** variables; indicators with the final run of October 21 (707 tests). | Development team |
| 2.7 | 2026-10-23 | Review against *develop* of October 23, 2026, version *v1.0.0*, and that day's system review. ACO-14 was closed (AC-55), as were the corrective actions Merari Urbano fixed that day in *develop* (AC-56 to AC-71, with their commit) and the outdated documentation (AC-72). ACO-15 to ACO-32 were opened with the findings that remain open and the caveats of that day's fixes (SEC-01, BIZ-01, BIZ-02, OPS-01, CD-01, among others); two are P1, so entry criterion E6 is no longer met. Table 10 was recalculated, improvements AM-17 (continuous deployment) and AM-18 (client tests) were added, and Annex D with the instructor's evaluation (H-01 to H-25) and its status. | Development team |

*Note.* Dates are written in the ISO 8601 format (year-month-day). Prepared by the development team.

## Table of Contents

<!-- toc -->

- [Version Control](#version-control)
- [4. Introduction](#4-introduction)
  - [4.1 Reference Framework](#41-reference-framework)
  - [4.2 Sources of This Document](#42-sources-of-this-document)
- [5. Objective](#5-objective)
  - [5.1 General Objective](#51-general-objective)
  - [5.2 Specific Objectives](#52-specific-objectives)
- [6. Scope](#6-scope)
- [7. Definitions and Classification](#7-definitions-and-classification)
  - [7.1 Types of Action](#71-types-of-action)
  - [7.2 Severity and Priority](#72-severity-and-priority)
  - [7.3 States of an Action](#73-states-of-an-action)
- [8. Action Management Procedure](#8-action-management-procedure)
  - [8.1 Identification Sources](#81-identification-sources)
  - [8.2 Stages of the Procedure](#82-stages-of-the-procedure)
  - [8.3 Root Cause Analysis](#83-root-cause-analysis)
  - [8.4 Effectiveness Verification](#84-effectiveness-verification)
  - [8.5 Roles](#85-roles)
- [9. Register of Closed Corrective Actions](#9-register-of-closed-corrective-actions)
- [10. Register of Open Corrective Actions](#10-register-of-open-corrective-actions)
- [11. Register of Preventive Actions](#11-register-of-preventive-actions)
- [12. Register of Improvement Actions](#12-register-of-improvement-actions)
- [13. Follow-Up Indicators](#13-follow-up-indicators)
- [14. Lessons Learned](#14-lessons-learned)
- [15. Glossary](#15-glossary)
- [References](#references)
- [16. Annexes](#16-annexes)
  - [Annex A. Action Record Form](#annex-a-action-record-form)
  - [Annex B. Root Cause Analysis Example](#annex-b-root-cause-analysis-example)
  - [Annex C. Traceability Between Actions, Risks, and Technical Debt](#annex-c-traceability-between-actions-risks-and-technical-debt)
  - [Annex D. Instructor Evaluation](#annex-d-instructor-evaluation)

<!-- /toc -->

*Note.* Numbering starts at 4 because sections 1 to 3 are the cover, the version control, and the table of contents, which have no number in their title. It is kept this way so that the cross-references between documents by section number (for example, "Installation Manual, section 10") remain valid.

## 4. Introduction

The Vehicle Washing Management System (Vehicle Washing), internally called *LavaRapido*, is a platform for bookings, operator assignment, execution and rating of services, verification of payments by QR code, and loyalty points for a car wash. It consists of a gateway, six microservices (five in Java 21 with Spring Boot 4 and one in .NET 8), a SQL Server 2022 database, RabbitMQ, and two clients, web (Angular 21) and mobile (React Native with Expo) (Vehicle Washing Development Team, 2026a).

During its construction, its reviews with the instructor, and the writing of its manuals, defects, risks, and improvement opportunities have been detected. This document establishes **how** they are managed (identification, recording, root cause analysis, planning, execution, verification, and closure) and **records** the actions taken and pending, so that any team member, the instructor, or a future maintenance team knows what was corrected, why, with what evidence, and what remains to be done.

### 4.1 Reference Framework

- **ISO/IEC/IEEE 12207:2017.** The Maintenance process (6.4.13) includes correcting defects, preventing failures, and improving the software in operation, and the Quality Assurance process (6.3.8) requires treating the incidents and problems detected and verifying that the actions are effective (International Organization for Standardization [ISO] et al., 2017).
- **ISO/IEC/IEEE 14764:2022.** It elaborates the maintenance process of ISO/IEC/IEEE 12207 and defines the types of maintenance; this document uses the corrective (correct discovered defects), preventive (correct latent defects before they become failures), adaptive (adjust the software to changes in the environment), and perfective (improve the software) types (ISO et al., 2022).
- **ISO 9001:2015.** Clause 10.2 requires reacting to a nonconformity, determining its causes, implementing the necessary action, reviewing its effectiveness, and retaining documented information; clause 10.3 requires continual improvement. The standard replaced "preventive action" as a separate requirement with risk-based thinking (clause 6.1), so in this document preventive actions arise from the risk register (ISO, 2015).
- **PDCA cycle.** Each action goes through the plan, do, check, and act cycle, which is the basis of continual improvement in ISO 9001.

### 4.2 Sources of This Document

The actions were verified against the code of the eleven repositories (*develop* branch as of October 23, 2026, with that day's version *v1.0.0*) and their Git history, against the system review of October 23, 2026 (security, business, operations, deployment, web, mobile, and documentation), and against the instructor's end-to-end evaluation of October 21, 2026 (Annex D), and against the risk register, the technical backlog, the incident management, the testing strategy, and the architecture decision records (ADRs) of the project (Vehicle Washing Development Team, 2026a). The findings of the review of the manuals of October 7, 9, and 16, 2026, and of the complete review of the system of October 16 (Annex B of the Technical Manual and the annexes of the other manuals) are also included.

## 5. Objective

### 5.1 General Objective

To document the procedure and the register of the corrective, preventive, and improvement actions of the Vehicle Washing Management System, to ensure that each defect, risk, or improvement opportunity is treated in a traceable and verifiable way, with learning for the team.

### 5.2 Specific Objectives

- Define the types of action, their classification by severity and priority, and their life cycle of states.
- Establish a single procedure to identify, record, analyze, execute, verify, and close actions.
- Record the corrective actions already performed with their root cause and their evidence.
- Record the pending corrective, preventive, and improvement actions with their person responsible, priority, and closure criterion.
- Define indicators to measure the effectiveness of the procedure and consolidate the lessons learned.

## 6. Scope

**It covers:** the six backend services, the gateway, the database, the Docker infrastructure, the web application, the mobile application, and the project documentation (manuals, ADRs, contracts, and data models), from construction to operation after implementation.

**It does not cover:** the management of new product requirements (user stories of the product backlog), except when an improvement need of the software already built is recorded as an improvement action; nor the academic management of the project (grades, program deliveries).

## 7. Definitions and Classification

### 7.1 Types of Action

**Table 2**

*Types of Action and Their Relationship With the Types of Maintenance*

| Type | Definition | Trigger | Type of maintenance (ISO/IEC/IEEE 14764) | Prefix |
|---|---|---|---|---|
| Corrective action | Eliminates the cause of a nonconformity that **has already occurred** (defect, failure to meet a requirement, an ADR, or the documentation) so that it does not recur. | Incident, failed test, review, remark of the instructor or of acceptance. | Corrective | AC (closed) and ACO (open) |
| Preventive action | Eliminates the cause of a **potential** nonconformity before it occurs. | Risk of the risk register, technical debt, trend analysis. | Preventive and adaptive | AP |
| Improvement action | Increases the value, quality, or efficiency of the software without an existing failure. | Retrospective, user suggestion, recommended evolution of the architecture. | Perfective and adaptive | AM |

*Note.* Prepared by the authors from ISO (2015) and ISO et al. (2022). The prefixes keep the Spanish initials so that both versions of the register share the same identifiers.

A **correction** (for example, restarting a service or editing a record) is not a corrective action: it resolves the symptom, but not the cause. In the project's incident management, the correction corresponds to the "mitigate" step; the corrective action is the change of code, configuration, or process that prevents the incident from recurring.

### 7.2 Severity and Priority

Severity uses the same scale as the project's incident management (Table 3). Priority combines severity with the probability of occurrence and the effort, and is expressed as High, Medium, or Low, as in the technical backlog.

**Table 3**

*Severity Scale*

| Level | Definition | Example | Response time |
|---|---|---|---|
| P0 | Nothing works. | SQL Server down; no service starts; login impossible. | Immediate. |
| P1 | A core flow is broken. | A booking, an assignment, the start of a service, or the report or approval of a payment is impossible. | The same day. |
| P2 | A secondary function fails and a workaround exists. | Emails do not arrive, but the internal inbox works. | Within the sprint. |
| P3 | Cosmetic or documentary. | Untranslated text, wrong icon, outdated manual. | Backlog. |

*Note.* Taken from the incident management of the project (Vehicle Washing Development Team, 2026a).

### 7.3 States of an Action

Each action goes through the states **Open** (recorded), **Under analysis** (the root cause is being sought), **Planned** (it has a person responsible, a solution, and a date), **In progress** (branch and pull request under way), **Under verification** (deployed; its effectiveness is being checked), and **Closed** (effective and with evidence). An action whose verification fails returns to *Under analysis*. An action that the team decides not to perform is marked **Accepted as a risk**, with the justification and the approval of the project leader.

## 8. Action Management Procedure

### 8.1 Identification Sources

- Incidents of the project's incident management and their post-mortems (P0 and P1).
- Failed automated tests (*./mvnw verify*, *dotnet test*, *ng build*) and manual end-to-end tests before each review.
- Code reviews (pull requests) and reviews by the instructor.
- Smoke and acceptance tests of the Implementation Procedure.
- Comparison between the code, the ADRs, and the manuals (discrepancy annexes).
- Risk register and technical backlog (source of preventive actions).
- Retrospectives of each sprint and user comments (source of improvement actions).

### 8.2 Stages of the Procedure

**Table 4**

*Stages of the Action Management Procedure*

| Stage (PDCA) | Activity | Responsible | Output |
|---|---|---|---|
| 1. Identify (Plan) | Detect the nonconformity, risk, or opportunity and report it in the team chat. | Whoever detects it | Notice with description and evidence. |
| 2. Record (Plan) | Create the row in the corresponding register (sections 9 to 12) with the form of Annex A; assign ID, type, severity, and person responsible. | Leader of the affected area | Action in the Open state. |
| 3. Contain (Do) | Only for P0 and P1 corrective actions: apply the immediate correction (restart, adjust *.env*, start the missing container). | Service owner | Flow restored. |
| 4. Analyze the cause (Plan) | Apply the five whys or the cause-and-effect diagram (section 8.3). | Service owner | Documented root cause. |
| 5. Plan (Plan) | Define the solution, the closure criterion, the effort, and the date; if a technical decision changes, create or modify an ADR. | Person responsible with the project leader | Action in the Planned state. |
| 6. Execute (Do) | *fix/\** or *feat/\** branch, change with tests that reproduce the defect, pull request reviewed by another person, and documentation updated in the same pull request (definition of done). | Person responsible | Pull request merged into *develop*. |
| 7. Verify effectiveness (Check) | Check the closure criterion in the implemented environment and that the problem does not reappear (section 8.4). | Person other than the executor | Verification evidence. |
| 8. Close and learn (Act) | Mark Closed, record the lesson learned (section 14), and update the risk register and the technical backlog. | Project leader | Action in the Closed state. |

*Note.* Prepared by the authors from clause 10.2 of ISO (2015) and the definition of done of the project.

### 8.3 Root Cause Analysis

For corrective actions of severity P0, P1, and P2, documenting the root cause is mandatory. Two techniques are used:

- **Five whys:** the question "why did it happen?" is asked about each answer until reaching a cause on which the team can act (process, design, configuration, or knowledge). Annex B contains a real example from the project.
- **Cause-and-effect (Ishikawa) diagram:** when there are several possible causes, they are classified into the categories *code*, *configuration*, *data*, *infrastructure*, *process*, and *people* before choosing the main cause.

The root cause is **never** recorded as "human error": if a person made a mistake, the question is what in the process, the tool, or the documentation allowed the mistake (the blameless approach of the project's post-mortems).

### 8.4 Effectiveness Verification

An action is closed only when its closure criterion is met and there is verifiable evidence: a commit or pull request, an automated test that reproduces the defect and now passes, the result of a manual test, a database query, or a screenshot. For P0 and P1 corrective actions, it is also required that the problem does not reappear in the next review or implementation. Verification is performed by a person other than the one who executed the action.

### 8.5 Roles

**Table 5**

*Roles in Action Management*

| Role | Person | Responsibility |
|---|---|---|
| Project leader | Brayan Estiven Patiño Cabrera | Approves priorities, accepts risks, verifies closure, and maintains this document. |
| Backend leader | Merari Urbano Quintero | Responsible for the actions of services, database, and infrastructure. |
| Frontend leader | Juan Camilo Guilombo Osorio | Responsible for the actions of the web and mobile applications. |
| Author of each pull request | Any team member | Updates the affected documentation in the same pull request. |
| Instructor | Karol Daniela Correa | Source of remarks; reviews the document at the deliveries. |

*Note.* Prepared by the authors. Each service also has an owner defined in the project's service catalog.

## 9. Register of Closed Corrective Actions

Table 6 records the nonconformities already corrected, with their root cause and the closure evidence. The "Origin" column refers to the closed risk (C-), the technical debt item (TD-), or the corresponding ADR.

**Table 6**

*Closed Corrective Actions*

| ID | Nonconformity | Sev. | Root cause | Action performed | Closure evidence | Origin | Closed |
|---|---|---|---|---|---|---|---|
| AC-01 | Booking times appeared shifted by five hours. | P1 | The JVM converted dates with the machine's time zone instead of the business's. | The booking-service JVM runs in UTC; dates are stored in UTC and converted only at the edges with *BOOKING_ZONE=America/Bogota*. | *AvailabilityPolicyTest* tests and correct bookings in the end-to-end test. | C-001 | 2026-10-04 |
| AC-02 | Services failed at startup after *docker compose up*. | P0 | The services tried to connect before SQL Server was healthy. | Health checks on *sqlserver* and *rabbitmq* and *service_healthy* and *service_completed_successfully* dependencies in the Compose file. | *docker-compose.yml* with conditional *depends_on*. | C-002 | 2026-10-04 |
| AC-03 | Two different implementations of the booking service existed. | P1 | Coding started without an agreed data model. | booking-service was rebuilt from the agreed SQL model; team rule: agree on the model before coding a service. | A single repository *lavarapido-booking-service* aligned with *06-data/models.md*. | C-003 | 2026-10-04 |
| AC-04 | With *--profile app*, every payment route failed. | P1 | payment-service had no Dockerfile or Compose service, and the gateway container did not receive *ROUTE_PAYMENT_URL*. | Multi-stage .NET 8 Dockerfile, *payment-service* service in Compose, and *ROUTE_PAYMENT_URL* in the gateway. | *lavarapido-infra* commit of 2026-10-08 ("wire payment-service to booking-service and rabbitmq"). | TD-014 | 2026-10-08 |
| AC-05 | *BOOKING_SERVICE_URL* was missing for payment-service in Compose; crediting points failed in containers. | P1 | The variable was omitted when the service was created (pre-existing gap found in ADR-015). | Variable added with *http://booking-service:3003/api/v1*. | Current *docker-compose.yml*. | ADR-015 | 2026-10-08 |
| AC-06 | The customer was not notified when a payment was approved, rejected, or refunded. | P2 | payment-service raised domain events but had no RabbitMQ publisher. | Publisher with *RabbitMQ.Client* and events *payment.confirmed*, *payment.rejected*, and *payment.refunded*, with an email to the customer. | ADR-011 section 9; *PAYMENT_\** types in notification-service (migration 028). | TD-015 | 2026-10-08 |
| AC-07 | The same transaction reference could pay two bookings. | P1 | The uniqueness of the reference was not validated when a payment was reported (control of ADR-008 and RF-016). | Validation in payment-service with the error code *TRANSACTION_REFERENCE_REUSED*. | *ErrorCodes.cs* of payment-service. | TD-016 | 2026-10-08 |
| AC-08 | payment-service only tested its domain; the role and conflict (409) rules were unprotected. | P2 | Application and API tests were postponed when the service was built. | Projects *PaymentService.Application.UnitTests* and *Infrastructure.IntegrationTests*. | *tests/* folder with command, query, promotion, and persistence tests. | TD-018 | 2026-10-08 |
| AC-09 | Points earned by a booking were not reversed when its payment was refunded, and two simultaneous movements could leave a wrong balance. | P1 | The points ledger had no reversal movement and no concurrency control. | *REVERSED* movement type and *sequence_no* column unique per customer (migration *pay-020*); the second concurrent movement answers 409. | Migration *020-loyalty-reversal-and-sequence.sql*. | ADR-015 | 2026-10-08 |
| AC-10 | Payment approval compared the booking total with itself and accepted invalid images. | P1 | The amount declared by the customer was neither sent nor compared. | The paid amount is sent and compared with the amount due in the review window, and images are validated as PNG or JPG. | payment-service and web commits of 2026-10-08. | Manuals v3.0 | 2026-10-08 |
| AC-11 | A "custom roles" catalog existed with no effect on authorization, contradicting ADR-010. | P2 | A feature was built without checking it against the recorded decisions. | *security.custom_role* was removed (migration 026); the three roles stay fixed and the permission matrix of *security.role_permission* is edited. | ADR-015 section 2; endpoint */api/v1/admin/roles-permissions*. | ADR-015 | 2026-10-08 |
| AC-12 | A fixed operator-per-bay assignment had been built, contrary to ADR-010. | P2 | Same as AC-11. | The *service_bay.operator_id* column was reverted (migration 024); the bay is chosen per booking and the operator per execution. | ADR-015 section 1. | ADR-015 | 2026-10-08 |
| AC-13 | Promotions showed a package price that was never applied to the charge. | P2 | The promotions model was used for display only. | Coupons with a real percentage discount, redeemable with points (*POST /api/v1/loyalty/redeem*), and a form without price, duration, or status. | ADR-015 sections 3 and 5. | ADR-015 | 2026-10-09 |
| AC-14 | When a service was edited, its loyalty points went back to 0. | P2 | booking-service binds the field to a primitive *int* and the clients omitted the field. | The web and the app always send *loyaltyPoints*; the app keeps the price of each vehicle type when editing. | ADR-015 section 5; mobile app commits of 2026-10-09. | ADR-015 | 2026-10-09 |
| AC-15 | "Pay" was offered on bookings already paid or under review. | P2 | Each screen repeated the payment rule instead of asking payment-service. | Endpoint *GET /api/v1/payments/me/bookings* with the *payable* flag; the web and the app show the button only with that flag. | ADR-015 section 5. | ADR-015 | 2026-10-09 |
| AC-16 | The notification switches were saved only in the browser or the phone and had no effect. | P2 | There were no columns for those preferences in the account. | Columns in *security.user_preference* (migration 030), partial update of preferences, and application of the switches in notification-service. | ADR-011 section 12. | ADR-011 | 2026-10-09 |
| AC-17 | Theme and language were stored per browser, and a second account on the same device inherited them. | P2 | Preferences were read from *localStorage* without querying the account. | Load after login and save with *GET/PUT /api/v1/users/me/preferences*; palettes accepted by security-service (migration 020). | *core/services/preferences.ts* of the web. | TD-002 | 2026-10-09 |
| AC-18 | The administrator could send any notification type by hand (for example, a fake "payment approved"). | P1 | The manual endpoint did not restrict the type. | Only *SYSTEM_MESSAGE* and *INSPECTION_REPORT* are accepted; any other type answers 400 *NOTIFICATION_TYPE_NOT_ALLOWED*. | ADR-011 section 11. | Security review | 2026-10-09 |
| AC-19 | Null or nonexistent identifiers were accepted when updating the permissions of a role. | P2 | Input validation was missing in the use case. | Rejection with 400 *UNKNOWN_PERMISSION* and a translated message in the web. | security-service commit of 2026-10-08. | ADR-015 | 2026-10-08 |
| AC-20 | The inspection report was shared by WhatsApp, outside the system's channels. | P3 | Earlier product decision. | "Notify customer" button that sends the summary by notification and email (*INSPECTION_REPORT*); WhatsApp was removed from the business data and the help center. | ADR-011 section 11; web commits of 2026-10-09. | ADR-011 | 2026-10-09 |
| AC-21 | The app opened in the browser with Expo (port 8081) was rejected by CORS. | P2 | Origin 8081 was not in the default values. | The default *CORS_ALLOWED_ORIGINS* includes *http://localhost:8081* in every service. | *lavarapido-infra* and gateway commits. | — | 2026-10-09 |
| AC-22 | The old operator tasks route showed an empty page. | P3 | Route without a component after a reorganization. | Redirect to "Assigned services" and removal of the empty page. | Web commit of 2026-10-09. | — | 2026-10-09 |
| AC-23 | Manuals v3.0 became outdated by the changes of October 8 and 9 (points, coupons, refunds, roles, preferences, payments in Docker), existed only in English, and the Installation Manual said to clone the operations repository with a name that breaks the build. | P3 | The documentation was not updated in the same pull requests (risk R-010). | Manuals updated to version 3.1 in Spanish and English, and creation of the Implementation Procedure and of this document. | Version control of each manual (2026-10-09). | R-010 | 2026-10-09 |
| AC-24 | The web test suite did not compile (formerly ACO-01). | P2 | Six scaffolding *.spec.ts* files pointed to classes that no longer existed. | The test files were fixed and tests for the API error messages were added. | *npx ng test --watch=false*: 43 tests in 37 files passed (2026-10-16). | TD-001 | 2026-10-16 |
| AC-25 | There was no login attempt limit (formerly ACO-02). | P1 | RF-004b had not been implemented. | *LoginLockout*: five failed attempts within 15 minutes lock the account for 15 minutes (423 ACCOUNT_LOCKED); a successful login or a password reset clears it. | Changelog 034, *AuthenticationServiceTest* and *ApiSecurityWebTest*; message shown on the web and mobile. | TD-003, RF-004b | 2026-10-16 |
| AC-26 | The acceptance of the Terms and of the Data Processing Policy was not stored on the server (formerly ACO-03). | P1 | The consent table was left pending in ADR-010. | *security.app_user* stores the date and time each document was accepted (*terms_accepted_at*, *data_policy_accepted_at*); web and mobile registration sends *acceptsTerms* and *acceptsDataPolicy*. | Changelog 039, 147 security-service tests passed, checkboxes in both clients. | Law 1581 of 2012 | 2026-10-16 |
| AC-27 | The payment-service health answered *UP* with the database down, and the service did not handle *X-Correlation-Id* (formerly ACO-05). | P2 | The endpoint returned a fixed value. | */health* and */actuator/health* query SQL Server with a 3-second limit; *CorrelationIdMiddleware* takes or creates the identifier and forwards it to booking-service. | With the database stopped the service answers 503 DOWN; 141 payment-service tests passed. | TD-017 | 2026-10-16 |
| AC-28 | The refund texts were fixed in Spanish (formerly ACO-06). | P3 | They were left in a temporary constants file. | Texts moved to the language files in Spanish, English, French, and Portuguese; *payment-texts.ts* was deleted. | Administrator payments screen in the four languages. | Administrator Manual | 2026-10-16 |
| AC-29 | The operator's "Report progress" button said it notified the customer but sent nothing (formerly ACO-07). | P3 | The function was left with only the visual confirmation. | The button was removed on the web and mobile; the customer receives the real start and finish notices. | Assigned services screen without the button. | User Manual | 2026-10-16 |
| AC-30 | The landing page announced a service "wherever you are", and the operator history could show payment methods the system does not support (formerly ACO-08). | P3 | Mockup texts. | The home page describes the service at the car wash with the real establishment data; the operator history no longer shows card or PSE. | Home page in the four languages. | Technical Manual, Annex B | 2026-10-16 |
| AC-31 | An unknown address showed an empty page (formerly ACO-09). | P3 | The wildcard route was missing. | 404 page (*features/not-found*, route *\*\**) with a link to the home page. | A nonexistent address shows the 404 page. | TD-009 | 2026-10-16 |
| AC-32 | The inspection report and its photos were kept only in the browser (formerly ACO-10). | P2 | There was no aggregate in the backend. | *InspectionReport* aggregate in operations-service with phases, findings, and photos (changelog 033); the public link opens on any device and the notice to the customer includes it. | Test *inspection-flow.test.js* of *lavarapido-infra/e2e* passed. | RF-036 | 2026-10-16 |
| AC-33 | The business data of Settings were kept only in the browser (formerly ACO-11). | P3 | The extension of *booking.establishment* waited for the definition of its fields. | Changelog 032 and *GET/PUT /api/v1/admin/establishment*; the home page and the help center read those data. | Changes are visible from another account and on the public page. | TD-013, RF-037 | 2026-10-16 |
| AC-34 | The *lavarapido-infra* README and the team guide described services and screens that already existed as pending (formerly ACO-12). | P3 | Documents not updated when the services were integrated. | Both documents updated. | Commits of 2026-10-16 in *lavarapido-infra*. | R-010 | 2026-10-16 |
| AC-35 | Two simultaneous requests could try to create the same operator, and one failed with error 500. | P2 | The operator creation read and then inserted without handling the race between requests. | The insert runs in its own transaction and, if the row already exists, it is read again instead of failing. | *OperatorPersistenceAdapterTest*; 54 operations-service tests passed. | Review of 2026-10-16 | 2026-10-16 |
| AC-36 | When a time outside the schedule or already past was requested, the system answered "That time was just taken". | P3 | The 409 response did not distinguish the reason. | The response carries *reason* (CLOSED_DAY, OUTSIDE_HOURS, TIME_PASSED, or NO_FREE_BAY), and the web and mobile show a message for each case. | Test *access-rules.test.js* (*reason: OUTSIDE_HOURS*) and *api-error.spec.ts*. | Review of 2026-10-16 | 2026-10-16 |
| AC-37 | The "Delete account" option said it erased the account and all the data, but it only deactivates it. | P2 | Text inherited from the mockup, contrary to what the server does. | The option is called "Deactivate my account" and explains that the history is kept, on the web and mobile and in the four languages. | Web and mobile profile; User Manual 4.0. | Law 1581 of 2012 | 2026-10-16 |
| AC-38 | The manuals and project documents became outdated with respect to the code of October 16 (lockout, automatic assignment, inspection, 57 tables), and the figures were placeholders. | P3 | Changes integrated without updating the documentation in the same pull request (R-010). | Manuals 4.0 with real screenshots, Implementation Procedure 2.0, this document 2.0, and the project's technical documentation reviewed against the code. | Version control of each document (2026-10-16). | R-010 | 2026-10-16 |
| AC-39 | With two accounts of the same method (for example, two Nequi), the web payment screen marked both at once and always showed the QR of the first one. | P3 | The chosen option was stored by method type and not by account. | The selection is stored by account and, if two accounts share a method, each option shows its holder. | *payment.spec.ts* (two Nequi accounts); 43 web tests passed. | Test Documentation, defect 6 | 2026-10-16 |
| AC-40 | When logging out, the web and the app showed "Your session expired". | P2 | A 401 that arrived after the token was deleted was taken as an expired session. | A 401 only ends the session with a notice while a session is still open (*auth-interceptor* on the web and *AuthServiceContext* in the app). | The notice no longer appears when logging out; it does when the token really expires. | Usage report | 2026-10-16 |
| AC-41 | On a phone (360 px) there were buttons off the screen, overlapping titles, the ☰ button over the titles, and filters outside their card. | P2 | Styles designed for desktop, without phone rules, and a fixed 20 px line height inherited from the Material theme. | Phone rules in the landing, authentication, customer dashboard, assigned services, management, and settings; global room for the ☰ button and a relative line height for titles. | 60 web screens (360 and 768 px) and 26 app screens with no overflow (tests, Table 5b). | Responsive design check | 2026-10-17 |
| AC-42 | In the app, the date and search inputs were squashed when placed in a column. | P3 | The box used *flex: 1*, which starts from a height of 0 in a column. | It grows only in width and keeps a minimum height of 46 px (*FilterInputs.tsx*). | History and Ratings show the full inputs. | Responsive design check | 2026-10-17 |
| AC-43 | The next service progress showed 10% or 25% although the wash had not started. | P3 | The progress table gave a percentage to the Scheduled and Confirmed statuses. | Scheduled and Confirmed stay at 0% on the web and in the app. | The dashboard shows 0% until the operator starts the service. | Usage report | 2026-10-16 |
| AC-44 | A token kept working up to an hour after logout or after the administrator disabled the account. | P2 | Each service only checked the JWT signature and expiry (ADR-006); nobody asked whether the session was still open. | security-service rejects the token of a closed session (*sid* claim, *ActiveSessionValidator*) and the gateway confirms it with *GET /api/v1/auth/session* before passing the request on, keeping the answer 30 seconds per token. | *SessionCheckFilterTest*, *ApiSecurityWebTest* (401 with the token of a closed session); 19 end-to-end tests with the check on. | TD-024 | 2026-10-21 |
| AC-45 | Bookings nobody started stayed Scheduled or Confirmed forever, and each admin screen counted "without an operator" its own way. | P2 | There was no close for expired bookings and the "without an operator" rule was repeated in the screens. | *ExpiredBookingsJob* cancels every 5 minutes, with the *EXPIRED* reason, a Scheduled booking one hour past its end without being confirmed; Confirmed ones are handled as AC-53 describes. *GET /api/v1/admin/assignments/unassigned* is the single count of bookings without an operator, on the web and in the mobile app. | *BookingTest*, *BookingServiceTest*, *OperationsServiceTest*, *reservations-store.spec.ts*. | TD-025 | 2026-10-21 |
| AC-46 | A manual and an automatic assignment at the same time could give an operator two services at the same time. | P2 | Both assignments read the operator schedule and saved without coordinating. | Both take the same SQL Server lock (*sp_getapplock* on *operations-assignment*) before reading and saving. | *OperationsServiceTest* checks that the lock is taken before saving. | TD-026 | 2026-10-21 |
| AC-47 | The server accepted payment receipts of any size, and a phone photo of several MB was stored as it was in the database. | P3 | The size limit was not in the payment domain. | payment-service rejects a receipt over 2 MB (*RECEIPT_TOO_LARGE*) and the web and the app compress it before sending it. | *PaymentTests* (over 2 MB and exactly 2 MB). | Review of 2026-10-21 | 2026-10-21 |
| AC-48 | The customer saw the Cash option even when the administrator had disabled that account. | P3 | *GET /api/v1/payment-accounts* did not return the cash account and the web and the app always added it on their own. | The API returns the cash account while it is active and the clients show Cash only if it comes in the list. | Payment screen with the cash account active and disabled. | Software Design, finding 8 | 2026-10-21 |
| AC-49 | The Reports cards and charts counted bookings that had not been finished as services done. | P3 | The count took the bookings by date without looking at their status. | Only completed bookings count. | *reports.spec.ts*. | Review of 2026-10-21 | 2026-10-21 |
| AC-50 | The roles tab promised that the permissions define what each user can do. | P3 | Real authorization uses the role in the token and the permission matrix is for reference (ADR-015), but the text did not say so. | The tab and the dialog explain that the roles are fixed and that the role decides the access. | *management.spec.ts* (fixed roles). | ADR-015 | 2026-10-21 |
| AC-51 | After signing out or signing in with another account in one tab, the other browser tabs kept showing the previous session. | P3 | Each tab read the session only when it opened. | The tabs listen to the *storage* event: if another one signs out they go back to sign-in, and if another account signs in they reload. | *auth.spec.ts* (tabs). | Review of 2026-10-21 | 2026-10-21 |
| AC-52 | The transaction log of the server database grew with no limit. | P2 | The database used the full recovery model without transaction log backups. | The database moves to the simple recovery model and is backed up in full every day (AP-04). | *RECOVERY SIMPLE* on the server; *lavarapido-infra*, commit of 2026-10-21. | R-008 | 2026-10-21 |
| AC-53 | The first version of AC-45 set to No-show every Confirmed booking nobody started one hour after its end. If the operator washed the car and forgot to press "Start", the history, reports, and metrics recorded that the customer did not come, and No-show is final. | P1 | The rule decided a final status on its own without knowing whether the service was done: the system cannot tell a no-show from a forgotten record when the booking has an operator. | The system only decides when it is sure: a Confirmed booking that never had an operator becomes No-show (operations-service asks booking through *POST /internal/v1/bookings/{id}/no-show*, which checks again that it expired); one with an operator that nobody started or finished goes to the administrator's "To close" list, on the web and in the mobile app, who closes it as "Attended" (without made-up times and without telling the customer to pick up the vehicle) or as "No-show"; the operator and the administrators get a single notice (migrations 040 and 041). | *FollowUpPolicyTest*, *FollowUpServiceTest*, *BookingServiceTest*, *BookingApiWebTest*, *reservations-store.spec.ts*; live test of October 21 on the web and in the mobile app. | Team review of 2026-10-21 | 2026-10-21 |
| AC-54 | A `null` field in an event payload sent the whole message to notification-service's dead-letter queue (DLQ), and the notice was not created. | P2 | Reading the event envelope failed on a `null` value instead of ignoring it. | The `null` field is ignored and the rest of the message is processed. | *DomainEventEnvelopeTest*. | R-005 | 2026-10-21 |
| AC-55 | The variables of October 21, 2026 (*SESSION_CHECK_\**, *BOOKING_EXPIRY_\**, and *FOLLOW_UP_\**) were not in *.env.example* or in the *environment* block of *docker-compose.yml*; in Docker only their defaults applied (formerly ACO-14). | P3 | They were added to the *application.yml* of each service without updating *lavarapido-infra*. | The nine variables, including *FOLLOW_UP_LOOK_BACK_DAYS*, are commented out in *.env.example* and *.env.production.example*, and the compose file passes them to *api-gateway*, *booking-service*, and *operations-service*. | *lavarapido-infra*, commit *70b990c*; *docker compose config* shows them (verified on 2026-10-23). | ACO-14 | 2026-10-22 |
| AC-56 | The gateway published */api/v1/operator/bookings/\** and booking-service let an operator start or finish any booking without checking that they were assigned or the 15-minute rule, and without publishing the execution events (E-01). | P1 | The route meant for operations-service's internal call was left published, and booking treated staff as administrators. | The gateway stops publishing the route; booking requires the internal key on the operator routes and applies the 15 minutes; operations-service sends the key. | Commits *b9107aa* (gateway, 404 test), *a73467d* (booking), *144a0c6* (operations), and *f07802a* (infra); CI green. | Review of 2026-10-22 (E-01, OPS-02, SEC-02, BIZ-03) | 2026-10-23 |
| AC-57 | Removing the administrator role in the database did not cut their token, which kept working for up to an hour (E-02). | P2 | The session was checked by its identifier (*sid*), not by the token's roles. | *ActiveSessionValidator* compares the token's roles with *security.user_role* and, if the token carries a removed role, rejects it and revokes the sessions. | security-service, commit *579480e* (*AuthenticationServiceTest*, *ApiSecurityWebTest*). Its effect is limited by ACO-15. | Review of 2026-10-22 (E-02, SEC-03) | 2026-10-23 |
| AC-58 | The default profile was *dev*, and the passwords of the demo accounts and of SQL Server were in the code, the team guide, the compose file, and payment-service's README (E-05, H-06, H-07, and H-08). | P2 | Convenience of the local environment. | security-service no longer sets the *dev* profile; demo passwords are read from *DEMO_ADMIN_PASSWORD*, *DEMO_OPERATOR_PASSWORD*, and *DEMO_CLIENT_PASSWORD* (empty: the account is not created); infra and payment have no literal passwords. | Commits *e952fe2* (security), *f0800ef* (infra), and *1c7df54* (payment). The old password is still in payment's history and *main*, a demo password is still written in an example of *GUIA-EQUIPO.md*, and *payment-migrate* receives the password as an argument: ACO-25. | Instructor evaluation (H-06 to H-08) | 2026-10-23 |
| AC-59 | A 100 % coupon or a fixed discount greater than or equal to the total left the booking with amount 0, which the payment does not accept: the booking could not be paid (E-07). | P1 | The domain accepted 100 % and did not cap the fixed discount. | The percentage goes from 1 to 99 and the fixed discount is capped at the total minus 1 peso; the web and the app limit the form to 99 %. | Commits *827746f* (payment), *1175eb0* (web), and *c0cd099* (mobile). BIZ-04 and BIZ-05 remain: ACO-20. | Review of 2026-10-22 (E-07, RF-024) | 2026-10-23 |
| AC-60 | "Remove coupon" only removed it from the screen: the server kept subtracting the redemption (E-08, B-05). | P2 | There was no way to cancel a redemption. | *DELETE /api/v1/loyalty/redemptions/{bookingId}/{promotionId}* (only the owning customer; 409 if there is already a payment), used by the web and the app. | Commits *6e2df05* (payment), *2158196* (web), and *ce630a5* (mobile). After reloading, the customer does not see the redemption: ACO-17. | Review of 2026-10-22 (E-08) | 2026-10-23 |
| AC-61 | A booking could accumulate several coupons (E-09). | P2 | The rule and the database index were missing. | One promotion per booking and a unique index. | payment-service, commit *6e2df05* and migration *021-promotion-one-per-booking.sql* (with *onFail: CONTINUE*: before deploying, check that no booking has two coupons). | Review of 2026-10-22 (E-09) | 2026-10-23 |
| AC-62 | The @gmail email rule was only in some forms and the server accepted any domain (A-01). | P2 | The rule was placed in the clients and not on the server. | security-service validates *ALLOWED_EMAIL_DOMAINS* (400 *EMAIL_DOMAIN_NOT_ALLOWED*) and the web and the app apply the same rule in every email form. | Commits *bef15d5* (security), *fed8465* (infra), *9f24ce8* (web), and *ee6e339* (mobile). Caveat in ACO-32: the server does not restrict sign-in, but the web and the app do, so an account already created with another domain cannot sign in. | Review of 2026-10-22 (A-01, SEC-08) | 2026-10-23 |
| AC-63 | The web did not allow reassigning a booking's operator (A-02). | P2 | The Assign button only appeared without an operator. | Assign also appears with an operator, in the list and in the detail. | Web, commit *eb3e16d*. | Review of 2026-10-22 (A-02, RF-009) | 2026-10-23 |
| AC-64 | The notes for the operator when assigning were discarded (B-01). | P3 | The assignment contract did not have the field. | operations-service stores the notes and the web sends them. | Commits *cf28fbe* (operations, migration 042) and *dbe0a49* (web). Caveat in ACO-32: the operator still does not see the notes. | Review of 2026-10-22 (B-01) | 2026-10-23 |
| AC-65 | Manual assignment did not check whether the operator's account was deactivated, and rescheduling kept the operator without validating them again (A-13, E-12). | P2 | Only automatic assignment checked the account. | The active account is validated when assigning and the operator is validated again when rescheduling; the web and the app show the deactivated-account message. | Commits *e94319c* and *c653b4e* (operations), *5f4377c* (web), and *437bd03* (mobile). | Review of 2026-10-22 (A-13, E-12) | 2026-10-23 |
| AC-66 | Status changes made by the administrator did not notify the customer (A-11). | P3 | booking-service published no event on that change. | booking publishes the event and notification-service notifies the customer. | Commits *369bd85* (booking) and *f9c9adf* (notification). Caveat in ACO-32: that change does not cancel the reminders. | Review of 2026-10-22 (A-11) | 2026-10-23 |
| AC-67 | A booking's loyalty points changed if the administrator changed the service's points (A-09). | P2 | The booking line did not store the points. | The points are frozen on each booking line. | booking-service, commit *8926287* (migration 043). | Review of 2026-10-22 (A-09) | 2026-10-23 |
| AC-68 | The cancellation reason chosen by the administrator was ignored (A-20, H-24). | P3 | The controller called the cancellation without the reason. | booking uses the chosen reason and the web asks for it. | Commits *5c23630* (booking) and *48e60e8* (web). | Instructor evaluation (H-24) | 2026-10-23 |
| AC-69 | The web's revenue was calculated by the report date and added up every year, and the operators' "In service" status was not calculated (A-17, A-19). | P3 | Calculations made with the wrong data. | Revenue by approval date and calculated status. | Web, commit *3c02a4d*. | Review of 2026-10-22 | 2026-10-23 |
| AC-70 | The operator's history and assigned services showed fake or empty data on the web (A-18). | P3 | Test data remained in the ViewModel. | Real data from the server. | Web, commit *b20d3a9*. Caveat in ACO-32: the payment method and the status in the history are still fixed values. | Review of 2026-10-22 | 2026-10-23 |
| AC-71 | A plate longer than 6 characters was cut instead of rejected (E-16). | P3 | The value object truncated the text. | It is rejected with a validation error. | customer-service, commit *645fa5c*. Caveat in ACO-32: a long plate already in the database breaks reading that vehicle. | Review of 2026-10-22 (E-16) | 2026-10-23 |
| AC-72 | The documentation became outdated after *v1.0.0*: it said there were no tags, cloned and rolled back with nonexistent tags, used *COMPRESSION* in the backup, did not document the mobile app for the user or the MVVM pattern, and this register did not have the real nonconformities (DOC-02 to DOC-16; A-03 to A-08, B-02, B-06, C-01 to C-03). | P3 | The documentation was not reviewed after the changes of October 22 and 23. | Review of documents 01, 02, 04 to 11, the README, and the CHANGELOG, in Spanish and English. | *lavarapido-docs*, branch *docs/update-october-23* (includes Merari Urbano's *fix/\** branches). The PDF and Word files are still to be regenerated. | R-010 | 2026-10-23 |

*Note.* Prepared by the authors from the Git history of the repositories, the risk register, and the ADRs of the project (Vehicle Washing Development Team, 2026a). AC-56 to AC-71 are in *develop* since October 23, 2026, with the CI green, and reach the server with version *v1.1.0*.

## 10. Register of Open Corrective Actions

**Table 7**

*Open Corrective Actions*

| ID | Nonconformity | Sev. | Root cause | Proposed action | Responsible | Priority | Closure criterion |
|---|---|---|---|---|---|---|---|
| ACO-04 | The table *audit.audit_log* exists but nothing writes to it. | P2 | The triggers were not created and *SESSION_CONTEXT(N'user_id')* is not set. | Audit triggers on the sensitive tables and session context in each service, or remove the table from the design through an ADR. | Backend leader | Medium | Changes of prices, payment accounts, and roles visible in the audit trail. |
| ACO-13 | Entities edited by administrators do not use optimistic locking: in concurrent edits, the last write wins. | P3 | The *row_version* column exists but is not mapped with *@Version*. | Map *@Version* in booking, customer, and security and answer 409 on conflict. | Backend leader | Low | Test of two updates with the same version. (TD-008) |
| ACO-15 | If the header says *bearer* in lowercase, the gateway does not check the session and the services other than security-service accept, for up to an hour, the token of a closed session (logout, deactivation, password change or recovery, removed role) (SEC-01). | P1 | *SessionCheckFilter* only checks headers that start exactly with *Bearer *, while Spring Security and .NET accept any case. | Compare ignoring case (*regionMatches(true, …)*) or check every request with *Authorization*, with its test in *SessionCheckFilterTest*. | Project leader | High | A request with *bearer* in lowercase and a closed session answers 401. |
| ACO-16 | A paid booking, or one whose payment is under review, can be rescheduled with other services and the payment is not told: the approved amount does not match what was done (BIZ-01). | P1 | booking accepts *serviceIds* when rescheduling without looking at the payment, and payment fixes the amount when reporting and does not recalculate it when approving. | When approving, compare the amount with the one owed today (409 *AMOUNT_CHANGED*); the customer only changes date and time, and the administrator gets a warning. | Frontend leader (booking-service) and backend leader (payment-service) | High | A test that reschedules with another service and does not allow approving the payment with the old amount. |
| ACO-17 | The customer cannot see the amount the server charges: if they open the payment again after redeeming a coupon, the web and the app show the full total and do not offer to remove it (BIZ-02, remainder of E-08). | P2 | The amount due is only exposed by an administrator route and the clients calculate it with their own state. | A customer route with the amount due and the redeemed coupon (or the data in */payments/me/bookings*), used by the web and the app. | Backend leader | High | Reloading the payment screen with a redeemed coupon shows the discounted total and allows removing it. |
| ACO-18 | Finishing a service is not atomic with booking-service: if booking saves but takes more than 3 seconds or saving the execution fails, the booking is completed and the line stays in progress, and the operator is blocked (OPS-01). | P2 | operations calls booking before saving its own state. | Save first and, on a 409 from booking, read again and treat the change as done if it was already applied. | Project leader | High | A test with a slow or partially failing booking that does not leave the execution in progress. |
| ACO-19 | Continuous deployment has never run: the secrets are missing (*AZURE_SSH_KEY*, *DEPLOY_DISPATCH_TOKEN*), the branches are not merged, and the virtual machine is usually off, so the public URL may not answer (CD-01, H-15). | P2 | The workflow was prepared on October 23, 2026 without a window with the machine on. | Merge *lavarapido-infra* first, create the secrets, install the key on the server, run the workflow twice by hand, and leave the machine on and a backup video for the presentation. | Project leader | High | A test merge into *main* deploys green, *crontab -l* shows *boot-update*, and the URL answers 200. |
| ACO-20 | Some bookings still cannot be paid: a price of 0 in the catalog, and a discount that is frozen in pesos and exceeds the total if the booking is rescheduled to a cheaper service (BIZ-04, BIZ-05). | P2 | The catalog accepts price 0 and the redemption stores the discount value, not the percentage. | Price greater than zero and recalculate the discount on the current total. | Frontend leader (booking-service) and backend leader (payment-service) | Medium | Tests for price 0 and for rescheduling with a coupon. |
| ACO-21 | Events and notices can be lost without warning: they are published after the commit with only a log entry, operations-service's queue has no dead-letter queue, and emails and push are not retried (OPS-04, OPS-05, H-11). | P2 | Risk accepted in ADR-004 (no Outbox). | Publisher confirms, a dead-letter queue in operations, and a pending-deliveries table with retries; or keep the accepted risk with monitoring. | Project leader | Medium | Turning RabbitMQ off during a booking and on again delivers the assignment and the notices. |
| ACO-22 | There is no request limit on sign-in or password recovery: anyone can lock an account with 5 attempts and the answers reveal which accounts exist (SEC-04, E-04). | P2 | No limit was configured in the gateway or in Caddy. | A per-IP limit on */api/v1/auth/\** and equal answers for accounts that exist and that do not. | Project leader | Medium | A test that gets 429 after passing the limit. |
| ACO-23 | The server does not require the Law 1581 consent when signing up: only the forms ask for it (SEC-07, E-03, RF-001). | P2 | *RegisterRequest* does not validate the acceptance fields. | Validate the acceptance on the server and adjust the test. | Project leader | Medium | Sign-up without acceptance answers 400. |
| ACO-24 | payment-service and the mobile app have no *v1.0.0* version (their *main* dates from September 30 and July 6, 2026) and no branch protection; *develop* is not protected in any repository (H-01, H-02). | P2 | payment's PR #2 has no review and its SonarCloud quality gate fails on four false positives; the app has no PR. | Mark the false positives, fix the README, review and merge PR #2, and tag; PR *develop* → *main* for the app and tag *v1.1.0*; protect *main* and *develop*. | Backend leader | High | Tag in the 10 repositories and *main* protected. |
| ACO-25 | Secrets are still exposed: the old development SQL Server password in payment-service's history and *main*, and the Firebase key in *google-services.json* (BIZ-11, H-09). | P2 | They were committed at the start of the project. | Rotate the password and restrict the Firebase key by package and SHA-1 fingerprint. | Backend leader | Medium | The old password no longer works and the key only works for the app. |
| ACO-26 | The tests do not cover the important end-to-end paths: the *e2e* tests do not run in the CI, payment's 7 integration tests are skipped, the app has only 13 tests, and no CI measures coverage (F-01 to F-05, H-03, H-04, H-13). | P2 | The CI does not start SQL Server or RabbitMQ. | A CI workflow with the containers that runs *e2e* and the integration tests, and coverage for the web and the app. | Development team | Medium | The workflow is green and publishes the coverage. |
| ACO-27 | Two simultaneous payment reports can leave two payments under review, and the transaction reference is not unique in the database (A-16, BIZ-09, RF-016). | P2 | The rule is checked in the application without a lock or unique index. | Filtered unique index for the open payment and for the reference. | Backend leader | Medium | A concurrency test with two reports at the same time. |
| ACO-28 | The EAS *production* profile does not set the server URL and the app allows unencrypted traffic in all its builds (MOV-08, MOV-11, H-14). | P3 | Only the *preview* profile defines the address. | Define the HTTPS URL in *production* and remove *usesCleartextTraffic*. | Backend leader | Low | A *production* APK calls the HTTPS URL. |
| ACO-29 | Rolling back on the server is manual and global: the scripts do not keep the previous image, restoring returns the whole database and does not run *payment-migrate*, and old images are not cleaned up (CD-10, CD-11). | P3 | The scripts were designed to update, not to go back. | Tag *:prev* before building, *docker image prune* afterwards, and a short rollback procedure. | Project leader | Low | Going back to the previous version without building. |
| ACO-30 | There are no issues or tracking board in the repositories (H-22). | P3 | Tracking was kept in documents. | One issue per user story, linked PRs, and a GitHub Projects board. | Development team | Medium | Each PR closes an issue and the board shows the status. |
| ACO-31 | The role permission matrix is saved but not applied when authorizing (H-05). | P3 | Authorization uses the token's role (ADR-015); the screen already says so (AC-50), but it still saves. | Remove the saving or apply the matrix with a 403 test. | Project leader | Low | The screen does not save changes, or removing a permission gives 403. |
| ACO-32 | Caveats of the fixes of October 23, 2026: the operator does not see the assignment notes and reassigning without notes erases the previous ones (B-01); a status change by the administrator does not cancel the reminders (A-11); existing accounts with another email domain cannot sign in on the web or in the app (A-01); a plate longer than 6 characters already in the database breaks reading that vehicle (E-16); the operator's history keeps the payment method and the status fixed (A-18); and French and Portuguese texts for reassignment and the cancellation reason are missing. | P3 | The fixes were made on the same day as the review, with tests for the main case. | Complete each fix and, before releasing *v1.1.0*, check in the database the accounts that are not @gmail.com and the long plates. | Development team | Medium | Each caveat with its test and both queries without problem rows. |

*Note.* Prepared by the authors from the technical backlog, Annex B of the Technical Manual, and the verification of the code as of October 16, 2026. Actions ACO-01 to ACO-03 and ACO-05 to ACO-12 were closed and moved to Table 6 (AC-24 to AC-34), and ACO-14 moved as AC-55 on October 23, 2026. ACO-15 to ACO-32 were recorded that day from the system review, the verification of that day's fixes, and the instructor's evaluation (Annex D). ACO-13 also covers the lack of optimistic locking in operations-service's executions and booking-service's bookings (OPS-03, BIZ-09).

## 11. Register of Preventive Actions

Preventive actions address the causes of risks that have not yet materialized or that could recur.

**Table 8**

*Preventive Actions*

| ID | Risk or potential cause | Preventive action | Responsible | Priority | Status | Origin |
|---|---|---|---|---|---|---|
| AP-01 | Regressions reach *develop* unnoticed. | Continuous integration per repository (*./mvnw verify*, *dotnet test*, *ng build*, *ng test*, and *tsc*) and the rule of merging only with a green result. | Project leader | High | Closed (2026-10-19): GitHub Actions in the 10 repositories, on every push or pull request to *develop* and *main* | R-003, TD-006 |
| AP-02 | An event is lost between the commit and the publication. | Outbox pattern in security, booking, operations, and payment. | Backend leader | Low | Accepted as a risk until leaving the academic scope | R-005, TD-011 |
| AP-03 | Secret leakage (*.env*, mail app password, *JWT_SECRET*). | Keep *.env* ignored, check with *git check-ignore* before each implementation, and rotate secrets every quarter or on suspicion. | Whole team | High | In progress (permanent) | R-004 |
| AP-04 | Data loss before a demonstration or in operation. | Automated daily backup with verification and a restoration test (Administrator Manual, section 14). | IT administrator | High | Closed (2026-10-21): *backup-db.sh* backs up the database every day and before every update, *verify-backup.sh* restores each backup under another name to check it, and the last 14 are kept (Deployment Document) | R-008 |
| AP-05 | The documentation drifts from the code again. | Pull request checklist that requires updating the affected models, OpenAPI contracts, ADRs, and manuals; review of the manuals before each implementation. | Author of each pull request | Medium | In progress (permanent) | R-010 |
| AP-06 | Implementing with *MESSAGING_ENABLED=false*, without *INTERNAL_API_KEY*, or with the *dev* profile. | Checklist of Annex A of the Implementation Procedure. | IT administrator | Medium | Closed (included in the procedure) | R-I02, R-I03 |
| AP-07 | Persistence defects (locks and triggers) seen only by hand. | Persistence tests with Testcontainers and a real SQL Server in booking-service. | Backend leader | Low | In progress (the end-to-end suite covers part of the risk) | TD-010 |
| AP-08 | All services use the *sa* account. | One login per service with permissions only on its schemas and a separate account for the migrations. | Backend leader | Medium | Open | Security policy |
| AP-09 | A user action cannot be followed across services. | Propagate *X-Correlation-Id* in all REST clients and messages and generate it in the gateway. | Backend leader | Low | In progress (booking, operations, and payment already forward the header) | TD-007 |
| AP-10 | Lack of metrics to check the response time (RNF-001). | *micrometer-registry-prometheus* in the Java services and equivalent metrics in .NET. | Backend leader | Low | Open | TD-012 |
| AP-11 | Brute-force attacks or API abuse if the system is exposed. | Request rate limit in the gateway or in Caddy (TD-022); account lockout is already active (AC-25). | Backend leader | Medium | Open | Security policy |
| AP-12 | Components with known vulnerabilities. | Quarterly review with *./mvnw versions:display-dependency-updates*, *dotnet list package --vulnerable*, and *npm audit*. | Backend and frontend leaders | Medium | In progress (permanent) | OWASP A06 |
| AP-13 | Confusion caused by the own numbering of the payment changelogs, which repeats the global numbers. | Document the rule in the migration strategy and use the *pay-* prefix in the identifiers. | Backend leader | Low | Closed (documented) | TD-019 |
| AP-14 | Features built that contradict decisions already recorded (cause of AC-11 and AC-12). | Review the current ADRs and the navigation map before starting a feature, and consult the team when there is a contradiction. | Whole team | Medium | In progress (permanent) | Lesson of ADR-015 |
| AP-15 | Interface changes that break the phone layout without anyone noticing (cause of AC-41). | Measure the screens at 360 and 768 px with Playwright before merging interface changes, starting from the *e2e/width-360.js* script, and review the screenshots. | Frontend and backend leads | Medium | In progress (permanent) | Lesson from AC-41 |
| AP-16 | Container logs filling the server disk. | Cap the logs of each container at 3 files of 10 MB. | Project leader | Medium | Closed (2026-10-20): *docker-compose.prod.yml* | Server review |
| AP-17 | Browser-side attacks against the public site (embedding it in another page, loading scripts from other origins). | Security headers and a content security policy (CSP) in Caddy. | Project leader | Medium | Closed (2026-10-20): *deploy/Caddyfile* | OWASP A05 |
| AP-18 | A container hanging without anyone noticing. | Health check every 30 seconds in every container, visible in *docker compose ps*. | Project leader | Medium | Closed (2026-10-20): *docker-compose.prod.yml* | Server review |
| AP-19 | An automatic job recording a final status with incomplete data (cause of AC-53). | Every automatic rule that changes a final status only acts when there is no doubt; anything doubtful goes to a list for a person to decide, and the rule is reviewed by the team before merging it. | Whole team | High | In progress (permanent) | Lesson from AC-53 |

*Note.* Prepared by the authors from the risk register, the technical backlog, and the security policy of the project.

## 12. Register of Improvement Actions

**Table 9**

*Improvement Actions*

| ID | Improvement opportunity | Expected benefit | Responsible | Priority | Status | Origin |
|---|---|---|---|---|---|---|
| AM-01 | Automatic operator assignment when a booking is confirmed, reusing *AssignmentPolicy*. | The administrator stops assigning every booking by hand (RF-008). | Backend leader | Medium | Closed (2026-10-16): *BookingConfirmedListener* and *AutoAssignmentPolicy*, with the optional choice of the customer; test *booking-flow.test.js* | TD-020, ADR-014 |
| AM-02 | Apply the permission matrix of *security.role_permission* to the real authorization of each endpoint. | Granular access control configurable from the panel. | Backend leader | Low | Open (requires an ADR) | ADR-015 |
| AM-03 | Rescheduling of bookings by the customer from the web and the app (the API already offers *PUT /api/v1/bookings/{id}*). | The customer does not have to cancel and book again. | Frontend leader | Medium | Open | User Manual |
| AM-04 | Complete the mobile application and build a version with EAS for push notifications. | Immediate notices on the phone. | Frontend leader | Medium | Closed (2026-10-16): APK built with EAS and published at */app/* on the server, with push notices of new versions | ADR-011 |
| AM-05 | RS256 signing and refresh tokens. | Lower impact of a secret leak and longer sessions without logging in again. | Backend leader | Low | Open | ADR-006 |
| AM-06 | Store receipts, QR codes, and photos outside the database. | Lighter database and faster backups. | Backend leader | Low | Open | Recommended evolution |
| AM-07 | Separate the display fields and the real discount fields in *promotion.promotion*. | Prevents the displayed package and the applied discount from contradicting each other. | Backend leader | Low | Open | ADR-015 |
| AM-08 | Publish the built web application behind the gateway with HTTPS. | Production-ready environment, without a development server. | Frontend leader | Medium | Closed (2026-10-16): web container with nginx behind Caddy and HTTPS on the public server (Deployment Document) | Implementation Procedure, R-I08 |
| AM-09 | Coverage (JaCoCo) and static analysis (SonarQube) tools. | Objective code quality metrics. | Project leader | Low | Open | Testing strategy |
| AM-10 | Automated end-to-end test across services (registration → booking → notification → payment). | Early detection of integration failures. | Backend leader | Medium | Closed (2026-10-16): *lavarapido-infra/e2e*, 19 tests passed against the containers | Testing strategy |
| AM-11 | Replace the figure placeholders of the manuals with real screenshots of the final version. | Complete manuals according to the SENA guide. | Frontend leader | High | Closed (2026-10-16): manuals 4.0 with real screenshots of the system | Annex A of each manual |
| AM-12 | Use the execution statuses *PAUSED* and *WITH_ISSUE* in the operator interface. | Record pauses and issues of the service. | Frontend leader | Low | Open | Data model |
| AM-13 | Expose in the panel the sending of general announcements (*SYSTEM_MESSAGE*) to groups of users. | Direct communication with customers and operators without using the API. | Frontend leader | Low | Open | Administrator Manual |
| AM-14 | Manage the inspection report from the mobile app. | The administrator records the vehicle condition next to the vehicle, with camera photos shrunk on the phone. | Backend lead | Medium | Closed (2026-10-17): *AdminInspection* screen in the app | Team request |
| AM-15 | Frequently asked questions on the home page. | Visitors solve the most common doubts (booking, payment, cancellation, points) without writing to the car wash. | Backend lead | Low | Closed (2026-10-17) | Landing review |
| AM-17 | Continuous deployment: every approved merge into *main* reaches the server on its own and, when the machine is turned on, what came in while it was off is deployed. | Nobody logs in over SSH to deploy and the server does not fall behind *main*. | Project leader | High | In progress (2026-10-23): prepared in the *ci/continuous-deployment* branch of *lavarapido-infra* and in *ci/request-deploy* of five repositories, not merged or tested live (ACO-19) | Review of 2026-10-23 |
| AM-18 | Behavior tests in the clients. | Catch the web's and the app's errors in time. | Development team | High | In progress (2026-10-23): the web went up to 146 tests in 59 files (guard, interceptor, and the sign-up, payment, and dashboard ViewModels) and the app has its first 13 with *jest-expo* in the CI (ACO-26) | Instructor evaluation (H-03, H-04) |
| AM-16 | Require installing the new APK when there are native changes that do not arrive over the internet. | Nobody keeps using an app version without the fixes that depend on the APK. | Backend leader | Medium | Closed (2026-10-21): a screen that only lets the user download the published APK if its *versionCode* is higher; if the server does not answer, the app goes on | Review of 2026-10-21 |

*Note.* Prepared by the authors from the recommended evolution of the Technical Manual, the ADRs, and the limitations documented in the manuals.

## 13. Follow-Up Indicators

**Table 10**

*Action Management Indicators*

| Indicator | Formula | Target | Value as of 2026-10-21 |
|---|---|---|---|
| Closed corrective actions | Closed corrective actions / recorded corrective actions × 100 | ≥ 70% per delivery | 72 / 92 = 78% (on 2026-10-21 it was 54 / 57) |
| Open P0 and P1 corrective actions | Number of ACO with severity P0 or P1 | 0 before an implementation | 2 (ACO-15 and ACO-16, both P1) |
| On-time closure | Actions closed within the time of their severity / closed actions × 100 | ≥ 90% | To be measured from version 1.0 |
| Recurrence | Closed corrective actions whose problem reappears / closed corrective actions × 100 | 0% | 0% |
| Escaped defects | Defects found in acceptance or operation / total defects of the period × 100 | Downward trend | To be measured from the first implementation |
| Automated tests | Tests run and passed in every repository | Increasing | 825 unit and integration tests in the latest *develop* CI of October 23, 2026 (web 146, gateway 39, Java services 489, and payment-service 151, with 7 integration tests skipped) and 13 in the mobile app; 19 end-to-end tests on October 21 and 42 functional cases on October 19 |

*Note.* Prepared by the authors. The test count corresponds to the latest *develop* CI of each repository on October 23, 2026 (in *v1.0.0*, that same day, there were 757; on October 21, 707); version 1.0 counted annotations (about 400). The recorded corrective actions count AC-01 to AC-72 and the open ACOs.

The project leader reviews the indicators at each retrospective and before each implementation. As of October 23, 2026 there are 20 open corrective actions (ACO-04, ACO-13, and ACO-15 to ACO-32). Two are P1 (ACO-15, the session that is not checked with *bearer* in lowercase, and ACO-16, the amount of a paid booking that is rescheduled), so **entry criterion E6** of the Implementation Procedure **is not met** until they are closed or the project leader records an exception with its mitigation. The rest are P2 and P3 and have a recorded action.

## 14. Lessons Learned

**Table 11**

*Lessons Learned*

| No. | Lesson | Related actions |
|---|---|---|
| L-01 | Storing time in UTC and converting it only at the edges prevents time shifts. | AC-01 |
| L-02 | A service must not start before its dependencies are healthy; the orchestration must guarantee it. | AC-02 |
| L-03 | Agreeing on the data model before coding a service prevents duplicate implementations. | AC-03 |
| L-04 | Every decision already recorded in an ADR must be reviewed before building; a contradiction is discussed before coding. | AC-11, AC-12, AP-14 |
| L-05 | A business rule must live in a single service, and the screens must query it, not repeat it. | AC-15, AC-45 |
| L-06 | A preference that the user changes must be saved in their account to have an effect. | AC-16, AC-17 |
| L-07 | A new service is not finished until it has a container, a gateway route, Compose variables, and published events. | AC-04, AC-05, AC-06 |
| L-08 | Administrative endpoints also need strict input validation and allowlists. | AC-18, AC-19 |
| L-09 | Documentation is updated in the same pull request as the code; otherwise, it becomes outdated within days. | AC-23, AP-05 |
| L-10 | An accounting ledger needs reversal movements and concurrency control from day one. | AC-09 |
| L-11 | A "create if it does not exist" operation must handle the race between two simultaneous requests. | AC-35 |
| L-12 | Each interface option must say exactly what it does with the person's data: deactivating is not deleting. | AC-37 |
| L-13 | Signing out must void the token in every service, not just delete it from the browser. | AC-44 |
| L-14 | What is done by hand and what the system does on its own over the same resource need the same lock. | AC-46 |
| L-15 | A backup only counts once it has been shown that it can be restored. | AP-04, AC-52 |
| L-16 | The system must not decide something final on its own with incomplete data: if the operator may have forgotten to register the service, the administrator decides. | AC-53, AP-19 |

*Note.* Prepared by the authors from the register of closed risks and the actions of this document.

## 15. Glossary

**Table 12**

*Glossary*

| Term | Definition |
|---|---|
| ADR | Architecture decision record. |
| Correction | Immediate action that eliminates the symptom of a nonconformity without addressing its cause. |
| Corrective action | Action that eliminates the cause of a nonconformity that occurred, to prevent its recurrence. |
| Effectiveness | Extent to which an action achieves the planned result. |
| Improvement action | Action that increases the value or quality of the software without an existing failure. |
| Ledger | Accounting record of point movements, whose balance is that of the last movement. |
| Nonconformity | Failure to meet a requirement, a recorded decision, or what is documented. |
| PDCA | Plan, do, check, and act cycle of continual improvement. |
| Post-mortem | Blameless analysis of a serious incident, with its cause and its actions. |
| Preventive action | Action that eliminates the cause of a potential nonconformity. |
| Root cause | Fundamental cause of a problem on which action can be taken so that it does not recur. |
| Technical debt | Pending work that makes the software work, but not as it should. |

*Note.* Prepared by the authors from ISO (2015), ISO et al. (2022), and the project documentation.

## References

Congreso de la República de Colombia. (2012). *Ley Estatutaria 1581 de 2012, por la cual se dictan disposiciones generales para la protección de datos personales* [Statutory Law 1581 of 2012, which issues general provisions for the protection of personal data]. http://www.secretariasenado.gov.co/senado/basedoc/ley_1581_2012.html

International Organization for Standardization. (2015). *Quality management systems — Requirements* (ISO 9001:2015). https://www.iso.org/standard/62085.html

International Organization for Standardization, International Electrotechnical Commission, & Institute of Electrical and Electronics Engineers. (2017). *Systems and software engineering — Software life cycle processes* (ISO/IEC/IEEE 12207:2017). https://www.iso.org/standard/63712.html

International Organization for Standardization, International Electrotechnical Commission, & Institute of Electrical and Electronics Engineers. (2022). *Software engineering — Software life cycle processes — Maintenance* (ISO/IEC/IEEE 14764:2022). https://www.iso.org/standard/80710.html

Servicio Nacional de Aprendizaje. (2026). *Guía para elaborar manuales de software: Manual de usuario, manual técnico, manual de instalación y manual de administrador* [Guide for writing software manuals: User manual, technical manual, installation manual, and administrator manual] [Unpublished instructional material]. Technologist in Software Analysis and Development program.

Vehicle Washing Development Team. (2026a). *Vehicle washing management system: Project documentation* (vehicle-w-docs) [Unpublished project documentation]. GitHub. https://github.com/code-sena/vehicle-w-docs

## 16. Annexes

### Annex A. Action Record Form

**Table 13**

*Action Record Form*

| Field | Content |
|---|---|
| ID | AC-NN, ACO-NN, AP-NN, or AM-NN |
| Type | Corrective / Preventive / Improvement |
| Recording date and who detected it |  |
| Description of the nonconformity, risk, or opportunity |  |
| Initial evidence (log, screenshot, test, error code) |  |
| Severity (P0 to P3) and priority (High, Medium, Low) |  |
| Immediate correction applied (if any) |  |
| Root cause and technique used |  |
| Planned action, person responsible, and committed date |  |
| Branch, pull request, and related ADR |  |
| Closure criterion |  |
| Effectiveness verification (who, when, evidence) |  |
| Status and closure date |  |
| Lesson learned |  |

### Annex B. Root Cause Analysis Example

**Table 14**

*Five Whys of Action AC-01 (Times Shifted by Five Hours)*

| Question | Answer |
|---|---|
| Why did the customer see their booking at another time? | Because the time shown differed by five hours from the one chosen. |
| Why did it differ? | Because the time was stored converted with one time zone and read with another. |
| Why were different time zones used? | Because the JVM of the service took the time zone of the machine where it ran. |
| Why did the machine's time zone affect the data? | Because the code converted dates without an explicit time zone. |
| Why was there no explicit time zone? | Because there was no team rule for handling time. |
| **Root cause** | Absence of a time convention: "store in UTC and convert only at the edges with *BOOKING_ZONE*" was adopted, and the JVM runs in UTC. |

*Note.* Prepared by the authors from the closed risk C-001 of the project.

### Annex C. Traceability Between Actions, Risks, and Technical Debt

**Table 15**

*Traceability*

| Project risk | Technical debt | Actions |
|---|---|---|
| R-002 Partial payment-service (closed as C-005) | TD-014, TD-015, TD-016, TD-017, TD-018 | AC-04 to AC-10, AC-27 |
| R-003 Regressions without a safety net | TD-001, TD-006, TD-010, TD-027 | AC-24, AP-01, AP-07, AM-10 |
| R-004 Secret leakage | — | AP-03 |
| R-005 Lost event | TD-011 | AP-02, AC-54 |
| R-007 Known requirement gaps (closed as C-006) | TD-002, TD-003, TD-009 | AC-16, AC-17, AC-25, AC-31 |
| R-008 Data loss | — | AP-04, AC-52 |
| R-010 Documentation drift | — | AC-23, AC-34, AC-38, AP-05 |
| R-011 Public server off | — | Implementation Procedure, R-I04 |
| API abuse | TD-022 | AP-11 |
| Closed sessions that stay active | TD-024 | AC-44 |
| Booking and operator schedule | TD-025, TD-026 | AC-45, AC-46, AC-53, AP-19 |
| Availability of the public server | — | AP-16, AP-17, AP-18 |
| R-001 operations-service integration (closed as C-004) | TD-020 | AM-01 |
| Law 1581 of 2012 | — | AC-26, AC-37 |

*Note.* Prepared by the authors from the risk register and the technical backlog of the project.

### Annex D. Instructor Evaluation

The instructor evaluated the system end to end with a cut-off of October 20, 2026 (report of October 21, team 8): **85/100, grade A**. The five main flows (session, booking, payment, operator execution, and notices) were complete. The lowest dimensions were Documentation and traceability (59.0), Process and collaboration (68.4), API and contracts (76.7), and Tests (78.8); the documentation repository was not among the ones reviewed. Table 16 records the 25 findings and their status as of October 23, 2026: 5 fixed (3 of them only in *develop*), 7 partial, 12 open, and 1 that cannot be fixed.

**Table 16**

*Findings of the Instructor's Evaluation and Their Status*

| ID | Instructor's finding | Level | Status on 2026-10-23 | Evidence or action |
|---|---|---|---|---|
| H-01 | *main* does not contain the deliverable work in any of the 10 repositories. | High | Partial | *v1.0.0* with *main* equal to *develop* in 8 repositories since October 23; payment-service and the app are missing (ACO-24). |
| H-02 | No pull requests or peer review. | Medium | Partial | *main* protected (CI and review) in 8 repositories and PRs in customer, booking, and payment; payment's PR #2 has no review and *develop* is not protected (ACO-24). |
| H-03 | The web tests are templates. | High | Partial | 146 tests in 59 files, with the guard, the interceptor, and several ViewModels (*401489b*); no coverage in the CI (AM-18, ACO-26). |
| H-04 | The mobile app has no tests. | High | Partial | *jest-expo* in the CI with 13 tests (*07d2ab8*, *2416330*); sign-in, payment, and coverage are missing (AM-18, ACO-26). |
| H-05 | The permission matrix is saved but not applied. | High | Partial | The screen says it is for reference (AC-50, ADR-015), but it still saves (ACO-31). |
| H-06 | The default profile is *dev* with demo accounts whose password is published. | Medium | Fixed in *develop* | AC-58. |
| H-07 | The team guide publishes development credentials. | Medium | Fixed in *develop* | AC-58: the guide names the accounts without passwords. |
| H-08 | Development SQL Server password in the compose file and the README. | Medium | Fixed in *develop* | AC-58; the old password is still in the history (ACO-25). |
| H-09 | *google-services.json* committed with the API key. | Low | Open | ACO-25. |
| H-10 | A single database and a single administrator user for the six services. | Medium | Open | Project decision: schema per service (Software Design Documentation, Table 8); one user per service remains as an evolution (Technical Manual, 16.8). |
| H-11 | If RabbitMQ does not answer, the event is lost. | Medium | Open | Accepted risk (ADR-004); ACO-21. |
| H-12 | *booking.created* is listened to but not published. | Low | Open | Recorded in the Software Design Documentation (Table 68, finding 3). |
| H-13 | The *e2e* tests do not run in the CI. | Medium | Open | ACO-26. |
| H-14 | A *production* build of the app would point to the emulator. | Medium | Open | ACO-28. |
| H-15 | Deployment depends on turning the machine on and could not be checked online. | Medium | Open | Continuous deployment prepared and not tested (AM-17, ACO-19). |
| H-16 | The administrator's reports are calculated in the browser. | Medium | Open | Pending improvement (RF-023 partial). |
| H-17 | The gateway README contradicted the code. | Low | Fixed | Fixed on October 22; test count up to date on October 23 (*5a952ae*). |
| H-18 | The token is stored in *localStorage*. | Low | Open | Mitigated with the script content security policy (CSP) in Caddy. |
| H-19 | The web image runs nginx as *root* and without a health check. | Low | Partial | Health check since October 21; still runs as *root*. |
| H-20 | *OperationsService* concentrates 617 lines and five responsibilities. | Low | Open | Technical debt. |
| H-21 | The web commits 8.2 MB of unoptimized images. | Low | Open | Technical debt. |
| H-22 | No issues or tracking board. | Medium | Open | ACO-30. |
| H-23 | The OpenAPI contract only exists in development. | Low | Partial | OpenAPI contracts in *vehicle-w-docs* (*docs* branch); not published per service. |
| H-24 | Cancellation accepts a reason and ignores it. | Low | Fixed in *develop* | AC-68. |
| H-25 | The services start as single commits of 63 to 142 files. | Low | Cannot be fixed | It is history; since then one commit per logical change is applied. |

*Note.* Prepared by the authors from the instructor's end-to-end evaluation (cut-off of October 20, 2026) and the system review of October 23, 2026.
