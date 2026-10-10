# Software Analysis: Dynamic Views of the LavaRápido System

Juan Camilo Guilombo Osorio, Brayan Estiven Patiño Cabrera and Merari Urbano Quintero

Centro de la Industria, la Empresa y los Servicios, Servicio Nacional de Aprendizaje (SENA), Huila Regional

Software Analysis and Development Technologist program (ADSO), group (ficha) 3145556

Instructor: Karol Daniela Correa

Version 1.0, October 9, 2026

---

## Introduction

This document shows how LavaRápido behaves when someone uses it: what happens, in which order, and between which screens and services. It is organized in four parts:

1. **Use cases by actor**, with their `«include»`/`«extend»` relationships.
2. **Sequence diagrams** of the main flows: from the screen to the gateway, from the gateway to the service, and from the service to the database or to another service.
3. **Activity diagrams** of the business processes.
4. **State diagrams** of the entities that change status (booking, payment, service execution).

The diagrams are written in Mermaid and were checked against the code and the running system on October 9, 2026. The screen inventory, with screenshots by role, is at the end.

The full specification of each requirement and use case (actors, precondition, main flow, alternative flows and postcondition) is in the *Software Requirements Specification*, sections 5 and 7.3; here they are cited by their identifier (RF-XXX, CUXX).

---

## 1. Use Cases by Actor

### 1.1 Use Case Diagram

The 29 use cases are presented in four diagrams, one per actor, grouped by module.

**Use cases common to the three roles**

```mermaid
flowchart LR
    Usuario(["Any user"])
    CU01(["CU01 Sign in"])
    CU03(["CU03 Recover password"])
    CU04(["CU04 Change password"])
    CU16(["CU16 View dashboard"])
    CU17(["CU17 Manage notifications"])
    CU18(["CU18 Customize visual theme"])
    CU19(["CU19 Select language"])

    Usuario --- CU01
    Usuario --- CU03
    Usuario --- CU04
    Usuario --- CU16
    Usuario --- CU17
    Usuario --- CU18
    Usuario --- CU19

    classDef actor fill:#08427b,color:#fff,stroke:#052e56
    class Usuario actor
```

**Customer use cases**

```mermaid
flowchart LR
    Cliente(["Customer"])
    Sistema(["System"])

    subgraph CTA["Account and vehicles"]
        CU02(["CU02 Create account"])
        CU26(["CU26 Manage vehicles"])
    end

    subgraph RES["Bookings"]
        CU05(["CU05 Request booking"])
        CU06(["CU06 Confirm booking based on availability"])
        CU07(["CU07 Reschedule or cancel booking"])
    end

    subgraph PAG["Payments and loyalty"]
        CU12(["CU12 Pay for a booking"])
        CU14(["CU14 View payment history"])
        CU25(["CU25 Apply promotion at payment"])
        CU15(["CU15 Rate service"])
    end

    Cliente --- CU02
    Cliente --- CU26
    Cliente --- CU05
    Cliente --- CU07
    Cliente --- CU12
    Cliente --- CU14
    Cliente --- CU15
    Cliente --- CU25
    Sistema --- CU06

    CU05 -. "«include»" .-> CU06
    CU25 -. "«extend»" .-> CU12

    classDef actor fill:#08427b,color:#fff,stroke:#052e56
    class Cliente,Sistema actor
```

**Operator use cases**

```mermaid
flowchart LR
    Operario(["Operator"])
    CU10(["CU10 View assigned services"])
    CU11(["CU11 Start and finish service"])
    CU22(["CU22 Manage operator availability"])

    Operario --- CU10
    Operario --- CU11
    Operario -. "views" .- CU22

    classDef actor fill:#08427b,color:#fff,stroke:#052e56
    class Operario actor
```

**Administrator and System use cases**

```mermaid
flowchart LR
    Administrador(["Administrator"])
    Sistema(["System"])

    subgraph AUTH["Users"]
        CU27(["CU27 Administer users and permissions"])
    end
    subgraph CAT["Catalog, opening hours and bays"]
        CU20(["CU20 Configure opening hours and bays"])
        CU21(["CU21 Manage catalog and prices"])
    end
    subgraph RES["Bookings and operations"]
        CU08(["CU08 Assign operator automatically"])
        CU09(["CU09 Assign or reassign operator"])
        CU22b(["CU22 Manage operator availability"])
        CU29(["CU29 Manage bookings"])
    end
    subgraph PAG["Payments and promotions"]
        CU13(["CU13 Review payment"])
        CU28(["CU28 Manage payment accounts"])
        CU24(["CU24 Manage promotions"])
    end
    subgraph REP["Reports"]
        CU23(["CU23 View reports"])
    end

    Administrador --- CU27
    Administrador --- CU20
    Administrador --- CU21
    Administrador --- CU09
    Administrador --- CU22b
    Administrador --- CU29
    Administrador --- CU13
    Administrador --- CU28
    Administrador --- CU24
    Administrador --- CU23
    Sistema --- CU08

    classDef actor fill:#08427b,color:#fff,stroke:#052e56
    class Administrador,Sistema actor
```

*Note.* `«include»` means that CU05 always runs CU06; `«extend»` means that CU25 optionally extends CU12. CU22 appears as view-only for the operator and as management for the administrator, who is the one recording shifts and absences (RF-022).

### 1.2 Actor and Use Case Matrix

| Actor | Use cases |
|---|---|
| All roles | CU01, CU03, CU04, CU16, CU17, CU18, CU19 |
| Customer | CU02, CU05, CU06, CU07, CU12, CU14, CU15, CU25, CU26 |
| Operator | CU10, CU11, CU22 (view only) |
| Administrator | CU09, CU13, CU20, CU21, CU22, CU23, CU24, CU27, CU28, CU29 |
| System | CU06 (included in CU05), CU08 |

The specification of each of the 29 use cases (precondition, main flow, alternative flows, postcondition, status) is in the *Software Requirements Specification*, Tables 23 to 51.

---

## 2. Sequence Diagrams

Each diagram follows the path of the request (screen, gateway, services, database and RabbitMQ) with the class and endpoint names from the code. The first five are based on the diagrams in `vehicle-w-docs/08-uml/diagrams/source/`; the last two cover loyalty and roles and permissions.

### 2.1 Registration and welcome (RF-001, RF-018)

```mermaid
sequenceDiagram
    autonumber
    actor C as Customer
    participant W as Web
    participant GW as API Gateway
    participant S as security-service
    participant MQ as RabbitMQ
    participant CU as customer-service
    participant N as notification-service
    participant M as SMTP

    C->>W: Fills in the registration form
    W->>GW: POST /api/v1/auth/register
    GW->>S: routes
    S->>S: Validates (password policy, unique email and ID number), saves person + account (CLIENT)
    S-->>W: 201 Created
    S-)MQ: UserRegistered (security.user_registered), after commit
    par customer profile
        MQ-)CU: UserRegistered
        CU->>CU: Creates the customer profile (idempotent)
    and welcome
        MQ-)N: UserRegistered
        N->>N: Creates WELCOME notification (idempotent: processed_event)
        N->>M: Welcome email (the address comes in the event)
    end
    C->>W: Signs in
    W->>GW: POST /api/v1/auth/login
    GW->>S: routes
    S-->>W: 200 JWT (HS256, 1 h, roles claim)
```

*Source:* `security-service` (`AccountRegistrationService`, `AuthenticationService`), event `security.user_registered`.

### 2.2 Booking a wash (RF-005, RF-006)

```mermaid
sequenceDiagram
    autonumber
    actor C as Customer
    participant W as Web (via gateway)
    participant B as booking-service
    participant CU as customer-service
    participant DB as SQL Server
    participant MQ as RabbitMQ
    participant N as notification-service
    participant S as security-service

    C->>W: Chooses vehicle, service and date
    W->>B: GET /api/v1/bookings/availability?date=…&vehicleTypeId=…&serviceIds=…
    B->>DB: opening hours, exceptions, bays, bookings of the day
    B-->>W: free times
    C->>W: Confirms a time
    W->>B: POST /api/v1/bookings
    B->>CU: GET /api/v1/vehicles/{id} (customer JWT)
    CU-->>B: vehicle + type (ownership is validated, INV-BOOK-002)
    B->>DB: sp_getapplock (schedule lock)
    alt free bay and the vehicle has no other booking at that time
        B->>DB: INSERT CONFIRMED booking + bay + lines with frozen prices
        B-->>W: 201 booking (code RES-000042)
        B-)MQ: BookingConfirmed (booking.confirmed), after commit
        MQ-)N: BookingConfirmed
        N->>S: GET /internal/v1/users/{id}/contact (X-Internal-Key)
        N->>N: BOOKING_CONFIRMED notification + reminders (24 h, 1 h)
        N-->>C: inbox + push + email
    else slot taken
        B-->>W: 409 SLOT_UNAVAILABLE + up to 5 alternative times
    end
```

*Source:* `booking-service` (`BookingService.confirmNew`), contract in `07-api/contracts/openapi/booking-service.yaml`.

### 2.3 Booking reminder (ADR-011 §7)

```mermaid
sequenceDiagram
    autonumber
    participant MQ as RabbitMQ
    participant N as notification-service
    participant DB as notification.booking_reminder
    participant J as ReminderScheduler
    participant S as security-service
    actor C as Customer

    MQ-)N: BookingConfirmed (new or rescheduled)
    N->>DB: Replaces pending reminders: one per lead time (24 h, 1 h) that is still in the future
    MQ-)N: BookingCancelled
    N->>DB: Cancels the pending reminders of that booking (soft delete)
    loop every 5 minutes (REMINDER_CHECK_INTERVAL)
        J->>DB: Due reminders (remind_at <= now, not sent)
        J->>S: GET /internal/v1/users/{id}/contact (X-Internal-Key)
        J->>N: BOOKING_REMINDER notification
        N-->>C: inbox + push + email
        J->>DB: sets sent_at (never sent twice)
    end
```

*Source:* `notification-service` (`BookingReminderService`, `ReminderScheduler`).

### 2.4 Operator assignment, execution and rating (RF-009, RF-011, RF-012, RF-012b)

```mermaid
sequenceDiagram
    autonumber
    actor A as Administrator
    actor O as Operator
    actor C as Customer
    participant W as Web (via gateway)
    participant OP as operations-service
    participant B as booking-service
    participant S as security-service
    participant DB as SQL Server (execution)
    participant MQ as RabbitMQ
    participant N as notification-service

    A->>W: Opens a booking → Operator assignment
    W->>OP: GET /api/v1/admin/assignments/{bookingId}/candidates
    OP->>B: GET /admin/bookings/{id} and /admin/bookings?from=&to= (admin JWT)
    OP->>S: GET /admin/users?role=OPERATOR (admin JWT)
    OP->>DB: shifts, absences, executions of the day
    OP-->>W: each operator + blocking reason (available ones first)
    A->>W: Picks an operator
    W->>OP: PUT /api/v1/admin/assignments/{bookingId}
    alt booking SCHEDULED/CONFIRMED and AssignmentPolicy finds no blocking reason
        OP->>DB: one PENDING service_execution per booking line
        OP-->>W: 200 assignment
        OP-)MQ: OperatorAssigned (execution.operator_assigned), after commit
        MQ-)N: notifies the operator and the customer
    else inactive / off shift / absent / busy
        OP-->>W: 409 OPERATOR_INACTIVE | OPERATOR_NOT_ON_SHIFT | OPERATOR_ABSENT | OPERATOR_BUSY
    end

    O->>W: Assigned services → Start service (only on the booking day)
    W->>OP: POST /api/v1/operator/services/{bookingId}/start
    OP->>B: PATCH /operator/bookings/{id}/status IN_PROGRESS (operator JWT)
    OP->>DB: lines → IN_PROGRESS, started_at
    OP-)MQ: ServiceStarted (execution.service_started)
    O->>W: Finish service
    W->>OP: POST /api/v1/operator/services/{bookingId}/finish
    OP->>B: PATCH /operator/bookings/{id}/status COMPLETED
    OP->>DB: lines → COMPLETED, finished_at
    OP-)MQ: ServiceCompleted (execution.service_completed)
    MQ-)N: tells the customer the wash is done

    C->>W: History → rates the completed booking
    W->>OP: POST /api/v1/ratings/{bookingId} {score 1–5, comment}
    OP->>B: GET /bookings/{id} (customer JWT: only their own bookings)
    OP->>DB: rating on each line (only once)
    OP-->>W: 201 rating
```

*Source:* `operations-service` (`OperationsService.candidates / assign / start / finish / rate`, `AssignmentPolicy`, ADR-014).

### 2.5 Payment by receipt and review (RF-013, RF-013b, RF-014)

```mermaid
sequenceDiagram
    autonumber
    actor C as Customer
    actor A as Administrator
    participant W as Web (via gateway)
    participant P as payment-service (.NET)
    participant B as booking-service
    participant DB as SQL Server (payment)

    C->>W: Pays for the service
    W->>P: GET /api/v1/payment-accounts
    P-->>W: active accounts that require a receipt (QR, instructions)
    C->>C: Pays from the bank app (outside the platform)
    C->>W: Account, reference code, receipt image
    W->>P: POST /api/v1/payments
    P->>B: GET /bookings/{id} (customer JWT)
    B-->>P: status, total, owner
    alt booking can be paid and has no open or approved payment
        P->>DB: PENDING payment (amount = booking total) + receipt → IN_REVIEW
        P-->>W: 201 payment IN_REVIEW
    else not payable / already reported / already approved
        P-->>W: 400 BOOKING_NOT_PAYABLE | 409 PAYMENT_ALREADY_REPORTED | 409 PAYMENT_ALREADY_APPROVED
    end

    A->>W: Payments → Verify
    W->>P: GET /api/v1/admin/payments?status=IN_REVIEW
    P->>B: GET /admin/bookings/{id} (admin JWT) for each payment
    P-->>W: payments with their booking data
    alt approve
        W->>P: POST /api/v1/admin/payments/{id}/approve
        P->>DB: APPROVED, approved_by, processed_at (unique index: one per booking)
    else reject
        W->>P: POST /api/v1/admin/payments/{id}/reject {reason}
        P->>DB: REJECTED + reason (the customer can report again)
    end

    A->>W: Payments → Manual record (cash at the site)
    W->>P: POST /api/v1/admin/payments {bookingId, paymentAccountId}
    P->>B: GET /admin/bookings/{id}
    P->>DB: APPROVED payment directly (amount = booking total)
```

*Source:* `payment-service` (`PaymentApplicationService.ReportPaymentAsync / ApproveAsync / RejectAsync / RegisterManualAsync`, `Payment` aggregate, ADR-008, ADR-013).

### 2.6 Coupon redemption and loyalty points (RF-024, RF-025, RF-026)

```mermaid
sequenceDiagram
    autonumber
    actor C as Customer
    actor A as Administrator
    participant W as Web (via gateway)
    participant P as payment-service (.NET)
    participant B as booking-service
    participant DB as SQL Server (promotion / payment)
    participant MQ as RabbitMQ
    participant N as notification-service

    A->>W: Management → Promotions → Create
    W->>P: POST /api/v1/admin/promotions {code, validity, % discount 1-100, required points}
    P->>DB: INSERT promotion
    P-->>W: 201 promotion

    Note over C,P: --- Points credit (when a payment is approved, flow 2.5) ---
    P->>DB: INSERT loyalty_transaction (+points of the paid service, unique sequence_no per customer)
    Note over P: The balance is never stored separately: it is always calculated<br/>from the last row of the ledger of movements (INV-LOY-001)

    C->>W: Dashboard → sees their points and unlocked promotions
    W->>P: GET /api/v1/loyalty/balance
    P->>DB: SELECT the customer's last movement (current balance)
    P-->>W: current points
    W->>P: GET /api/v1/loyalty/promotions
    P->>DB: active promotions
    P-->>W: each promotion + whether it is already unlocked (points >= required)

    C->>W: Payment of a booking → enters the coupon code
    W->>P: POST /api/v1/loyalty/redeem {bookingId, code}
    P->>B: checks that the booking belongs to the customer and has no reported payment
    P->>DB: looks up the promotion by code
    alt valid, unlocked, not redeemed before for this booking and within the usage limits
        P->>P: Promotion.Redeem(...) calculates the discount on the subtotal (never exceeds it)
        P->>DB: INSERT promotion_redemption (uses up one redemption, so two simultaneous redemptions collide)
        P-)MQ: PromotionRedeemed (payment.promotion_redeemed)
        MQ-)N: notifies the redemption in the inbox and by email
        P-->>W: 200 {discount applied, new total to pay}
    else expired / not unlocked / already redeemed / no redemptions left
        P-->>W: 409 PromotionNotRedeemable | PromotionAlreadyRedeemed | PromotionExhausted | PromotionCustomerLimitReached
    end
```

*Source:* `payment-service` (`LoyaltyController`, `CustomerPromotionService.RedeemAsync`, `Promotion.Redeem` aggregate, `LoyaltyLedgerRepository`), ADR-015.

### 2.7 Roles and permissions management (RF-029)

```mermaid
sequenceDiagram
    autonumber
    actor A as Administrator
    participant W as Web (via gateway)
    participant S as security-service
    participant DB as SQL Server (security)

    A->>W: Management → Roles
    W->>S: GET /api/v1/admin/roles-permissions
    S->>DB: SELECT permission catalog + permissions of each role
    S-->>W: 200 {permissions[], roles: [{role, permissions[]}]}, 3 fixed roles: ADMIN, OPERATOR, CLIENT
    A->>W: Checks or unchecks permissions of a role and saves
    W->>S: PUT /api/v1/admin/roles-permissions/{role} {permissionIds[]}
    alt all permissionIds exist in the catalog
        S->>DB: replaces exactly those permissions for the role (transaction)
        S-->>W: 200 updated permissions of the role
    else some id does not exist in the catalog
        S-->>W: 400 UnknownPermissionException (unknown permission, nothing is saved)
    end
    Note over S: Roles cannot be created or deleted (ADR-010).<br/>This matrix is informational: real authorization still comes<br/>from the roles claim in the JWT, not from this table (open decision, section 11.3 of the SRS)
```

*Source:* `security-service` (`RolePermissionController`, `RolePermissionAdministrationService`, migration `026-security-role-permissions.sql`), ADR-015.

---

## 3. Activity Diagrams

The activity diagrams show the business processes as they work in the system. There is no payment gateway: the customer uploads a receipt and the administrator reviews it (ADR-008).

### 3.1 Authentication (RF-001 to RF-004)

```mermaid
flowchart TD
    start([Start]) --> menu[Show the sign-in screen]
    menu --> choice{What does the user want to do?}

    choice -->|Register| f1[Show the registration form]
    f1 --> d1[Enter data and accept the data policy]
    d1 --> v1{Fields complete and<br/>email valid and available?}
    v1 -->|No| e1[Show the field with the error]
    e1 --> d1
    v1 -->|Yes| v2{Does the password meet<br/>the RNF-004 policy?}
    v2 -->|No| e2[Show the password requirements]
    e2 --> d1
    v2 -->|Yes| ok1[Create account + customer profile]
    ok1 --> mail1[Send welcome email]
    mail1 --> stop1([End])

    choice -->|Sign in| f2[Show the sign-in form]
    f2 --> d2[Enter email and password]
    d2 --> v3{Account exists, is<br/>active and password is correct?}
    v3 -->|No| e3[Generic error message]
    e3 --> d2
    v3 -->|"5 failures in 15 min"| lock["Lock the account for 15 min (RF-004b, pending)"]
    lock --> stop2([End])
    v3 -->|Yes| ok2[Issue JWT and redirect to the dashboard of the role]
    ok2 --> stop3([End])

    choice -->|Recover password| f3[Ask for the email]
    f3 --> d3[Enter email]
    d3 --> v4{Is the email registered?}
    v4 -->|No| e4["Same generic response<br/>(does not reveal whether it exists)"]
    e4 --> stop4([End])
    v4 -->|Yes| code[Send a 6-digit code that expires in 15 min]
    code --> d4[Enter code and new password]
    d4 --> v5{Is the code valid<br/>and not expired?}
    v5 -->|No, 5 attempts| e5[Request a new code]
    e5 --> f3
    v5 -->|Yes| ok3[Update password, invalidate code]
    ok3 --> stop5([End])

    choice -->|Change password| auth{Is the user authenticated?}
    auth -->|No| stop6([End])
    auth -->|Yes| d5[Enter current and new password]
    d5 --> v6{Current one correct and<br/>new one meets the policy?}
    v6 -->|No| e6[Show error]
    e6 --> d5
    v6 -->|Yes| ok4[Update password]
    ok4 --> stop7([End])
```

### 3.2 Booking a wash (RF-005, RF-006, RF-007)

```mermaid
flowchart TD
    start([Start]) --> veh{Does the customer have<br/>at least one vehicle?}
    veh -->|No| regveh["Ask them to register a vehicle (CU26)"]
    regveh --> stop0([End])
    veh -->|Yes| sel[Choose vehicle and one or more services]
    sel --> price[Show the price for the vehicle type]
    price --> date[Choose date and time]
    date --> check[Check opening hours, exceptions and bays]
    check --> avail{Is there a free bay<br/>in that slot?}
    avail -->|No| alt[Offer up to 5 alternative times on the same day]
    alt --> date
    avail -->|Yes| confirm[Confirm booking: assign bay, freeze prices]
    confirm --> notif[Send confirmation and schedule 24h/1h reminders]
    notif --> stop1([End: booking Confirmed])

    stop1 -.-> manage{Does the customer want<br/>to reschedule or cancel?}
    manage -->|Reschedule| state{Is the booking Scheduled<br/>or Confirmed?}
    state -->|No - in progress/finished| block[Block the action with an explanatory message]
    block --> stop2([End])
    state -->|Yes| date
    manage -->|Cancel| reason[Ask for a reason from the list of reasons]
    reason --> free[Free the bay, mark as Cancelled]
    free --> stop3([End])
```

### 3.3 Operator assignment and service execution (RF-008, RF-009, RF-011, RF-012b)

```mermaid
flowchart TD
    start([Confirmed booking without an operator]) --> auto{"Does automatic assignment<br/>find an eligible operator?<br/>(RF-008, partial)"}
    auto -->|Yes| pick[Pick the one with the fewest open jobs<br/>tie: lowest identifier]
    pick --> notifyop[Notify the operator]
    notifyop --> stopA([End])
    auto -->|No eligible operators| manual[Notify the administrator for manual assignment]
    manual --> list[Admin sees candidates: available first, with rating]
    list --> chooseop[Admin picks an operator]
    chooseop --> valid{Operator active, on shift,<br/>not absent and with no schedule overlap?}
    valid -->|No| blockop[Block assignment, show reason]
    blockop --> list
    valid -->|Yes| assign[Create PENDING execution, notify the operator]
    assign --> stopB([End])

    stopB -.-> today{Is it the day of the booking?}
    today -->|No| blockday[Block service start]
    blockday --> stopC([End])
    today -->|Yes| startsvc[Operator marks Start service]
    startsvc --> inprog[Execution → In progress]
    inprog --> finish[Operator marks Finish service]
    finish --> completed[Execution → Completed, booking → Completed]
    completed --> rate["Customer can rate (CU15)"]
    rate --> stopD([End])
```

### 3.4 Paying for a booking (RF-013, RF-013b, RF-014, RF-016)

```mermaid
flowchart TD
    start([Confirmed booking without an approved payment]) --> method{Which payment method?}

    method -->|QR / Transfer / Nequi / Daviplata| showqr[Show the QR of the active account and instructions]
    showqr --> extpay[Customer pays from their bank app<br/>outside the platform]
    extpay --> upload[Uploads receipt + declared amount + reference code]
    upload --> dup{Reference code<br/>already used in another booking?}
    dup -->|Yes| rejectref[Reject: TRANSACTIONREFERENCEREUSED]
    rejectref --> stop1([End])
    dup -->|No| inreview["Payment → Under review (linked to the booking)"]
    inreview --> stop2([End: waiting for the admin])

    method -->|Cash| cash[Customer pays at the site]
    cash --> register[Admin records the payment manually]
    register --> approved1["Payment → Approved directly"]
    approved1 --> points1["Credit loyalty points (RF-026)"]
    points1 --> stop3([End])

    stop2 -.-> review[Admin opens pending payments]
    review --> compare{Declared amount =<br/>amount due and receipt readable?}
    compare -->|No| reject[Reject with a reason, customer can resend]
    reject --> stop4([End])
    compare -->|Yes| approve["Payment → Approved"]
    approve --> points2["Credit loyalty points (RF-026)"]
    points2 --> notifyc[Notify the customer]
    notifyc --> stop5([End])
```

### 3.5 Redeeming a loyalty coupon (RF-024, RF-025, RF-026)

```mermaid
flowchart TD
    start([Customer on the payment screen]) --> has{Do they have promotions<br/>unlocked by their points?}
    has -->|No| noshow[No coupon is offered]
    noshow --> stop1([End])
    has -->|Yes| enter[Enters the coupon code]
    enter --> valid{Valid, active,<br/>unlocked and not redeemed<br/>before for this booking?}
    valid -->|No| inform["Report the reason and keep the original amount<br/>(expired coupon / not enough points / already redeemed / used up)"]
    inform --> stop2([End])
    valid -->|Yes| limit{"Within the usage limit<br/>(total and per customer)?"}
    limit -->|No| exhausted[Report: coupon used up]
    exhausted --> stop3([End])
    limit -->|Yes| calc[Calculate the discount on the subtotal<br/>without exceeding it]
    calc --> apply[Apply the discount to the total to pay]
    apply --> notify[Notify the redemption in the inbox and by email]
    notify --> stop4([End: payment continues for the discounted amount])
```

### 3.6 Managing roles and permissions (RF-029)

```mermaid
flowchart TD
    start([Admin opens Management → Roles]) --> load[Load the 3 fixed roles + permission catalog]
    load --> view[View the current permissions of each role: Administrator, Operator, Customer]
    view --> edit[Admin checks or unchecks permissions of a role]
    edit --> save[Save]
    save --> valid{Do all permission<br/>ids exist in the catalog?}
    valid -->|No| reject[Reject the save explicitly]
    reject --> edit
    valid -->|Yes| replace[Replace exactly those permissions for the role]
    replace --> stop([End: roles cannot be created or deleted])
```

---

## 4. State Diagrams

### 4.1 Booking life cycle (RF-006, RF-007)

```mermaid
stateDiagram-v2
    [*] --> CONFIRMED : create (a free bay is assigned immediately, RF-006)
    SCHEDULED --> CONFIRMED : confirm (needs a bay)
    SCHEDULED --> CANCELLED : cancel
    CONFIRMED --> CONFIRMED : reschedule (new time/bay, prices are kept)
    CONFIRMED --> IN_PROGRESS : start
    CONFIRMED --> NO_SHOW : the customer did not show up
    CONFIRMED --> CANCELLED : cancel (customer or admin, with a reason)
    IN_PROGRESS --> COMPLETED : finish
    COMPLETED --> [*]
    CANCELLED --> [*]
    NO_SHOW --> [*]
```

*Source:* `booking-service`, `Booking.moveTo`, `Booking.cancel`, `BookingStatus`. Only `SCHEDULED` and `CONFIRMED` can be rescheduled or cancelled (RF-007); `SCHEDULED` exists in the model, but the current flow always creates the booking directly as `CONFIRMED`.

### 4.2 Payment life cycle (RF-013b, RF-014, ADR-008)

```mermaid
stateDiagram-v2
    [*] --> PENDING : create (amount = booking total)
    PENDING --> PENDING : attach receipt
    PENDING --> IN_REVIEW : send for review (requires at least one receipt)
    IN_REVIEW --> APPROVED : approve (admin)
    IN_REVIEW --> REJECTED : reject (admin, reason ≤ 200 characters)
    APPROVED --> REFUNDED : refund (admin)
    REJECTED --> [*]
    REFUNDED --> [*]
    APPROVED --> [*]
```

*Source:* `payment-service`, `Payment` aggregate. A booking allows only one approved payment and only one open payment at a time; after `REJECTED` the customer can report a new payment.

### 4.3 Service execution life cycle (RF-012b)

```mermaid
stateDiagram-v2
    [*] --> PENDING : assign operator (RF-009)
    PENDING --> IN_PROGRESS : start service (RF-012b)
    IN_PROGRESS --> PAUSED : pause
    PAUSED --> IN_PROGRESS : resume
    IN_PROGRESS --> COMPLETED : finish service (RF-012b)
    IN_PROGRESS --> WITH_ISSUE : report an issue
    COMPLETED --> [*]
    WITH_ISSUE --> [*]
```

*Source:* `operations-service`. `COMPLETED` enables the customer's rating (RF-012).

### 4.4 Promotion life cycle (RF-024)

```mermaid
stateDiagram-v2
    [*] --> ACTIVE : create (code, validity, % discount, required points)
    ACTIVE --> INACTIVE : deactivate (admin)
    INACTIVE --> ACTIVE : reactivate (admin)
    ACTIVE --> EXPIRED : current date > end date
    INACTIVE --> EXPIRED : current date > end date
    EXPIRED --> [*]
    ACTIVE --> [*] : delete
    INACTIVE --> [*] : delete
```

*Source:* `payment-service`, `Promotion.IsAvailableOn` (active and within the validity period). An `INACTIVE` or `EXPIRED` promotion cannot be redeemed (RF-024, RN-PROMO-01).

---

## 5. Screen Inventory (mockup)

Screen by screen and by role, including the create and edit modals of each module. All screenshots are in the `assets/` folder of this document.

### 5.1 Common screens (no session)

| Screen | Evidence |
|---|---|
| Sign-in | ![Sign-in](../assets/01_login.png) |
| Registration | ![Registration](../assets/02_registro.png) |
| Password recovery | ![Password recovery](../assets/03_recuperar_contrasena.png) |

### 5.2 Administrator role

| Screen | Evidence |
|---|---|
| Dashboard | ![Admin dashboard](../assets/04_admin_dashboard.png) |
| Management → Users | ![Users](../assets/05_admin_usuarios.png) |
| Modal: Create user | ![Create user modal](../assets/29_modal_crear_usuario.png) |
| Management → Roles | ![Roles](../assets/06_admin_roles.png) |
| Modal: Edit role permissions | ![Edit permissions modal](../assets/30_modal_editar_permisos.png) |
| Management → Services (catalog) | ![Catalog](../assets/07_admin_catalogo.png) |
| Modal: Add service | ![Add service modal](../assets/31_modal_crear_servicio.png) |
| Management → Promotions | ![Promotions](../assets/08_admin_promociones.png) |
| Modal: Create promotion | ![Create promotion modal](../assets/32_modal_crear_promocion.png) |
| Opening hours and bays | ![Opening hours and bays](../assets/09_admin_horarios_bahias.png) |
| Modal: Add opening-hours exception | ![Add exception modal](../assets/33_modal_agregar_excepcion.png) |
| Operators | ![Operators](../assets/10_admin_operarios.png) |
| Modal: New operator | ![New operator modal](../assets/34_modal_nuevo_operario.png) |
| Modal: Assign shift | ![Assign shift modal](../assets/42_modal_asignar_turno.png) |
| Bookings | ![Bookings](../assets/11_admin_reservas.png) |
| Modal: Assign an operator to a booking | ![Assign operator modal](../assets/35_modal_asignar_operario.png) |
| Payments | ![Payments](../assets/12_admin_pagos.png) |
| Modal: Record manual payment | ![Record payment modal](../assets/36_modal_registrar_pago.png) |
| Reports | ![Reports](../assets/13_admin_reportes.png) |
| Settings → Payment accounts | ![Payment accounts](../assets/14_admin_cuentas_pago.png) |
| Modal: Add payment account | ![Payment account modal](../assets/37_modal_cuenta_pago.png) |
| Notifications | ![Admin notifications](../assets/15_admin_notificaciones.png) |
| Profile | ![Admin profile](../assets/16_admin_perfil.png) |

### 5.3 Customer role

| Screen | Evidence |
|---|---|
| Dashboard | ![Customer dashboard](../assets/17_client_dashboard.png) |
| Modal: View details of the next service | ![Booking details modal](../assets/39_modal_detalle_reserva_cliente.png) |
| My vehicles | ![Vehicles](../assets/18_client_vehiculos.png) |
| Modal: Register vehicle | ![Register vehicle modal](../assets/38_modal_registrar_vehiculo.png) |
| Book a wash | ![Book a wash](../assets/19_client_reservar.png) |
| Booking history | ![History](../assets/20_client_historial.png) |
| Pay for a service | ![Payment](../assets/21_client_pago.png) |
| Modal: Confirm booking cancellation | ![Cancel booking modal](../assets/41_modal_cancelar_reserva.png) |
| Notifications | ![Customer notifications](../assets/22_client_notificaciones.png) |
| Settings (theme and language) | ![Settings](../assets/23_client_configuracion.png) |

### 5.4 Operator role

| Screen | Evidence |
|---|---|
| Main dashboard | ![Operator dashboard](../assets/24_operario_home.png) |
| Assigned services | ![Assigned services](../assets/25_operario_servicios_asignados.png) |
| My schedule (availability) | ![My schedule](../assets/26_operario_horario.png) |
| Service history | ![Operator history](../assets/27_operario_historial.png) |
| Ratings received | ![Ratings](../assets/28_operario_calificaciones.png) |

---

## Correlation with the Software Requirements Specification

| Dynamic view in this document | Requirements it illustrates |
|---|---|
| §2.1 Registration and welcome | RF-001, RF-018 |
| §2.2 Booking a wash | RF-005, RF-006 |
| §2.3 Booking reminder | RF-018 |
| §2.4 Assignment and execution | RF-008, RF-009, RF-011, RF-012, RF-012b |
| §2.5 Payment by receipt | RF-013, RF-013b, RF-014, RF-016 |
| §2.6 Coupon redemption and points | RF-024, RF-025, RF-026 |
| §2.7 Roles and permissions | RF-029 |
| §3.1 to §3.6 Activities | The whole authentication, booking, operations, payment and promotion module |
| §4.1 to §4.4 States | RF-006, RF-007, RF-012b, RF-013b, RF-014, RF-024 |
