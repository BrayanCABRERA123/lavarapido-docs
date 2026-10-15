# Test Documentation — Vehicle Washing Management System

## Cover Page

**Table 1**

*Document identification data*

| Field | Value |
| --- | --- |
| Project | Vehicle Washing Management System (Vehicle Washing / LavaRápido) |
| Deliverable | Test documentation (section 2.5.4) |
| Program | Software Analysis and Development Technologist (ADSO) |
| Group (ficha) | 3145556 |
| Apprentices | Brayan Estiven Patiño Cabrera, Juan Camilo Guilombo Osorio, Merari Urbano |
| Instructor | Karol Daniela Correa |
| Training center | Industria |
| Date | October 15, 2026 |

This document gathers the test plan, the inventory of automated tests in the repositories, their actual results when run on October 15, 2026, and the functional test cases, run on October 9, 2026, traced to the SRS v6 requirements (`lavarapido-docs/01-informe-especificacion-requisitos`). Its structure follows the ISO/IEC/IEEE 29119-3 standard for test documentation (International Organization for Standardization [ISO], 2021). No result in this document is assumed.

## 1. Test Plan

### 1.1 Scope

The web application, the mobile application, and the seven backend services on their `develop` branch are tested. Offensive security testing is out of scope; load is only checked through the RNF-001 response time measurement.

### 1.2 Test Types and Tools

**Table 2**

*Test types, actual tool, and where each applies*

| Type | What it verifies | Tool | Where |
| --- | --- | --- | --- |
| Domain unit tests | Rules of entities and value objects (states, validations) | JUnit 5 (`spring-boot-starter-test`); xUnit 2 | `src/test/.../domain` in Java; `tests/PaymentService.Domain.UnitTests` |
| Application unit tests | Use cases with in-memory repositories (test doubles) | JUnit 5 with fakes (`Fakes.java`, `InMemory*Repository`); xUnit with `InMemoryPorts.cs` | `application/usecase` and `PaymentService.Application.UnitTests` |
| Web integration (controller + security) | Routes, HTTP status codes, JWT, and roles with MockMvc | `spring-boot-starter-webmvc-test`, `spring-security-test` | `*ApiWebTest.java`, `ApiSecurityWebTest.java`, `AdminNotificationControllerTest.java` |
| Gateway route integration | Each public route reaches its service | Spring Boot Test | `GatewayRoutesTest.java` |
| Persistence integration | EF Core mapping against a real SQL Server | xUnit + `DatabaseFixture` | `PaymentService.Infrastructure.IntegrationTests` (requires a database) |
| Web UI unit tests | Angular components, guards, and services | Vitest 4 + jsdom (`@angular/build:unit-test`) | `Web/src/**/*.spec.ts` |
| Functional / acceptance | End-to-end flows per role against the deployed system | Manual, with Postman or Swagger UI for the API and a browser / Expo Go for the UI | Cases CP-01 to CP-33 (section 4) |
| Cross-service and RNF | Booking flow through the gateway with operator choice, automatic assignment and notices; 95th percentile response time (RNF-001); web screens at 360 px (RNF-008) | Node 22 (`node:test` and `fetch`) and Playwright Core with headless Edge | `lavarapido-infra/e2e` |

> *Note.* Tools documented in JUnit (n.d.), xUnit.net (n.d.), and Vitest (n.d.).

### 1.3 Environment

**Table 3**

*Execution environment for the tests*

| Item | Version |
| --- | --- |
| Operating system | Windows 11 Home Single Language 10.0.26300 (October 15); 10.0.26200 (October 9) |
| Node.js / npm | 24.14.0 / 11.9.0 |
| JDK | Java 25 (the projects compile for Java 21) with each service's Maven Wrapper |
| .NET SDK | 9.0.306; the project targets `net8.0` and the tests were run with `DOTNET_ROLL_FORWARD=Major` |
| Database and messaging | Not needed by the automated tests. The October 9 functional cases used SQL Server 2022, RabbitMQ 4 and Mailpit on Docker 28.4 (Docker Desktop) |
| Services | For the functional cases, the 7 services on the machine (Spring Boot JARs and `dotnet run`); email was redirected to Mailpit so no real emails were sent |

### 1.4 Criteria

- **Passed:** the actual result matches the expected one.
- **Failed:** the result differs; the error is recorded.
- **Blocked:** could not run because a dependency was missing (for example, the database).
- **Exit:** the release is accepted when the automated suites pass and the high-priority functional cases are passed.

## 2. Automated Test Inventory

The repositories have 504 test methods: 468 in the backend and 36 in the web client. The mobile app has no automated tests.

**Table 4**

*Tests per artifact (count of `@Test`/`@ParameterizedTest`, `[Fact]`/`[Theory]`/`[IntegrationFact]`, and `it()`)*

| Artifact | Files | Methods | What they cover |
| --- | --- | --- | --- |
| api-gateway | 1 | 8 | Routing of each `/api/v1/**` prefix to its service, and that `/internal/**` is not exposed by the gateway (`GatewayRoutesTest`) |
| security-service | 15 | 119 | Registration, sign-in with lockout after failed attempts, password recovery, profile and address, user administration, roles and permissions, preferences, value objects, password policy, JWT issuing and HTTP security by role (`ApiSecurityWebTest`) |
| customer-service | 6 | 50 | Customer account, license plates, vehicle CRUD, `security.user_registered` listener and web API |
| booking-service | 6 | 38 | Booking life cycle, availability, catalog, business data (`EstablishmentTest`), preferred operator in the event and web API |
| operations-service | 10 | 49 | Manual and automatic assignment, free operators, start window, execution, rating, operator metrics, team summary, operator profile, inspection report and web API |
| notification-service | 10 | 94 | Notification use cases, message factory per event, notices in the account's language, reminders, alerts for bookings without an operator, device tokens and admin controller |
| payment-service (.NET) | 9 | 110 | Payment and receipt, reused reference, history with filters, promotions, loyalty points, payment policy, command and query services, and 7 persistence tests against SQL Server |
| Web (Angular) | 35 | 36 | Creation of components, guards and services (`should create` smoke tests) |
| Mobile | 0 | 0 | No automated tests |

> *Note.* Support files (`Fakes.java`, `InMemory*.java`, `InMemoryPorts.cs`, `DatabaseFixture.cs`) are not counted as tests. The 7 payment persistence tests skip themselves when the SQL Server connection variable is not set (`DatabaseFixture.cs:20-21`).

Backend tests are domain and application tests with in-memory doubles, plus controller tests with MockMvc. Web tests only check that each component is created; they do not validate UI business rules.

## 3. Execution Results

On October 15, 2026 the eight automated suites were run: 601 tests, all passed. The 7 payment persistence tests were skipped because the test database was not set; on October 9 they had been run against an isolated database (`LavaRapidoPaymentIT`) created with the same changelogs, and they passed.

**Table 5**

*Actual results per artifact (October 15, 2026)*

| Artifact | Command | Run | Passed | Failed | Skipped | Duration |
| --- | --- | --- | --- | --- | --- | --- |
| Web (Angular) | `npx ng test --watch=false` | 36 | 36 | 0 | 0 | 23.5 s |
| api-gateway | `./mvnw test` | 34 | 34 | 0 | 0 | 10.9 s |
| security-service | `./mvnw test` | 135 | 135 | 0 | 0 | 18.0 s |
| customer-service | `./mvnw test` | 68 | 68 | 0 | 0 | 8.0 s |
| booking-service | `./mvnw test` | 38 | 38 | 0 | 0 | 8.6 s |
| operations-service | `./mvnw test` | 49 | 49 | 0 | 0 | 9.7 s |
| notification-service | `./mvnw test` | 100 | 100 | 0 | 0 | 0.5 s |
| payment-service: domain | `dotnet test PaymentService.sln` | 113 | 113 | 0 | 0 | 0.1 s |
| payment-service: application | (same command) | 28 | 28 | 0 | 0 | 0.1 s |
| payment-service: integration | (same command, without `PAYMENT_INTEGRATION_DB`) | 0 | 0 | 0 | 7 | — |
| **Total** | | **601** | **601** | **0** | **7** | |

> *Note.* Sources: Vitest output, the `target/surefire-reports/*.xml` files of each Java service and the `dotnet test` output. Maven durations add up the time of the test classes, without compilation. There are more tests run than methods in Table 4 because parameterized tests (`@ParameterizedTest`, `[Theory]`) run once per data row.

Execution notes:

- The line `ERROR ... Could not send the password recovery email: SMTP down` in the security-service log is triggered on purpose by `EmailResetCodeNotifierTest`, which simulates an SMTP outage. It is not a failure.
- Vitest prints a build warning: `src/test-providers.ts` is not included in `tsconfig`. It does not affect the results.
- The run used JDK 25 and .NET SDK 9 on projects targeting Java 21 and .NET 8; for the final delivery it should be repeated with the project's exact versions.

## 4. Functional Test Cases

The 33 cases cover the requirements that were implemented or partial in SRS v4. They were run on October 9, 2026, between 15:40 and 15:45, against the full system through the API Gateway (the same calls the web and mobile clients make), using an automated script. All 33 passed. The requirements implemented afterwards (RF-004b, RF-008, RF-010, RF-015, RF-022, RF-036, RF-037 and RF-038) are covered by automated tests (section 5), and the booking flow with operator choice and automatic assignment is also run by `lavarapido-infra/e2e/booking-flow.test.js`.

**Table 6**

*Functional test cases*

| ID | RF | Case | Precondition | Steps | Data | Expected result | Actual result | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CP-01 | RF-001 | Successful customer sign-up | Email not registered | Sign up and log in | ID, name, phone, new email, and valid password | Account created with the CLIENT role; the profile is created in customer-service | Sign-up 201; login with the CLIENT role; customer profile available (`GET /vehicles` 200) | Passed |
| CP-02 | RF-001 | Sign-up with a duplicate email | The email already exists | Sign up with the same email | Email from CP-01 | "Email already registered" message; no account is created | 409 `EMAIL_ALREADY_REGISTERED`; no account was created | Passed |
| CP-03 | RF-002 | Login by role | CLIENT, OPERATOR, and ADMIN users | Log in with each one | Valid credentials | Redirects to `/client`, `/operator`, or `/admin` by role | The three logins return a JWT with the ADMIN, OPERATOR, and CLIENT roles; the web redirects by that role (`authGuard`) | Passed |
| CP-04 | RF-002 | Wrong credentials | — | Log in with a wrong password, then with a nonexistent email | Two attempts | Same generic message in both; it does not reveal whether the email exists | Both: 401 `INVALID_CREDENTIALS` (same response) | Passed |
| CP-05 | RF-003 | Recover password | Registered user; Mailpit running | Request a code, read it in Mailpit, verify it, and set a new password | 6-digit code | Password changed; login with the new one works | 6-digit code received in Mailpit; verify 204, reset 204; login with the new password succeeds | Passed |
| CP-06 | RF-003 | Code locked after attempts | Code requested | Enter 5 wrong codes, then the right one | 5 invalid codes | The right code is no longer accepted | 5 attempts: 400; then the right code: 400 `INVALID_RESET_CODE` | Passed |
| CP-07 | RF-004 | Password change with a wrong current password | Logged in | Change the password with the wrong current one | Wrong current password | "Incorrect current password" error; nothing changes | 400 `INCORRECT_CURRENT_PASSWORD`; login with the current password still works | Passed |
| CP-08 | RF-005 | Create a booking | Customer with an SUV | Choose vehicle, Basic service, a free date and time | SUV, Basic | Booking created; price COP 23,000 (seed price of Basic for SUV) | Booking 201 RES-060003 for 10/10/2026 08:00, status CONFIRMED; total COP 23,000 | Passed |
| CP-09 | RF-006 | Time slot taken | Active bays of a slot booked | Book the same slot until it is full | Several customer vehicles | The booking is not saved; up to five alternative times on the same day are offered | Slot 08:30 full (BAY-02 and BAY-03 plus an earlier booking); the next one: 409 `SLOT_UNAVAILABLE` with alternatives 09:00, 09:30, 10:00, 10:30, and 11:00 | Passed |
| CP-10 | RF-007 | Cancel a booking before it starts | Booking CONFIRMED | Cancel with a reason | Reason `CUSTOMER_REQUEST` | Booking is CANCELLED with the reason stored | 200: status CANCELLED, reason `CUSTOMER_REQUEST` | Passed |
| CP-11 | RF-007 | Change a booking in progress | Booking IN_PROGRESS | Try to cancel | — | Action blocked with a message | Booking IN_PROGRESS; cancel: 409 `BOOKING_NOT_CHANGEABLE` | Passed |
| CP-12 | RF-009 | Assign an unavailable operator | Operator with an absence at the booking time | Check candidates and try to assign them; then assign an available one | Absent operator | The operator is not allowed; available operators are listed first | Available listed first; the absent one shows reason `OPERATOR_ABSENT`; assigning them: 409 `OPERATOR_ABSENT`; assigning the available one: 200 | Passed |
| CP-13 | RF-011 | Operator sees their services | Booking assigned to the operator | Check assigned services | — | List with customer and vehicle data | RES-060003 shows vehicle Mazda CX-5, plate FPW-653, and service Basic | Passed |
| CP-14 | RF-012b | Start and finish a service | Assigned service PENDING, 15 min before its time | Another operator tries to start; the assigned one starts and finishes | — | States IN_PROGRESS and COMPLETED; the other operator gets an error | Other operator: 404 `BOOKING_NOT_FOUND`; start 200 (IN_PROGRESS), finish 200 (COMPLETED); booking COMPLETED | Passed |
| CP-15 | RF-012 | Rate a service once | Booking COMPLETED | Rate 5 stars; try to rate again | 5, comment | First rating saved; the second is rejected | First: 201 (5); second: 409 `ALREADY_RATED` | Passed |
| CP-16 | RF-013 | Payment methods | Payment accounts configured | Check methods (admin) and accounts (customer) | — | Cash, Nequi, Daviplata, and bank transfer; cash shows no QR | The admin sees the 4 methods; the API gives the customer only the active digital accounts with QR, and the UI always adds cash without QR (`payment.ts:44-57`) | Passed |
| CP-17 | RF-013b | Upload a receipt | Booking awaiting payment | Pay with Nequi attaching image, amount, and reference | PNG < 10 MB | Payment created in review with its receipt | 201: status IN_REVIEW, amount COP 24,000, reference REF-428646 | Passed |
| CP-18 | RF-014 | Approve and reject payments | Payments in review | Approve one and reject another with a reason | Rejection reason | States APPROVED and REJECTED; the customer gets a notification | Approve 200 (APPROVED); reject 200 (REJECTED); the customer received `PAYMENT_CONFIRMED` and `PAYMENT_REJECTED` | Passed |
| CP-19 | RF-016 | Duplicate reference | Approved payment with reference R1 | Upload another receipt with R1 on another booking | Reference R1 | Receipt rejected | 409 `TRANSACTION_REFERENCE_REUSED` | Passed |
| CP-20 | RF-018 | Booking notification | `MESSAGING_ENABLED=true` | Confirm a booking; open notifications; mark as read | — | The notification arrives; the unread counter goes down | 9 notifications (`USER_WELCOME`, `BOOKING_CONFIRMED`, `BOOKING_CANCELLED`, `OPERATOR_ASSIGNED`); unread 9 → 8 | Passed |
| CP-21 | RF-020 | Language saved on the account | Logged in | Switch to English; start a new session | `en` | The UI opens in English | Preference saved (200); the new session returns `language=en` and the web opened in English (test screenshot) | Passed |
| CP-22 | RF-021 | Schedule exception | — | Create a "closed" exception and check availability that day | 10/20/2026 | No times available that day | Exception 201; availability: `open=false`, no free times | Passed |
| CP-23 | RF-024 | Create and deactivate a promotion | Admin session | Create a 10% promotion and deactivate it | 10% discount | Promotion visible, then inactive | Created 201; deactivated 200; status in the list: `paused` | Passed |
| CP-24 | RF-026 | Earn points | Service with 10 points configured | Approve the booking payment; check the balance | — | The balance grows by the service points | Balance 0 → 10 on payment approval | Passed |
| CP-25 | RF-027 | Deactivate one's own account | Customer session | Deactivate the account with the current password and try to log in | Current password | The session is revoked and login is rejected | Deactivation 204; new login: 403 `ACCOUNT_DISABLED` | Passed |
| CP-26 | RF-028 | Create an operator and restrict by role | Admin and customer sessions | Admin creates an operator; the customer calls `GET /admin/users` | Operator data | OPERATOR account created; the customer gets 403 | Operator created 201; the customer gets 403 | Passed |
| CP-27 | RF-029 | Edit the permission matrix | Admin session | Remove `EDIT_DATA` from OPERATOR; try to create a role | Permission `EDIT_DATA` | The matrix is saved; roles cannot be created | Matrix saved (200); create role: 405. The matrix was restored afterward | Passed |
| CP-28 | RF-030 | Register a vehicle with a duplicate plate | Customer with a registered vehicle | Register another vehicle with the same plate | Plate FPW653 | Registration is rejected | First registration 201; second: 409 `PLATE_ALREADY_REGISTERED` | Passed |
| CP-29 | RF-031 | Price change without affecting bookings | Confirmed booking with Basic | Admin raises the Basic/SUV price; check the existing booking and create a new one | COP 23,000 → 24,000 | The existing one keeps its price; the new one uses the new price | Earlier booking: COP 23,000; new booking: COP 24,000. The price was restored afterward | Passed |
| CP-30 | RF-032 | Bay under maintenance | BAY-04 under maintenance (seed) | Fill a slot and check which bays were used | — | The bay under maintenance is not used for new bookings | BAY-04 was not used; the slot was full with only the active bays | Passed |
| CP-31 | RF-033 | Disallowed status transition | Booking CANCELLED | Admin tries to change it to CONFIRMED | — | Rejected | 409 `INVALID_STATUS_TRANSITION` | Passed |
| CP-32 | RF-034 | Deactivated payment account | Active Daviplata account | Admin deactivates it; the customer checks accounts | — | The account is no longer shown to the customer | Visible when created; once deactivated (200) it no longer appears to the customer | Passed |
| CP-33 | RF-035 | Refund an approved payment | Payment APPROVED | Admin refunds | — | Status REFUNDED; `payment.refunded` is published and the customer is notified | Refund 204; payment REFUNDED; `PAYMENT_REFUNDED` notification received; points reversed (10 → 0) | Passed |

> *Note.* Prices and codes in the test data come from the seed changelogs (`103-seed-catalog.sql`, `104-seed-booking-catalogs.sql`). Cases CP-25 to CP-33 cover requirements RF-027 to RF-035, new in SRS v4. New test accounts were used, because the demo account `operador@gmail.com` is deactivated in the local database. Afterward, the Basic price, the permission matrix, the promotion, and the schedule exception were restored. Evidence: execution log with the HTTP status and error code of each step.

## 5. Traceability Matrix

Of the 41 requirements in SRS v6, 30 have a functional case and 39 a related automated test; RF-032 and RF-034 only have a functional case.

**Table 7**

*RF → status → endpoint / screen → test case*

| RF | Status (SRS v6) | Endpoint (prefix `/api/v1`) | Web screen | Functional case | Related automated test |
| --- | --- | --- | --- | --- | --- |
| RF-001 | Implemented | `POST /auth/register` | `/auth/register` | CP-01, CP-02 | `AccountRegistrationServiceTest`, `UserRegisteredListenerTest` |
| RF-002 | Implemented | `POST /auth/login` | `/auth` | CP-03, CP-04 | `AuthenticationServiceTest`, `JwtTokenIssuerTest`, `ApiSecurityWebTest` |
| RF-003 | Implemented | `POST /auth/password/forgot`, `/verify`, `/reset` | `/auth/forgot-password` | CP-05, CP-06 | `PasswordRecoveryServiceTest`, `PasswordResetTokenTest` |
| RF-004 | Implemented | `PUT /users/me/password` | `/client/profile` | CP-07 | `UserProfileAndAdministrationTest`, `PasswordPolicyTest` |
| RF-004b | Implemented | `POST /auth/login` (423 `ACCOUNT_LOCKED`) | `/auth` | — | `AuthenticationServiceTest` (lockout and window), `PasswordRecoveryServiceTest` (a reset lifts it), `ApiSecurityWebTest` (423) |
| RF-027 | Implemented | `GET/PATCH /users/me`, `GET/PUT /users/me/address`, `PUT /users/me/email`, `POST /auth/logout`, `POST /users/me/deactivate` | `/client/profile` | CP-25 | `UserProfileAndAdministrationTest`, `PersonAddressServiceTest`, `AuthenticationServiceTest` |
| RF-028 | Implemented | `GET/POST /admin/users`, `PATCH /admin/users/{id}/status` | `/admin/management`, `/admin/operators` | CP-26 | `UserProfileAndAdministrationTest`, `ApiSecurityWebTest` |
| RF-029 | Implemented | `GET /admin/roles-permissions`, `PUT /admin/roles-permissions/{role}` | `/admin/management` | CP-27 | `RolePermissionAdministrationServiceTest` |
| RF-030 | Implemented | `/vehicles`, `GET /vehicle-types`, `GET /admin/vehicles` | `/client/vehicles` | CP-28 | `CustomerVehicleServiceTest`, `LicensePlateTest`, `CustomerApiWebTest` |
| RF-031 | Implemented | `GET /catalog/services`, `/admin/catalog/services` | `/admin/management` | CP-29 | `CatalogServiceTest` |
| RF-021 | Implemented | `PUT /admin/schedule/business-hours`, `POST /admin/schedule/exceptions` | `/admin/schedule` | CP-22 | `AvailabilityPolicyTest` |
| RF-032 | Implemented | `/admin/bays` | `/admin/schedule` | CP-30 | — |
| RF-037 | Implemented | `GET/PUT /admin/establishment`, `GET /establishment` | `/admin/settings` | — | `EstablishmentTest`, `BookingApiWebTest` |
| RF-005 | Implemented | `POST /bookings`, `GET /catalog/services` | `/client/reserve` | CP-08 | `BookingServiceTest`, `BookingTest` |
| RF-006 | Implemented | `GET /bookings/availability` | `/client/reserve` | CP-09 | `AvailabilityPolicyTest` |
| RF-007 | Implemented | `PUT /bookings/{id}`, `POST /bookings/{id}/cancel` | `/client/history` | CP-10, CP-11 | `BookingTest`, `BookingApiWebTest` |
| RF-033 | Implemented | `GET /admin/bookings`, `PATCH /admin/bookings/{id}/status` | `/admin/reservations` | CP-31 | `BookingTest`, `BookingServiceTest` |
| RF-008 | Implemented | `booking.confirmed` event, `GET /internal/v1/bookings` | `/admin/reservations` | — | `AutoAssignmentPolicyTest`, `OperationsServiceTest` (automatic assignment, deactivated account), `booking-flow.test.js` |
| RF-009 | Implemented | `GET /admin/assignments/{id}/candidates`, `PUT /admin/assignments/{id}` | `/admin/reservations` | CP-12 | `AssignmentPolicyTest`, `OperationsServiceTest` |
| RF-010 | Implemented | `GET /operators/available`, `POST /bookings` (`preferredOperatorId`) | `/client/reserve` | — | `OperationsServiceTest` (free operators), `OperationsApiWebTest`, `booking-flow.test.js` |
| RF-011 | Implemented | `GET /operator/services` | `/operator/assigned-services` | CP-13 | `OperationsServiceTest` |
| RF-012b | Implemented | `POST /operator/services/{id}/start`, `/finish` | `/operator/assigned-services` | CP-14 | `StartPolicyTest`, `ServiceExecutionTest` |
| RF-012 | Implemented | `POST /ratings/{bookingId}` | `/client/history` | CP-15 | `ServiceExecutionTest` |
| RF-022 | Implemented | `PUT /admin/operators/{id}/availability`, `/absences`, `GET /admin/operators/summary` | `/admin/operators/:id` | — | `AssignmentPolicyTest`, `TeamSummaryCalculatorTest` |
| RF-036 | Implemented | `/admin/inspections/{bookingId}/**`, `GET /public/inspections/{token}` | `/admin/reservations/:id/inspection`, `/report/:token` | — | `InspectionReportTest`, `OperationsApiWebTest` |
| RF-038 | Implemented | `GET /admin/operators/profiles`, `PUT /admin/operators/{id}/profile` | `/admin/operators/:id` | — | `OperatorProfileServiceTest` |
| RF-034 | Implemented | `/admin/payment-accounts`, `GET /payment-accounts` | `/admin/settings` | CP-32 | — |
| RF-013 | Implemented | `GET /payment-accounts` | `/client/payment` | CP-16 | `PaymentQueryServiceTests` |
| RF-013b | Implemented | `POST /payments` | `/client/payment` | CP-17 | `PaymentTests`, `PaymentCommandServiceTests` |
| RF-014 | Implemented | `POST /admin/payments/{id}/approve`, `/reject` | `/admin/payments` | CP-18 | `PaymentTests`, `PaymentCommandServiceTests` |
| RF-015 | Implemented | `GET /payments/me?from=&to=&service=` | `/client/history` | — | `PaymentQueryServiceTests` (order and filters) |
| RF-016 | Implemented | `POST /payments` | `/client/payment` | CP-19 | `PaymentPolicyTests`, `PaymentCommandServiceTests` (reused reference) |
| RF-035 | Implemented | `POST /admin/payments/{id}/refund` | `/admin/payments` | CP-33 | `PaymentTests`, `PaymentCommandServiceTests` |
| RF-017 | Implemented | `GET /admin/bookings/day-summary`, `GET /operators/my-bookings` and dashboard stores | `/client`, `/operator`, `/admin` | — | `BookingServiceTest` (day summary), web smoke tests (`dashboard.spec.ts`) |
| RF-018 | Implemented | `/notifications/*` + RabbitMQ events | `/*/notifications` | CP-20 | `NotificationUseCasesTest`, `NotificationFactoryTest`, `BookingReminderServiceTest`, `LocalizedNotificationsTest`, `UnassignedBookingAlertTest`, `StaffNotificationsTest` |
| RF-019 | Implemented | `PUT /users/me/preferences` | `/*/configuration` | Covered by CP-21 | `UserPreferenceServiceTest` |
| RF-020 | Implemented | `PUT /users/me/preferences` | `/*/configuration` | CP-21 | `UserPreferenceServiceTest`, `UserPreferenceTest` |
| RF-023 | Partial | `GET /admin/operators/{id}/metrics`, `GET /admin/operators/summary`, payment and booking stores | `/admin/reports`, `/admin/operators/:id` | — | `OperatorMetricsCalculatorTest`, `TeamSummaryCalculatorTest` |
| RF-024 | Implemented | `/admin/promotions` | `/admin/management` | CP-23 | `PromotionTests` |
| RF-025 | Implemented | `POST /loyalty/redeem` | `/client/payment` | — | `CustomerPromotionServiceTests` |
| RF-026 | Implemented | `GET /loyalty/balance` | `/client` | CP-24 | `LoyaltyTransactionTests` |

> *Note.* The automated test column points to the file whose name and methods match the requirement; code coverage was not measured. `booking-flow.test.js` is in `lavarapido-infra/e2e` and needs the system running.

## 6. Findings and Open Items

**Table 8**

*Testing gaps found*

| # | Gap | Recommendation |
| --- | --- | --- |
| 1 | The mobile app has no automated tests | Add Jest with `jest-expo`, at least for validators (`shared/validators`) and services (`core/services`) |
| 2 | The 36 web tests only check that the component is created | Test real rules: `authGuard` by role, `authInterceptor` on 401, booking form |
| 3 | The 7 payment persistence tests need a migrated database and skip without it | Document in the README how to create the test database and set `PAYMENT_INTEGRATION_DB` |
| 4 | For RF-023 (reports) only the operator metrics and the team summary are tested; the PDF/Excel export has no test | Add a functional case for reports and the PDF/Excel export |
| 5 | RF-032 (bays) and RF-034 (payment accounts) have no dedicated automated tests: `ScheduleService` and `PaymentAccountService` have no test class | Add unit tests for those two services |
| 6 | The requirements implemented after October 9 (RF-004b, RF-008, RF-010, RF-015, RF-022, RF-036, RF-037 and RF-038) have automated tests but no functional case of their own | Add their CP cases and run them against the full system |

**Table 9**

*Defects found while running the system*

| # | Defect | Evidence | Severity |
| --- | --- | --- | --- |
| 1 | The administrator dashboard always says "¡Hola, Laura!" regardless of who logs in | `Web/src/app/features/admin/pages/dashboard/dashboard.ts:73` (`adminName = 'Laura'`); "Laura Méndez" is also hard-coded in `payment-review-modal.html:167` | Low |
| 2 | In the operator's "Assigned services" (web), the Customer column shows the license plate | `Web/src/app/features/operator/pages/assigned-services/assigned-services.ts:141` | Medium |
| 3 | On the customer home (mobile), "Assigned operator" is empty even though the booking has an operator | Booking RES-060003, assigned in CP-12; mobile screenshot | Medium |
| 4 | The brand name is inconsistent: "AquaWash" (mobile), "Car Wash" and "Lavado Vehicular" (web), "Express Car Wash" (establishment) | Web and mobile screenshots | Low |
| 5 | The landing page advertises a "mobile wash service" and "wherever you are", but SRS v4 defines a single-location car wash | Landing screenshot; SRS v4, section 1 | Low |
| 6 | If there are two accounts of the same method (two Nequi), the payment screen shows both selected at once | Customer Payments screenshot | Low |

> *Note.* Code review of October 15, 2026: defect 3 is fixed (the customer home shows the name of the assigned operator, on the web and on mobile). Defects 1, 2, 4 and 5 are still in the code; defect 6 was not checked again.

## References

International Organization for Standardization. (2021). *Software and systems engineering — Software testing — Part 3: Test documentation* (ISO/IEC/IEEE 29119-3:2021). https://www.iso.org/standard/79429.html

JUnit. (n.d.). *JUnit 5 user guide*. Retrieved October 9, 2026, from https://junit.org/junit5/docs/current/user-guide/

Vitest. (n.d.). *Vitest documentation*. Retrieved October 9, 2026, from https://vitest.dev/

xUnit.net. (n.d.). *xUnit.net documentation*. Retrieved October 9, 2026, from https://xunit.net/
