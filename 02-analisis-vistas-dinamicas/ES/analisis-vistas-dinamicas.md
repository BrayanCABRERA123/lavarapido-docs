# Análisis del Software: Vistas Dinámicas del Sistema LavaRápido

Juan Camilo Guilombo Osorio, Brayan Estiven Patiño Cabrera y Merari Urbano Quintero

Centro de la Industria, la Empresa y los Servicios, Servicio Nacional de Aprendizaje (SENA), Regional Huila

Tecnólogo en Análisis y Desarrollo de Software (ADSO), ficha 3145556

Instructora: Karol Daniela Correa

Versión 1.0, 9 de octubre de 2026

---

## Introducción

Este documento muestra cómo se comporta LavaRápido cuando alguien lo usa: qué pasa, en qué orden y entre qué pantallas y servicios. Está organizado en cuatro partes:

1. **Casos de uso por actor**, con sus relaciones `«include»`/`«extend»`.
2. **Diagramas de secuencia** de los flujos principales: de la pantalla al gateway, del gateway al servicio, del servicio a la base de datos o a otro servicio.
3. **Diagramas de actividades** de los procesos de negocio.
4. **Diagramas de estados** de las entidades que cambian de estado (reserva, pago, ejecución del servicio).

Los diagramas están hechos en Mermaid y se revisaron contra el código y el sistema en ejecución el 9 de octubre de 2026. Al final está el inventario de pantallas, con capturas por rol.

La especificación completa de cada requisito y caso de uso (actores, precondición, flujo normal, flujos alternos y postcondición) está en el *Informe de especificación de requisitos*, secciones 5 y 7.3; aquí se citan por su identificador (RF-XXX, CUXX).

---

## 1. Casos de Uso por Actor

### 1.1 Diagrama de Casos de Uso

Los 29 casos de uso se presentan en cuatro diagramas, uno por actor, agrupados por módulo.

**Casos de uso comunes a los tres roles**

```mermaid
flowchart LR
    Usuario(["Cualquier usuario"])
    CU01(["CU01 Iniciar sesión"])
    CU03(["CU03 Recuperar contraseña"])
    CU04(["CU04 Cambiar contraseña"])
    CU16(["CU16 Consultar panel"])
    CU17(["CU17 Gestionar notificaciones"])
    CU18(["CU18 Personalizar tema visual"])
    CU19(["CU19 Seleccionar idioma"])

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

**Casos de uso del Cliente**

```mermaid
flowchart LR
    Cliente(["Cliente"])
    Sistema(["Sistema"])

    subgraph CTA["Cuenta y vehículos"]
        CU02(["CU02 Crear cuenta"])
        CU26(["CU26 Gestionar vehículos"])
    end

    subgraph RES["Reservas"]
        CU05(["CU05 Solicitar reserva"])
        CU06(["CU06 Confirmar reserva según disponibilidad"])
        CU07(["CU07 Modificar o cancelar reserva"])
    end

    subgraph PAG["Pagos y fidelización"]
        CU12(["CU12 Pagar una reserva"])
        CU14(["CU14 Consultar historial de pagos"])
        CU25(["CU25 Aplicar promoción en el pago"])
        CU15(["CU15 Calificar servicio"])
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

**Casos de uso del Operario**

```mermaid
flowchart LR
    Operario(["Operario"])
    CU10(["CU10 Consultar servicios asignados"])
    CU11(["CU11 Iniciar y finalizar servicio"])
    CU22(["CU22 Gestionar disponibilidad de operarios"])

    Operario --- CU10
    Operario --- CU11
    Operario -. "consulta" .- CU22

    classDef actor fill:#08427b,color:#fff,stroke:#052e56
    class Operario actor
```

**Casos de uso del Administrador y del Sistema**

```mermaid
flowchart LR
    Administrador(["Administrador"])
    Sistema(["Sistema"])

    subgraph AUTH["Usuarios"]
        CU27(["CU27 Administrar usuarios y permisos"])
    end
    subgraph CAT["Catálogo, horario y bahías"]
        CU20(["CU20 Configurar horario y bahías"])
        CU21(["CU21 Gestionar catálogo y precios"])
    end
    subgraph RES["Reservas y operación"]
        CU08(["CU08 Asignar operario automáticamente"])
        CU09(["CU09 Asignar o reasignar operario"])
        CU22b(["CU22 Gestionar disponibilidad de operarios"])
        CU29(["CU29 Gestionar reservas"])
    end
    subgraph PAG["Pagos y promociones"]
        CU13(["CU13 Revisar pago"])
        CU28(["CU28 Gestionar cuentas de pago"])
        CU24(["CU24 Gestionar promociones"])
    end
    subgraph REP["Reportes"]
        CU23(["CU23 Consultar reportes"])
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

*Nota.* `«include»` indica que CU05 siempre ejecuta CU06; `«extend»` indica que CU25 amplía opcionalmente CU12. CU22 aparece como consulta para el operario y como gestión para el administrador, que es quien registra los turnos y las ausencias (RF-022).

### 1.2 Matriz de Actores y Casos de Uso

| Actor | Casos de uso |
|---|---|
| Todos los roles | CU01, CU03, CU04, CU16, CU17, CU18, CU19 |
| Cliente | CU02, CU05, CU06, CU07, CU12, CU14, CU15, CU25, CU26 |
| Operario | CU10, CU11, CU22 (consulta) |
| Administrador | CU09, CU13, CU20, CU21, CU22, CU23, CU24, CU27, CU28, CU29 |
| Sistema | CU06 (incluido en CU05), CU08 |

La especificación de cada uno de los 29 casos de uso (precondición, flujo normal, flujos alternos, postcondición, estado) está en el *Informe de especificación de requisitos*, Tablas 23 a 51.

---

## 2. Diagramas de Secuencia

Cada diagrama sigue el recorrido de la petición (pantalla, gateway, servicios, base de datos y RabbitMQ) con los nombres de clases y endpoints del código. Los cinco primeros parten de los diagramas de `vehicle-w-docs/08-uml/diagrams/source/`; los dos últimos cubren la fidelización y los roles y permisos.

### 2.1 Registro y bienvenida (RF-001, RF-018)

```mermaid
sequenceDiagram
    autonumber
    actor C as Cliente
    participant W as Web
    participant GW as API Gateway
    participant S as security-service
    participant MQ as RabbitMQ
    participant CU as customer-service
    participant N as notification-service
    participant M as SMTP

    C->>W: Llena el formulario de registro
    W->>GW: POST /api/v1/auth/register
    GW->>S: enruta
    S->>S: Valida (política de contraseña, correo/documento únicos), guarda persona + cuenta (CLIENT)
    S-->>W: 201 Created
    S-)MQ: UserRegistered (security.user_registered), tras el commit
    par perfil de cliente
        MQ-)CU: UserRegistered
        CU->>CU: Crea el perfil de cliente (idempotente)
    and bienvenida
        MQ-)N: UserRegistered
        N->>N: Crea notificación WELCOME (idempotente: processed_event)
        N->>M: Correo de bienvenida (la dirección viene en el evento)
    end
    C->>W: Inicia sesión
    W->>GW: POST /api/v1/auth/login
    GW->>S: enruta
    S-->>W: 200 JWT (HS256, 1 h, claim roles)
```

*Fuente:* `security-service` (`AccountRegistrationService`, `AuthenticationService`), evento `security.user_registered`.

### 2.2 Reservar un lavado (RF-005, RF-006)

```mermaid
sequenceDiagram
    autonumber
    actor C as Cliente
    participant W as Web (vía gateway)
    participant B as booking-service
    participant CU as customer-service
    participant DB as SQL Server
    participant MQ as RabbitMQ
    participant N as notification-service
    participant S as security-service

    C->>W: Elige vehículo, servicio y fecha
    W->>B: GET /api/v1/bookings/availability?date=…&vehicleTypeId=…&serviceIds=…
    B->>DB: horario, excepciones, bahías, reservas del día
    B-->>W: horas libres
    C->>W: Confirma una hora
    W->>B: POST /api/v1/bookings
    B->>CU: GET /api/v1/vehicles/{id} (JWT del cliente)
    CU-->>B: vehículo + tipo (se valida la propiedad, INV-BOOK-002)
    B->>DB: sp_getapplock (bloqueo del horario)
    alt hay bahía libre y el vehículo no tiene otra reserva a esa hora
        B->>DB: INSERT reserva CONFIRMED + bahía + líneas con precios congelados
        B-->>W: 201 reserva (código RES-000042)
        B-)MQ: BookingConfirmed (booking.confirmed), tras el commit
        MQ-)N: BookingConfirmed
        N->>S: GET /internal/v1/users/{id}/contact (X-Internal-Key)
        N->>N: Notificación BOOKING_CONFIRMED + recordatorios (24 h, 1 h)
        N-->>C: bandeja + push + correo
    else horario ocupado
        B-->>W: 409 SLOT_UNAVAILABLE + hasta 5 horas alternativas
    end
```

*Fuente:* `booking-service` (`BookingService.confirmNew`), contrato en `07-api/contracts/openapi/booking-service.yaml`.

### 2.3 Recordatorio de reserva (ADR-011 §7)

```mermaid
sequenceDiagram
    autonumber
    participant MQ as RabbitMQ
    participant N as notification-service
    participant DB as notification.booking_reminder
    participant J as ReminderScheduler
    participant S as security-service
    actor C as Cliente

    MQ-)N: BookingConfirmed (nueva o reprogramada)
    N->>DB: Reemplaza recordatorios pendientes: uno por anticipación (24 h, 1 h) que siga en el futuro
    MQ-)N: BookingCancelled
    N->>DB: Cancela los recordatorios pendientes de esa reserva (borrado lógico)
    loop cada 5 minutos (REMINDER_CHECK_INTERVAL)
        J->>DB: Recordatorios vencidos (remind_at <= ahora, no enviados)
        J->>S: GET /internal/v1/users/{id}/contact (X-Internal-Key)
        J->>N: Notificación BOOKING_REMINDER
        N-->>C: bandeja + push + correo
        J->>DB: marca sent_at (nunca se envía dos veces)
    end
```

*Fuente:* `notification-service` (`BookingReminderService`, `ReminderScheduler`).

### 2.4 Asignación de operario, ejecución y calificación (RF-009, RF-011, RF-012, RF-012b)

```mermaid
sequenceDiagram
    autonumber
    actor A as Administrador
    actor O as Operario
    actor C as Cliente
    participant W as Web (vía gateway)
    participant OP as operations-service
    participant B as booking-service
    participant S as security-service
    participant DB as SQL Server (execution)
    participant MQ as RabbitMQ
    participant N as notification-service

    A->>W: Abre una reserva → Asignación de operario
    W->>OP: GET /api/v1/admin/assignments/{bookingId}/candidates
    OP->>B: GET /admin/bookings/{id} y /admin/bookings?from=&to= (JWT admin)
    OP->>S: GET /admin/users?role=OPERATOR (JWT admin)
    OP->>DB: turnos, ausencias, ejecuciones del día
    OP-->>W: cada operario + motivo de bloqueo (disponibles primero)
    A->>W: Elige un operario
    W->>OP: PUT /api/v1/admin/assignments/{bookingId}
    alt reserva SCHEDULED/CONFIRMED y AssignmentPolicy no encuentra motivo de bloqueo
        OP->>DB: una service_execution PENDING por línea de la reserva
        OP-->>W: 200 asignación
        OP-)MQ: OperatorAssigned (execution.operator_assigned), tras el commit
        MQ-)N: notifica al operario y al cliente
    else inactivo / sin turno / ausente / ocupado
        OP-->>W: 409 OPERATOR_INACTIVE | OPERATOR_NOT_ON_SHIFT | OPERATOR_ABSENT | OPERATOR_BUSY
    end

    O->>W: Servicios asignados → Iniciar servicio (solo el día de la reserva)
    W->>OP: POST /api/v1/operator/services/{bookingId}/start
    OP->>B: PATCH /operator/bookings/{id}/status IN_PROGRESS (JWT operario)
    OP->>DB: líneas → IN_PROGRESS, started_at
    OP-)MQ: ServiceStarted (execution.service_started)
    O->>W: Finalizar servicio
    W->>OP: POST /api/v1/operator/services/{bookingId}/finish
    OP->>B: PATCH /operator/bookings/{id}/status COMPLETED
    OP->>DB: líneas → COMPLETED, finished_at
    OP-)MQ: ServiceCompleted (execution.service_completed)
    MQ-)N: avisa al cliente que el lavado terminó

    C->>W: Historial → califica la reserva completada
    W->>OP: POST /api/v1/ratings/{bookingId} {puntuación 1–5, comentario}
    OP->>B: GET /bookings/{id} (JWT cliente: solo sus reservas)
    OP->>DB: calificación en cada línea (una sola vez)
    OP-->>W: 201 calificación
```

*Fuente:* `operations-service` (`OperationsService.candidates / assign / start / finish / rate`, `AssignmentPolicy`, ADR-014).

### 2.5 Pago por comprobante y revisión (RF-013, RF-013b, RF-014)

```mermaid
sequenceDiagram
    autonumber
    actor C as Cliente
    actor A as Administrador
    participant W as Web (vía gateway)
    participant P as payment-service (.NET)
    participant B as booking-service
    participant DB as SQL Server (payment)

    C->>W: Paga el servicio
    W->>P: GET /api/v1/payment-accounts
    P-->>W: cuentas activas que requieren comprobante (QR, instrucciones)
    C->>C: Paga desde la app del banco (fuera de la plataforma)
    C->>W: Cuenta, código de referencia, imagen del comprobante
    W->>P: POST /api/v1/payments
    P->>B: GET /bookings/{id} (JWT cliente)
    B-->>P: estado, total, dueño
    alt reserva pagable y sin pago abierto/aprobado
        P->>DB: pago PENDING (monto = total de la reserva) + comprobante → IN_REVIEW
        P-->>W: 201 pago IN_REVIEW
    else no pagable / ya reportado / ya aprobado
        P-->>W: 400 BOOKING_NOT_PAYABLE | 409 PAYMENT_ALREADY_REPORTED | 409 PAYMENT_ALREADY_APPROVED
    end

    A->>W: Pagos → Verificar
    W->>P: GET /api/v1/admin/payments?status=IN_REVIEW
    P->>B: GET /admin/bookings/{id} (JWT admin) por cada pago
    P-->>W: pagos con los datos de su reserva
    alt aprobar
        W->>P: POST /api/v1/admin/payments/{id}/approve
        P->>DB: APPROVED, approved_by, processed_at (índice único: uno por reserva)
    else rechazar
        W->>P: POST /api/v1/admin/payments/{id}/reject {motivo}
        P->>DB: REJECTED + motivo (el cliente puede reportar de nuevo)
    end

    A->>W: Pagos → Registro manual (efectivo en el local)
    W->>P: POST /api/v1/admin/payments {bookingId, paymentAccountId}
    P->>B: GET /admin/bookings/{id}
    P->>DB: pago APPROVED directamente (monto = total de la reserva)
```

*Fuente:* `payment-service` (`PaymentApplicationService.ReportPaymentAsync / ApproveAsync / RejectAsync / RegisterManualAsync`, agregado `Payment`, ADR-008, ADR-013).

### 2.6 Canje de cupón y puntos de fidelización (RF-024, RF-025, RF-026)

```mermaid
sequenceDiagram
    autonumber
    actor C as Cliente
    actor A as Administrador
    participant W as Web (vía gateway)
    participant P as payment-service (.NET)
    participant B as booking-service
    participant DB as SQL Server (promotion / payment)
    participant MQ as RabbitMQ
    participant N as notification-service

    A->>W: Gestión → Promociones → Crear
    W->>P: POST /api/v1/admin/promotions {código, vigencia, % descuento 1-100, puntos requeridos}
    P->>DB: INSERT promotion
    P-->>W: 201 promoción

    Note over C,P: --- Acreditación de puntos (al aprobar un pago, flujo 2.5) ---
    P->>DB: INSERT loyalty_transaction (+puntos del servicio pagado, sequence_no único por cliente)
    Note over P: El saldo nunca se guarda aparte: se calcula siempre<br/>desde la última fila del libro de movimientos (INV-LOY-001)

    C->>W: Dashboard → ve sus puntos y promociones desbloqueadas
    W->>P: GET /api/v1/loyalty/balance
    P->>DB: SELECT último movimiento del cliente (saldo vigente)
    P-->>W: puntos actuales
    W->>P: GET /api/v1/loyalty/promotions
    P->>DB: promociones vigentes
    P-->>W: cada promoción + si ya está desbloqueada (puntos >= requeridos)

    C->>W: Pago de una reserva → ingresa el código del cupón
    W->>P: POST /api/v1/loyalty/redeem {bookingId, código}
    P->>B: valida que la reserva sea del cliente y no tenga pago reportado
    P->>DB: busca la promoción por código
    alt vigente, desbloqueada, no canjeada antes en esta reserva y dentro de los límites de uso
        P->>P: Promotion.Redeem(...) calcula el descuento sobre el subtotal (nunca lo supera)
        P->>DB: INSERT promotion_redemption (consume un uso, así que dos canjes simultáneos chocan entre sí)
        P-)MQ: PromotionRedeemed (payment.promotion_redeemed)
        MQ-)N: notifica el canje en la bandeja y por correo
        P-->>W: 200 {descuento aplicado, nuevo total a pagar}
    else vencida / no desbloqueada / ya canjeada / sin cupos
        P-->>W: 409 PromotionNotRedeemable | PromotionAlreadyRedeemed | PromotionExhausted | PromotionCustomerLimitReached
    end
```

*Fuente:* `payment-service` (`LoyaltyController`, `CustomerPromotionService.RedeemAsync`, agregado `Promotion.Redeem`, `LoyaltyLedgerRepository`), ADR-015.

### 2.7 Gestión de roles y permisos (RF-029)

```mermaid
sequenceDiagram
    autonumber
    actor A as Administrador
    participant W as Web (vía gateway)
    participant S as security-service
    participant DB as SQL Server (security)

    A->>W: Gestión → Roles
    W->>S: GET /api/v1/admin/roles-permissions
    S->>DB: SELECT catálogo de permisos + permisos de cada rol
    S-->>W: 200 {permisos[], roles: [{rol, permisos[]}]}, 3 roles fijos: ADMIN, OPERATOR, CLIENT
    A->>W: Marca/desmarca permisos de un rol y guarda
    W->>S: PUT /api/v1/admin/roles-permissions/{rol} {permissionIds[]}
    alt todos los permissionIds existen en el catálogo
        S->>DB: reemplaza exactamente esos permisos para el rol (transacción)
        S-->>W: 200 permisos actualizados del rol
    else algún id no existe en el catálogo
        S-->>W: 400 UnknownPermissionException (permiso inexistente, no se guarda nada)
    end
    Note over S: No se pueden crear ni borrar roles (ADR-010).<br/>Esta matriz es informativa: la autorización real sigue viniendo<br/>del claim roles del JWT, no de esta tabla (decisión abierta, sección 11.3 del SRS)
```

*Fuente:* `security-service` (`RolePermissionController`, `RolePermissionAdministrationService`, migración `026-security-role-permissions.sql`), ADR-015.

---

## 3. Diagramas de Actividades

Los diagramas de actividades muestran los procesos de negocio tal como funcionan en el sistema. En los pagos no hay pasarela: el cliente sube un comprobante y el administrador lo revisa (ADR-008).

### 3.1 Autenticación (RF-001 a RF-004)

```mermaid
flowchart TD
    start([Inicio]) --> menu[Mostrar pantalla de ingreso]
    menu --> choice{¿Qué desea hacer?}

    choice -->|Registrarse| f1[Mostrar formulario de registro]
    f1 --> d1[Ingresar datos y aceptar política de datos]
    d1 --> v1{¿Campos completos y<br/>correo válido y disponible?}
    v1 -->|No| e1[Mostrar el campo con error]
    e1 --> d1
    v1 -->|Sí| v2{¿Contraseña cumple<br/>la política RNF-004?}
    v2 -->|No| e2[Mostrar requisitos de contraseña]
    e2 --> d1
    v2 -->|Sí| ok1[Crear cuenta + perfil de cliente]
    ok1 --> mail1[Enviar correo de bienvenida]
    mail1 --> stop1([Fin])

    choice -->|Iniciar sesión| f2[Mostrar formulario de login]
    f2 --> d2[Ingresar correo y contraseña]
    d2 --> v3{¿Cuenta existe,<br/>activa y contraseña correcta?}
    v3 -->|No| e3[Mensaje genérico de error]
    e3 --> d2
    v3 -->|"5 fallos en 15 min"| lock["Bloquear cuenta 15 min (RF-004b, pendiente)"]
    lock --> stop2([Fin])
    v3 -->|Sí| ok2[Emitir JWT y redirigir al panel del rol]
    ok2 --> stop3([Fin])

    choice -->|Recuperar contraseña| f3[Pedir el correo]
    f3 --> d3[Ingresar correo]
    d3 --> v4{¿Correo registrado?}
    v4 -->|No| e4["Misma respuesta genérica<br/>(no revela si existe)"]
    e4 --> stop4([Fin])
    v4 -->|Sí| code[Enviar código de 6 dígitos, vence en 15 min]
    code --> d4[Ingresar código y nueva contraseña]
    d4 --> v5{¿Código válido<br/>y no vencido?}
    v5 -->|No, 5 intentos| e5[Pedir código nuevo]
    e5 --> f3
    v5 -->|Sí| ok3[Actualizar contraseña, invalidar código]
    ok3 --> stop5([Fin])

    choice -->|Cambiar contraseña| auth{¿Usuario autenticado?}
    auth -->|No| stop6([Fin])
    auth -->|Sí| d5[Ingresar contraseña actual y nueva]
    d5 --> v6{¿Actual correcta y<br/>nueva cumple la política?}
    v6 -->|No| e6[Mostrar error]
    e6 --> d5
    v6 -->|Sí| ok4[Actualizar contraseña]
    ok4 --> stop7([Fin])
```

### 3.2 Reservar un lavado (RF-005, RF-006, RF-007)

```mermaid
flowchart TD
    start([Inicio]) --> veh{¿Cliente tiene<br/>al menos un vehículo?}
    veh -->|No| regveh["Pedir que registre un vehículo (CU26)"]
    regveh --> stop0([Fin])
    veh -->|Sí| sel[Elegir vehículo y uno o más servicios]
    sel --> price[Mostrar precio según el tipo de vehículo]
    price --> date[Elegir fecha y hora]
    date --> check[Validar horario del local, excepciones y bahías]
    check --> avail{¿Hay bahía libre<br/>en esa franja?}
    avail -->|No| alt[Ofrecer hasta 5 horas alternativas del mismo día]
    alt --> date
    avail -->|Sí| confirm[Confirmar reserva: asignar bahía, congelar precios]
    confirm --> notif[Notificar confirmación y programar recordatorios 24h/1h]
    notif --> stop1([Fin: reserva Confirmada])

    stop1 -.-> manage{¿El cliente quiere<br/>modificar o cancelar?}
    manage -->|Reprogramar| state{¿Reserva Programada<br/>o Confirmada?}
    state -->|No - en proceso/terminada| block[Bloquear la acción con mensaje explicativo]
    block --> stop2([Fin])
    state -->|Sí| date
    manage -->|Cancelar| reason[Pedir motivo del catálogo de motivos]
    reason --> free[Liberar la bahía, marcar Cancelada]
    free --> stop3([Fin])
```

### 3.3 Asignación de operario y ejecución del servicio (RF-008, RF-009, RF-011, RF-012b)

```mermaid
flowchart TD
    start([Reserva Confirmada sin operario]) --> auto{"¿Asignación automática<br/>encuentra un elegible?<br/>(RF-008, parcial)"}
    auto -->|Sí| pick[Elegir el de menos trabajos abiertos<br/>empate: menor identificador]
    pick --> notifyop[Notificar al operario]
    notifyop --> stopA([Fin])
    auto -->|No hay elegibles| manual[Notificar al administrador para asignación manual]
    manual --> list[Admin ve candidatos: disponibles primero, con calificación]
    list --> chooseop[Admin elige un operario]
    chooseop --> valid{¿Operario activo, en turno,<br/>sin ausencia y sin cruce de horario?}
    valid -->|No| blockop[Bloquear asignación, mostrar motivo]
    blockop --> list
    valid -->|Sí| assign[Crear ejecución PENDING, notificar al operario]
    assign --> stopB([Fin])

    stopB -.-> today{¿Es el día de la reserva?}
    today -->|No| blockday[Bloquear inicio del servicio]
    blockday --> stopC([Fin])
    today -->|Sí| startsvc[Operario marca Iniciar servicio]
    startsvc --> inprog[Ejecución → En proceso]
    inprog --> finish[Operario marca Finalizar servicio]
    finish --> completed[Ejecución → Completada; reserva → Completada]
    completed --> rate["Cliente puede calificar (CU15)"]
    rate --> stopD([Fin])
```

### 3.4 Pagar una reserva (RF-013, RF-013b, RF-014, RF-016)

```mermaid
flowchart TD
    start([Reserva Confirmada sin pago aprobado]) --> method{¿Qué método de pago?}

    method -->|QR / Transferencia / Nequi / Daviplata| showqr[Mostrar QR de la cuenta activa e instrucciones]
    showqr --> extpay[Cliente paga desde su app bancaria<br/>fuera de la plataforma]
    extpay --> upload[Sube comprobante + valor declarado + código de referencia]
    upload --> dup{¿Código de referencia<br/>ya usado en otra reserva?}
    dup -->|Sí| rejectref[Rechazar: TRANSACTIONREFERENCEREUSED]
    rejectref --> stop1([Fin])
    dup -->|No| inreview["Pago → En revisión (ligado a la reserva)"]
    inreview --> stop2([Fin: esperando al admin])

    method -->|Efectivo| cash[Cliente paga en el local]
    cash --> register[Admin registra el pago manualmente]
    register --> approved1["Pago → Aprobado directamente"]
    approved1 --> points1["Acreditar puntos de fidelización (RF-026)"]
    points1 --> stop3([Fin])

    stop2 -.-> review[Admin abre pagos pendientes]
    review --> compare{¿Valor declarado =<br/>valor a pagar y comprobante legible?}
    compare -->|No| reject[Rechazar con motivo; cliente puede reenviar]
    reject --> stop4([Fin])
    compare -->|Sí| approve["Pago → Aprobado"]
    approve --> points2["Acreditar puntos de fidelización (RF-026)"]
    points2 --> notifyc[Notificar al cliente]
    notifyc --> stop5([Fin])
```

### 3.5 Canjear un cupón de fidelización (RF-024, RF-025, RF-026)

```mermaid
flowchart TD
    start([Cliente en la pantalla de pago]) --> has{¿Tiene promociones<br/>desbloqueadas por sus puntos?}
    has -->|No| noshow[No se ofrece ningún cupón]
    noshow --> stop1([Fin])
    has -->|Sí| enter[Ingresa el código del cupón]
    enter --> valid{¿Vigente, activa,<br/>desbloqueada y no canjeada<br/>antes en esta reserva?}
    valid -->|No| inform["Informar el motivo y mantener el valor original<br/>(cupón vencido / sin puntos / ya canjeado / agotado)"]
    inform --> stop2([Fin])
    valid -->|Sí| limit{"¿Dentro del límite de usos<br/>(total y por cliente)?"}
    limit -->|No| exhausted[Informar: cupón agotado]
    exhausted --> stop3([Fin])
    limit -->|Sí| calc[Calcular descuento sobre el subtotal<br/>sin superarlo]
    calc --> apply[Aplicar descuento al total a pagar]
    apply --> notify[Notificar el canje en la bandeja y por correo]
    notify --> stop4([Fin: continúa el pago por el valor con descuento])
```

### 3.6 Gestionar roles y permisos (RF-029)

```mermaid
flowchart TD
    start([Admin abre Gestión → Roles]) --> load[Cargar los 3 roles fijos + catálogo de permisos]
    load --> view[Ver permisos actuales de cada rol: Administrador, Operario, Cliente]
    view --> edit[Admin marca/desmarca permisos de un rol]
    edit --> save[Guardar]
    save --> valid{¿Todos los ids de<br/>permiso existen en el catálogo?}
    valid -->|No| reject[Rechazar explícitamente el guardado]
    reject --> edit
    valid -->|Sí| replace[Reemplazar exactamente esos permisos para el rol]
    replace --> stop([Fin: no se pueden crear ni borrar roles])
```

---

## 4. Diagramas de Estados

### 4.1 Ciclo de vida de la reserva (RF-006, RF-007)

```mermaid
stateDiagram-v2
    [*] --> CONFIRMED : crear (se asigna bahía libre de inmediato, RF-006)
    SCHEDULED --> CONFIRMED : confirmar (necesita bahía)
    SCHEDULED --> CANCELLED : cancelar
    CONFIRMED --> CONFIRMED : reprogramar (nueva hora/bahía, se conservan precios)
    CONFIRMED --> IN_PROGRESS : iniciar
    CONFIRMED --> NO_SHOW : el cliente no llegó
    CONFIRMED --> CANCELLED : cancelar (cliente o admin, con motivo)
    IN_PROGRESS --> COMPLETED : finalizar
    COMPLETED --> [*]
    CANCELLED --> [*]
    NO_SHOW --> [*]
```

*Fuente:* `booking-service`, `Booking.moveTo`, `Booking.cancel`, `BookingStatus`. Solo `SCHEDULED` y `CONFIRMED` se pueden reprogramar o cancelar (RF-007); `SCHEDULED` existe en el modelo pero el flujo actual siempre crea la reserva directo en `CONFIRMED`.

### 4.2 Ciclo de vida del pago (RF-013b, RF-014, ADR-008)

```mermaid
stateDiagram-v2
    [*] --> PENDING : crear (monto = total de la reserva)
    PENDING --> PENDING : adjuntar comprobante
    PENDING --> IN_REVIEW : enviar a revisión (requiere al menos un comprobante)
    IN_REVIEW --> APPROVED : aprobar (admin)
    IN_REVIEW --> REJECTED : rechazar (admin, motivo ≤ 200 caracteres)
    APPROVED --> REFUNDED : reembolsar (admin)
    REJECTED --> [*]
    REFUNDED --> [*]
    APPROVED --> [*]
```

*Fuente:* `payment-service`, agregado `Payment`. Una reserva admite un solo pago aprobado y un solo pago abierto a la vez; después de `REJECTED` el cliente puede reportar un pago nuevo.

### 4.3 Ciclo de vida de la ejecución del servicio (RF-012b)

```mermaid
stateDiagram-v2
    [*] --> PENDING : asignar operario (RF-009)
    PENDING --> IN_PROGRESS : iniciar servicio (RF-012b)
    IN_PROGRESS --> PAUSED : pausar
    PAUSED --> IN_PROGRESS : reanudar
    IN_PROGRESS --> COMPLETED : finalizar servicio (RF-012b)
    IN_PROGRESS --> WITH_ISSUE : registrar incidente
    COMPLETED --> [*]
    WITH_ISSUE --> [*]
```

*Fuente:* `operations-service`. `COMPLETED` habilita la calificación del cliente (RF-012).

### 4.4 Ciclo de vida de una promoción (RF-024)

```mermaid
stateDiagram-v2
    [*] --> ACTIVA : crear (código, vigencia, % descuento, puntos requeridos)
    ACTIVA --> INACTIVA : desactivar (admin)
    INACTIVA --> ACTIVA : reactivar (admin)
    ACTIVA --> VENCIDA : fecha actual > fecha de fin
    INACTIVA --> VENCIDA : fecha actual > fecha de fin
    VENCIDA --> [*]
    ACTIVA --> [*] : eliminar
    INACTIVA --> [*] : eliminar
```

*Fuente:* `payment-service`, `Promotion.IsAvailableOn` (activa y dentro de vigencia). Una promoción `INACTIVA` o `VENCIDA` no se puede canjear (RF-024, RN-PROMO-01).

---

## 5. Inventario de Pantallas (mockup)

Pantalla por pantalla y por rol, incluyendo los modales de crear/editar de cada módulo. Todas las capturas están en `assets/`, en esta misma carpeta.

### 5.1 Pantallas comunes (sin sesión)

| Pantalla | Evidencia |
|---|---|
| Inicio de sesión | ![Login](../assets/01_login.png) |
| Registro | ![Registro](../assets/02_registro.png) |
| Recuperar contraseña | ![Recuperar](../assets/03_recuperar_contrasena.png) |

### 5.2 Rol Administrador

| Pantalla | Evidencia |
|---|---|
| Dashboard | ![Dashboard admin](../assets/04_admin_dashboard.png) |
| Gestión → Usuarios | ![Usuarios](../assets/05_admin_usuarios.png) |
| Modal: Crear usuario | ![Modal crear usuario](../assets/29_modal_crear_usuario.png) |
| Gestión → Roles | ![Roles](../assets/06_admin_roles.png) |
| Modal: Editar permisos del rol | ![Modal editar permisos](../assets/30_modal_editar_permisos.png) |
| Gestión → Servicios (catálogo) | ![Catálogo](../assets/07_admin_catalogo.png) |
| Modal: Agregar servicio | ![Modal agregar servicio](../assets/31_modal_crear_servicio.png) |
| Gestión → Promociones | ![Promociones](../assets/08_admin_promociones.png) |
| Modal: Crear promoción | ![Modal crear promoción](../assets/32_modal_crear_promocion.png) |
| Horarios y bahías | ![Horarios y bahías](../assets/09_admin_horarios_bahias.png) |
| Modal: Agregar excepción de horario | ![Modal agregar excepción](../assets/33_modal_agregar_excepcion.png) |
| Operarios | ![Operarios](../assets/10_admin_operarios.png) |
| Modal: Nuevo operario | ![Modal nuevo operario](../assets/34_modal_nuevo_operario.png) |
| Modal: Asignar turno | ![Modal asignar turno](../assets/42_modal_asignar_turno.png) |
| Reservas | ![Reservas](../assets/11_admin_reservas.png) |
| Modal: Asignar operario a una reserva | ![Modal asignar operario](../assets/35_modal_asignar_operario.png) |
| Pagos | ![Pagos](../assets/12_admin_pagos.png) |
| Modal: Registrar pago manual | ![Modal registrar pago](../assets/36_modal_registrar_pago.png) |
| Reportes | ![Reportes](../assets/13_admin_reportes.png) |
| Configuración → Cuentas de pago | ![Cuentas de pago](../assets/14_admin_cuentas_pago.png) |
| Modal: Agregar cuenta de pago | ![Modal cuenta de pago](../assets/37_modal_cuenta_pago.png) |
| Notificaciones | ![Notificaciones admin](../assets/15_admin_notificaciones.png) |
| Perfil | ![Perfil admin](../assets/16_admin_perfil.png) |

### 5.3 Rol Cliente

| Pantalla | Evidencia |
|---|---|
| Dashboard | ![Dashboard cliente](../assets/17_client_dashboard.png) |
| Modal: Ver detalle del próximo servicio | ![Modal detalle reserva](../assets/39_modal_detalle_reserva_cliente.png) |
| Mis vehículos | ![Vehículos](../assets/18_client_vehiculos.png) |
| Modal: Registrar vehículo | ![Modal registrar vehículo](../assets/38_modal_registrar_vehiculo.png) |
| Reservar lavado | ![Reservar](../assets/19_client_reservar.png) |
| Historial de reservas | ![Historial](../assets/20_client_historial.png) |
| Pagar servicio | ![Pago](../assets/21_client_pago.png) |
| Modal: Confirmar cancelación de reserva | ![Modal cancelar reserva](../assets/41_modal_cancelar_reserva.png) |
| Notificaciones | ![Notificaciones cliente](../assets/22_client_notificaciones.png) |
| Configuración (tema e idioma) | ![Configuración](../assets/23_client_configuracion.png) |

### 5.4 Rol Operario

| Pantalla | Evidencia |
|---|---|
| Panel principal | ![Panel operario](../assets/24_operario_home.png) |
| Servicios asignados | ![Servicios asignados](../assets/25_operario_servicios_asignados.png) |
| Mi agenda (disponibilidad) | ![Mi agenda](../assets/26_operario_horario.png) |
| Historial de servicios | ![Historial operario](../assets/27_operario_historial.png) |
| Calificaciones recibidas | ![Calificaciones](../assets/28_operario_calificaciones.png) |

---

## Correlación con el Informe de Especificación de Requisitos

| Vista dinámica de este documento | Requisitos que ilustra |
|---|---|
| §2.1 Registro y bienvenida | RF-001, RF-018 |
| §2.2 Reservar un lavado | RF-005, RF-006 |
| §2.3 Recordatorio de reserva | RF-018 |
| §2.4 Asignación y ejecución | RF-008, RF-009, RF-011, RF-012, RF-012b |
| §2.5 Pago por comprobante | RF-013, RF-013b, RF-014, RF-016 |
| §2.6 Canje de cupón y puntos | RF-024, RF-025, RF-026 |
| §2.7 Roles y permisos | RF-029 |
| §3.1 a §3.6 Actividades | Todo el módulo de autenticación, reservas, operación, pagos y promociones |
| §4.1 a §4.4 Estados | RF-006, RF-007, RF-012b, RF-013b, RF-014, RF-024 |
