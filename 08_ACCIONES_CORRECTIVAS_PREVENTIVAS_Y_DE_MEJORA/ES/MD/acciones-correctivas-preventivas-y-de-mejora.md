<!-- running-head: ACCIONES CORRECTIVAS, PREVENTIVAS Y DE MEJORA: SISTEMA DE LAVADO VEHICULAR -->

# Documentación de Acciones Correctivas, Preventivas y de Mejoramiento del Software

Sistema de Gestión de Lavado Vehicular (Vehicle Washing)

Procedimiento de Gestión, Registro de Acciones, Análisis de Causa Raíz, Seguimiento y Lecciones Aprendidas

Brayan Estiven Patiño Cabrera (líder de proyecto), Juan Camilo Guilombo Osorio (líder de frontend) y Merari Urbano (líder de backend)

Tecnólogo en Análisis y Desarrollo de Software (ADSO), Servicio Nacional de Aprendizaje (SENA), Centro de Formación: Industria

Ficha 3145556

Instructora: Karol Daniela Correa

9 de octubre de 2026

Tipo de documento: Registro de acciones correctivas, preventivas y de mejoramiento (equipo de desarrollo e instructora) · Versión 1.0

## Control de Versiones

La Tabla 1 registra el historial de cambios de este documento. El registro de acciones (secciones 9 a 12) es un documento vivo: cada vez que se abre, se actualiza o se cierra una acción, se modifica la fila de la acción y, al menos una vez por sprint, se agrega una fila a esta tabla.

**Tabla 1**

*Historial de Versiones del Documento de Acciones*

| Versión | Fecha | Descripción del cambio | Responsable |
|---|---|---|---|
| 1.0 | 2026-10-09 | Creación del documento (en español y en inglés). Se define el procedimiento de gestión y se registran 23 acciones correctivas cerradas, 13 acciones correctivas abiertas, 14 acciones preventivas y 13 acciones de mejoramiento, verificadas contra el código de los once repositorios (rama *develop* al 9 de octubre de 2026), el historial de Git, el registro de riesgos y el backlog técnico del proyecto. | Equipo de desarrollo |

*Nota.* Las fechas se escriben en formato ISO 8601 (año-mes-día). Elaborado por el equipo de desarrollo.

## Tabla de Contenido

<!-- toc -->

- [Control de Versiones](#control-de-versiones)
- [4. Introducción](#4-introducción)
  - [4.1 Marco de Referencia](#41-marco-de-referencia)
  - [4.2 Fuentes de Este Documento](#42-fuentes-de-este-documento)
- [5. Objetivo](#5-objetivo)
  - [5.1 Objetivo General](#51-objetivo-general)
  - [5.2 Objetivos Específicos](#52-objetivos-específicos)
- [6. Alcance](#6-alcance)
- [7. Definiciones y Clasificación](#7-definiciones-y-clasificación)
  - [7.1 Tipos de Acción](#71-tipos-de-acción)
  - [7.2 Severidad y Prioridad](#72-severidad-y-prioridad)
  - [7.3 Estados de una Acción](#73-estados-de-una-acción)
- [8. Procedimiento de Gestión de Acciones](#8-procedimiento-de-gestión-de-acciones)
  - [8.1 Fuentes de Identificación](#81-fuentes-de-identificación)
  - [8.2 Etapas del Procedimiento](#82-etapas-del-procedimiento)
  - [8.3 Análisis de Causa Raíz](#83-análisis-de-causa-raíz)
  - [8.4 Verificación de la Eficacia](#84-verificación-de-la-eficacia)
  - [8.5 Roles](#85-roles)
- [9. Registro de Acciones Correctivas Cerradas](#9-registro-de-acciones-correctivas-cerradas)
- [10. Registro de Acciones Correctivas Abiertas](#10-registro-de-acciones-correctivas-abiertas)
- [11. Registro de Acciones Preventivas](#11-registro-de-acciones-preventivas)
- [12. Registro de Acciones de Mejoramiento](#12-registro-de-acciones-de-mejoramiento)
- [13. Indicadores de Seguimiento](#13-indicadores-de-seguimiento)
- [14. Lecciones Aprendidas](#14-lecciones-aprendidas)
- [15. Glosario](#15-glosario)
- [Referencias](#referencias)
- [16. Anexos](#16-anexos)
  - [Anexo A. Formato de Registro de una Acción](#anexo-a-formato-de-registro-de-una-acción)
  - [Anexo B. Ejemplo de Análisis de Causa Raíz](#anexo-b-ejemplo-de-análisis-de-causa-raíz)
  - [Anexo C. Trazabilidad Entre Acciones, Riesgos y Deuda Técnica](#anexo-c-trazabilidad-entre-acciones-riesgos-y-deuda-técnica)

<!-- /toc -->

## 4. Introducción

El Sistema de Gestión de Lavado Vehicular (Vehicle Washing), llamado internamente *LavaRapido*, es una plataforma de reservas, asignación de operarios, ejecución y calificación de servicios, verificación de pagos por código QR y fidelización por puntos para un lavadero. Está formado por un gateway, seis microservicios (cinco en Java 21 con Spring Boot 4 y uno en .NET 8), una base de datos SQL Server 2022, RabbitMQ y dos clientes, web (Angular 21) y móvil (React Native con Expo) (Equipo de Desarrollo Vehicle Washing, 2026a).

Durante su construcción, sus revisiones con la instructora y la elaboración de sus manuales se han detectado defectos, riesgos y oportunidades de mejora. Este documento establece **cómo** se gestionan (identificación, registro, análisis de causa raíz, planificación, ejecución, verificación y cierre) y **registra** las acciones tomadas y pendientes, de modo que cualquier integrante del equipo, la instructora o un futuro equipo de mantenimiento sepan qué se corrigió, por qué, con qué evidencia y qué queda por hacer.

### 4.1 Marco de Referencia

- **ISO/IEC/IEEE 12207:2017.** El proceso de Mantenimiento (6.4.13) incluye corregir defectos, prevenir fallas y mejorar el software en operación, y el proceso de Aseguramiento de la Calidad (6.3.8) exige tratar los incidentes y los problemas detectados y verificar que las acciones sean eficaces (International Organization for Standardization [ISO] et al., 2017).
- **ISO/IEC/IEEE 14764:2022.** Desarrolla el proceso de mantenimiento de la ISO/IEC/IEEE 12207 y define los tipos de mantenimiento; este documento usa los tipos correctivo (corregir defectos descubiertos), preventivo (corregir defectos latentes antes de que se manifiesten), adaptativo (ajustar el software a cambios del entorno) y perfectivo (mejorar el software) (ISO et al., 2022).
- **ISO 9001:2015.** La cláusula 10.2 exige reaccionar ante una no conformidad, determinar sus causas, implementar la acción necesaria, revisar su eficacia y conservar información documentada; la cláusula 10.3 exige la mejora continua. La norma reemplazó la "acción preventiva" como requisito separado por el pensamiento basado en riesgos (cláusula 6.1), por lo que en este documento las acciones preventivas nacen del registro de riesgos (ISO, 2015).
- **Ciclo PHVA.** Cada acción recorre el ciclo planear, hacer, verificar y actuar, que es la base de la mejora continua de la ISO 9001.

### 4.2 Fuentes de Este Documento

Las acciones se verificaron contra el código de los once repositorios (rama *develop* al 9 de octubre de 2026) y su historial de Git, y contra el registro de riesgos, el backlog técnico, la gestión de incidentes, la estrategia de pruebas y los registros de decisiones de arquitectura (ADR) del proyecto (Equipo de Desarrollo Vehicle Washing, 2026a). También se incluyen los hallazgos de la revisión de los manuales del 7 y del 9 de octubre de 2026 (anexo B del Manual Técnico y anexos de los demás manuales).

## 5. Objetivo

### 5.1 Objetivo General

Documentar el procedimiento y el registro de las acciones correctivas, preventivas y de mejoramiento del Sistema de Gestión de Lavado Vehicular, para asegurar que cada defecto, riesgo u oportunidad de mejora se trate de forma trazable, verificable y con aprendizaje para el equipo.

### 5.2 Objetivos Específicos

- Definir los tipos de acción, su clasificación por severidad y prioridad y su ciclo de estados.
- Establecer un procedimiento único para identificar, registrar, analizar, ejecutar, verificar y cerrar acciones.
- Registrar las acciones correctivas ya ejecutadas con su causa raíz y su evidencia.
- Registrar las acciones correctivas, preventivas y de mejoramiento pendientes con su responsable, prioridad y criterio de cierre.
- Definir indicadores para medir la eficacia del procedimiento y consolidar las lecciones aprendidas.

## 6. Alcance

**Cubre:** los seis servicios de backend, el gateway, la base de datos, la infraestructura de Docker, la aplicación web, la aplicación móvil y la documentación del proyecto (manuales, ADR, contratos y modelos de datos), desde la construcción hasta la operación posterior a la implementación.

**No cubre:** la gestión de los requisitos nuevos del producto (historias de usuario del backlog de producto), salvo cuando una necesidad de mejora del software ya construido se registra como acción de mejoramiento; tampoco cubre la gestión académica del proyecto (notas, entregas del programa).

## 7. Definiciones y Clasificación

### 7.1 Tipos de Acción

**Tabla 2**

*Tipos de Acción y su Relación con los Tipos de Mantenimiento*

| Tipo | Definición | Disparador | Tipo de mantenimiento (ISO/IEC/IEEE 14764) | Prefijo |
|---|---|---|---|---|
| Acción correctiva | Elimina la causa de una no conformidad **ya ocurrida** (defecto, incumplimiento de un requisito, de un ADR o de la documentación) para que no se repita. | Incidente, prueba fallida, revisión, observación de la instructora o de la aceptación. | Correctivo | AC (cerradas) y ACO (abiertas) |
| Acción preventiva | Elimina la causa de una no conformidad **potencial** antes de que ocurra. | Riesgo del registro de riesgos, deuda técnica, análisis de tendencias. | Preventivo y adaptativo | AP |
| Acción de mejoramiento | Aumenta el valor, la calidad o la eficiencia del software sin que exista una falla. | Retrospectiva, sugerencia de usuarios, evolución recomendada de la arquitectura. | Perfectivo y adaptativo | AM |

*Nota.* Elaborado por los autores a partir de ISO (2015) e ISO et al. (2022).

Una **corrección** (por ejemplo, reiniciar un servicio o editar un dato) no es una acción correctiva: resuelve el síntoma, pero no la causa. En la gestión de incidentes del proyecto la corrección corresponde al paso "mitigar"; la acción correctiva es el cambio de código, configuración o proceso que impide que el incidente se repita.

### 7.2 Severidad y Prioridad

La severidad usa la misma escala de la gestión de incidentes del proyecto (Tabla 3). La prioridad combina la severidad con la probabilidad de ocurrencia y el esfuerzo, y se expresa como Alta, Media o Baja, igual que en el backlog técnico.

**Tabla 3**

*Escala de Severidad*

| Nivel | Definición | Ejemplo | Plazo de respuesta |
|---|---|---|---|
| P0 | Nada funciona. | SQL Server caído; ningún servicio arranca; imposible iniciar sesión. | Inmediato. |
| P1 | Un flujo principal está roto. | No se puede reservar, asignar, iniciar un servicio, reportar o aprobar un pago. | El mismo día. |
| P2 | Una función secundaria falla y existe alternativa. | Los correos no llegan, pero la bandeja interna sí funciona. | Dentro del sprint. |
| P3 | Cosmético o documental. | Texto sin traducir, ícono incorrecto, manual desactualizado. | Backlog. |

*Nota.* Tomado de la gestión de incidentes del proyecto (Equipo de Desarrollo Vehicle Washing, 2026a).

### 7.3 Estados de una Acción

Cada acción pasa por los estados **Abierta** (registrada), **En análisis** (se busca la causa raíz), **Planificada** (tiene responsable, solución y fecha), **En ejecución** (rama y pull request en curso), **En verificación** (desplegada; se comprueba su eficacia) y **Cerrada** (eficaz y con evidencia). Una acción cuya verificación falla vuelve a *En análisis*. Una acción que el equipo decide no ejecutar se marca **Aceptada como riesgo**, con la justificación y la aprobación del líder de proyecto.

## 8. Procedimiento de Gestión de Acciones

### 8.1 Fuentes de Identificación

- Incidentes de la gestión de incidentes del proyecto y sus *post-mortems* (P0 y P1).
- Pruebas automáticas fallidas (*./mvnw verify*, *dotnet test*, *ng build*) y pruebas manuales de punta a punta antes de cada revisión.
- Revisiones de código (pull requests) y revisiones de la instructora.
- Pruebas de humo y de aceptación del Procedimiento de Implementación.
- Contraste entre el código, los ADR y los manuales (anexos de discrepancias).
- Registro de riesgos y backlog técnico (fuente de acciones preventivas).
- Retrospectivas de cada sprint y comentarios de las personas usuarias (fuente de acciones de mejoramiento).

### 8.2 Etapas del Procedimiento

**Tabla 4**

*Etapas del Procedimiento de Gestión de Acciones*

| Etapa (PHVA) | Actividad | Responsable | Salida |
|---|---|---|---|
| 1. Identificar (Planear) | Detectar la no conformidad, el riesgo o la oportunidad y comunicarla en el chat del equipo. | Quien la detecta | Aviso con descripción y evidencia. |
| 2. Registrar (Planear) | Crear la fila en el registro correspondiente (secciones 9 a 12) con el formato del Anexo A; asignar ID, tipo, severidad y responsable. | Líder del área afectada | Acción en estado Abierta. |
| 3. Contener (Hacer) | Solo en correctivas P0 y P1: aplicar la corrección inmediata (reiniciar, ajustar *.env*, levantar el contenedor faltante). | Responsable del servicio | Flujo restablecido. |
| 4. Analizar la causa (Planear) | Aplicar los cinco porqués o el diagrama de causa y efecto (sección 8.3). | Responsable del servicio | Causa raíz documentada. |
| 5. Planificar (Planear) | Definir la solución, el criterio de cierre, el esfuerzo y la fecha; si cambia una decisión técnica, crear o modificar un ADR. | Responsable con el líder de proyecto | Acción en estado Planificada. |
| 6. Ejecutar (Hacer) | Rama *fix/\** o *feat/\**, cambio con pruebas que reproduzcan el defecto, pull request revisado por otra persona y documentación actualizada en el mismo pull request (definición de terminado). | Responsable | Pull request integrado en *develop*. |
| 7. Verificar la eficacia (Verificar) | Comprobar el criterio de cierre en el entorno implementado y que el problema no reaparece (sección 8.4). | Persona distinta del ejecutor | Evidencia de verificación. |
| 8. Cerrar y aprender (Actuar) | Marcar Cerrada, registrar la lección aprendida (sección 14) y actualizar el registro de riesgos y el backlog técnico. | Líder de proyecto | Acción en estado Cerrada. |

*Nota.* Elaborado por los autores a partir de la cláusula 10.2 de ISO (2015) y de la definición de terminado del proyecto.

### 8.3 Análisis de Causa Raíz

Para las acciones correctivas de severidad P0, P1 y P2 es obligatorio documentar la causa raíz. Se usan dos técnicas:

- **Cinco porqués:** se pregunta "¿por qué ocurrió?" sobre cada respuesta hasta llegar a una causa sobre la que el equipo puede actuar (proceso, diseño, configuración o conocimiento). El Anexo B contiene un ejemplo real del proyecto.
- **Diagrama de causa y efecto (Ishikawa):** cuando hay varias causas posibles, se clasifican en las categorías *código*, *configuración*, *datos*, *infraestructura*, *proceso* y *personas* antes de elegir la causa principal.

La causa raíz **nunca** se registra como "error humano": si una persona se equivocó, la pregunta es qué en el proceso, la herramienta o la documentación permitió el error (enfoque sin culpables de los *post-mortems* del proyecto).

### 8.4 Verificación de la Eficacia

Una acción solo se cierra cuando se cumple su criterio de cierre y existe evidencia verificable: commit o pull request, prueba automática que reproduce el defecto y ahora pasa, resultado de una prueba manual, consulta a la base de datos o captura. Para las correctivas P0 y P1 se exige además que el problema no reaparezca en la siguiente revisión o implementación. La verificación la hace una persona distinta de quien ejecutó la acción.

### 8.5 Roles

**Tabla 5**

*Roles en la Gestión de Acciones*

| Rol | Persona | Responsabilidad |
|---|---|---|
| Líder de proyecto | Brayan Estiven Patiño Cabrera | Aprueba prioridades, acepta riesgos, verifica el cierre y mantiene este documento. |
| Líder de backend | Merari Urbano | Responsable de las acciones de servicios, base de datos e infraestructura. |
| Líder de frontend | Juan Camilo Guilombo Osorio | Responsable de las acciones de las aplicaciones web y móvil. |
| Autor de cada pull request | Cualquier integrante | Actualiza la documentación afectada en el mismo pull request. |
| Instructora | Karol Daniela Correa | Fuente de observaciones; revisa el documento en las entregas. |

*Nota.* Elaborado por los autores. Cada servicio tiene además un dueño definido en el catálogo de servicios del proyecto.

## 9. Registro de Acciones Correctivas Cerradas

La Tabla 6 registra las no conformidades ya corregidas, con su causa raíz y la evidencia de cierre. La columna "Origen" remite al riesgo cerrado (C-), a la deuda técnica (TD-) o al ADR correspondiente.

**Tabla 6**

*Acciones Correctivas Cerradas*

| ID | No conformidad | Sev. | Causa raíz | Acción ejecutada | Evidencia de cierre | Origen | Cierre |
|---|---|---|---|---|---|---|---|
| AC-01 | Las horas de las reservas aparecían corridas cinco horas. | P1 | La JVM convertía las fechas con la zona del equipo y no con la del negocio. | La JVM de booking-service corre en UTC; las fechas se guardan en UTC y se convierten solo en los bordes con *BOOKING_ZONE=America/Bogota*. | Pruebas de *AvailabilityPolicyTest* y reservas correctas en la prueba de punta a punta. | C-001 | 2026-10-04 |
| AC-02 | Los servicios fallaban al arrancar después de *docker compose up*. | P0 | Los servicios intentaban conectarse antes de que SQL Server estuviera sano. | Chequeos de salud en *sqlserver* y *rabbitmq* y dependencias *service_healthy* y *service_completed_successfully* en el archivo de Compose. | *docker-compose.yml* con *depends_on* condicionados. | C-002 | 2026-10-04 |
| AC-03 | Existían dos implementaciones distintas del servicio de reservas. | P1 | Se empezó a programar sin un modelo de datos acordado. | Se reconstruyó booking-service a partir del modelo SQL acordado; regla del equipo: acordar el modelo antes de programar un servicio. | Un solo repositorio *lavarapido-booking-service* alineado con *06-data/models.md*. | C-003 | 2026-10-04 |
| AC-04 | Con *--profile app* todas las rutas de pagos fallaban. | P1 | payment-service no tenía Dockerfile ni servicio en Compose, y el contenedor del gateway no recibía *ROUTE_PAYMENT_URL*. | Dockerfile multietapa de .NET 8, servicio *payment-service* en Compose y *ROUTE_PAYMENT_URL* en el gateway. | Commit de *lavarapido-infra* del 2026-10-08 ("wire payment-service to booking-service and rabbitmq"). | TD-014 | 2026-10-08 |
| AC-05 | Faltaba *BOOKING_SERVICE_URL* para payment-service en Compose; la acreditación de puntos fallaba en contenedores. | P1 | La variable se omitió al crear el servicio (vacío previo descubierto en ADR-015). | Variable agregada con *http://booking-service:3003/api/v1*. | *docker-compose.yml* vigente. | ADR-015 | 2026-10-08 |
| AC-06 | El cliente no recibía aviso cuando su pago se aprobaba, rechazaba o reembolsaba. | P2 | payment-service levantaba eventos de dominio, pero no tenía publicador de RabbitMQ. | Publicador con *RabbitMQ.Client* y eventos *payment.confirmed*, *payment.rejected* y *payment.refunded*, con correo al cliente. | ADR-011 sección 9; tipos *PAYMENT_\** en notification-service (migración 028). | TD-015 | 2026-10-08 |
| AC-07 | Una misma referencia de transacción podía pagar dos reservas. | P1 | No se validaba la unicidad de la referencia al reportar un pago (control de ADR-008 y RF-016). | Validación en payment-service con el código de error *TRANSACTION_REFERENCE_REUSED*. | *ErrorCodes.cs* de payment-service. | TD-016 | 2026-10-08 |
| AC-08 | payment-service solo probaba su dominio; las reglas de rol y de conflicto (409) no estaban protegidas. | P2 | Las pruebas de aplicación y de API se aplazaron al construir el servicio. | Proyectos *PaymentService.Application.UnitTests* e *Infrastructure.IntegrationTests*. | Carpeta *tests/* con pruebas de comandos, consultas, promociones y persistencia. | TD-018 | 2026-10-08 |
| AC-09 | Los puntos ganados por una reserva no se revertían al reembolsar su pago, y dos movimientos simultáneos podían dejar un saldo incorrecto. | P1 | El ledger de puntos no tenía movimiento de reversión ni control de concurrencia. | Tipo de movimiento *REVERSED* y columna *sequence_no* única por cliente (migración *pay-020*); el segundo movimiento concurrente responde 409. | Migración *020-loyalty-reversal-and-sequence.sql*. | ADR-015 | 2026-10-08 |
| AC-10 | La aprobación de pagos comparaba el total de la reserva consigo mismo y aceptaba imágenes no válidas. | P1 | El monto declarado por el cliente no se enviaba ni se comparaba. | Envío del monto pagado, comparación con el monto adeudado en la ventana de revisión y validación de imágenes PNG o JPG. | Commits de payment-service y de la web del 2026-10-08. | Manuales v3.0 | 2026-10-08 |
| AC-11 | Existía un catálogo de "roles personalizados" sin efecto en la autorización, que contradecía ADR-010. | P2 | Se construyó una función sin contrastarla con las decisiones registradas. | Se eliminó *security.custom_role* (migración 026); los tres roles quedan fijos y se edita la matriz de permisos de *security.role_permission*. | ADR-015 sección 2; endpoint */api/v1/admin/roles-permissions*. | ADR-015 | 2026-10-08 |
| AC-12 | Se había construido una asignación fija de operario por bahía, contraria a ADR-010. | P2 | Igual que AC-11. | Se revirtió la columna *service_bay.operator_id* (migración 024); la bahía se elige por reserva y el operario por ejecución. | ADR-015 sección 1. | ADR-015 | 2026-10-08 |
| AC-13 | Las promociones mostraban un precio de paquete que nunca se aplicaba al cobro. | P2 | El modelo de promociones se usaba solo para presentación. | Cupones con descuento porcentual real, canjeables con puntos (*POST /api/v1/loyalty/redeem*), y formulario sin precio, duración ni estado. | ADR-015 secciones 3 y 5. | ADR-015 | 2026-10-09 |
| AC-14 | Al editar un servicio, sus puntos de fidelización volvían a 0. | P2 | booking-service enlaza el campo a un *int* primitivo y los clientes omitían el campo. | La web y la app envían siempre *loyaltyPoints*; la app conserva el precio de cada tipo de vehículo al editar. | ADR-015 sección 5; commits de la app móvil del 2026-10-09. | ADR-015 | 2026-10-09 |
| AC-15 | Se ofrecía "Pagar" en reservas ya pagadas o en revisión. | P2 | Cada pantalla repetía la regla de pago y no consultaba a payment-service. | Endpoint *GET /api/v1/payments/me/bookings* con el indicador *payable*; la web y la app solo muestran el botón con ese indicador. | ADR-015 sección 5. | ADR-015 | 2026-10-09 |
| AC-16 | Los interruptores de notificaciones se guardaban solo en el navegador o el teléfono y no tenían efecto. | P2 | No existían columnas para esas preferencias en la cuenta. | Columnas en *security.user_preference* (migración 030), actualización parcial de preferencias y aplicación de los interruptores en notification-service. | ADR-011 sección 12. | ADR-011 | 2026-10-09 |
| AC-17 | El tema y el idioma se guardaban por navegador y una segunda cuenta en el mismo equipo los heredaba. | P2 | Las preferencias se leían de *localStorage* sin consultar la cuenta. | Carga después del inicio de sesión y guardado con *GET/PUT /api/v1/users/me/preferences*; paletas aceptadas por security-service (migración 020). | *core/services/preferences.ts* de la web. | TD-002 | 2026-10-09 |
| AC-18 | El administrador podía enviar a mano cualquier tipo de notificación (por ejemplo, un falso "pago aprobado"). | P1 | El endpoint manual no restringía el tipo. | Solo se aceptan *SYSTEM_MESSAGE* e *INSPECTION_REPORT*; cualquier otro responde 400 *NOTIFICATION_TYPE_NOT_ALLOWED*. | ADR-011 sección 11. | Revisión de seguridad | 2026-10-09 |
| AC-19 | Al actualizar los permisos de un rol se aceptaban identificadores nulos o inexistentes. | P2 | Faltaba validación de entrada en el caso de uso. | Rechazo con 400 *UNKNOWN_PERMISSION* y mensaje traducido en la web. | Commit de security-service del 2026-10-08. | ADR-015 | 2026-10-08 |
| AC-20 | El informe de inspección se compartía por WhatsApp, fuera de los canales del sistema. | P3 | Decisión de producto anterior. | Botón "Notificar al cliente" que envía el resumen por notificación y correo (*INSPECTION_REPORT*); se retiró WhatsApp de los datos del negocio y del centro de ayuda. | ADR-011 sección 11; commits de la web del 2026-10-09. | ADR-011 | 2026-10-09 |
| AC-21 | La app abierta en el navegador con Expo (puerto 8081) era rechazada por CORS. | P2 | El origen 8081 no estaba en los valores por defecto. | *CORS_ALLOWED_ORIGINS* por defecto incluye *http://localhost:8081* en todos los servicios. | Commits de *lavarapido-infra* y del gateway. | — | 2026-10-09 |
| AC-22 | La ruta antigua de tareas del operario mostraba una página vacía. | P3 | Ruta sin componente después de una reorganización. | Redirección a "Servicios asignados" y eliminación de la página vacía. | Commit de la web del 2026-10-09. | — | 2026-10-09 |
| AC-23 | Los manuales v3.0 quedaron desactualizados por los cambios del 8 y 9 de octubre (puntos, cupones, reembolsos, roles, preferencias, pagos en Docker), solo existían en inglés y el Manual de Instalación indicaba clonar el repositorio de operaciones con un nombre que rompe la construcción. | P3 | La documentación no se actualizó en los mismos pull requests (riesgo R-010). | Manuales actualizados a la versión 3.1 en español y en inglés, y creación del Procedimiento de Implementación y de este documento. | Control de versiones de cada manual (2026-10-09). | R-010 | 2026-10-09 |

*Nota.* Elaborado por los autores a partir del historial de Git de los repositorios, el registro de riesgos y los ADR del proyecto (Equipo de Desarrollo Vehicle Washing, 2026a).

## 10. Registro de Acciones Correctivas Abiertas

**Tabla 7**

*Acciones Correctivas Abiertas*

| ID | No conformidad | Sev. | Causa raíz | Acción propuesta | Responsable | Prioridad | Criterio de cierre |
|---|---|---|---|---|---|---|---|
| ACO-01 | La suite de pruebas web no compila. | P2 | Seis archivos *.spec.ts* de andamiaje apuntan a clases que ya no existen (*features/\*/viewmodels/\*.spec.ts*, *settings-panel.spec.ts*, *stepper.spec.ts*). | Corregir o eliminar esos archivos y agregar pruebas del formulario de reserva y de los *stores*. | Líder de frontend | Alta | *npx ng test --watch=false* pasa. (TD-001) |
| ACO-02 | No existe límite de intentos de inicio de sesión. | P1 | El requisito RF-004b no se implementó en security-service. | Bloqueo temporal o retardo progresivo tras cinco intentos fallidos, con prueba de seguridad. | Líder de backend | Alta | Prueba que demuestra el bloqueo y manuales actualizados. (TD-003) |
| ACO-03 | La aceptación de los Términos y de la Política de Tratamiento de Datos no se guarda en el servidor. | P1 | La tabla *security.user_consent* quedó pendiente (ADR-010). | Registrar la versión del documento aceptado, la fecha y la cuenta, como evidencia exigida por la Ley 1581 de 2012 (Congreso de la República de Colombia, 2012). | Líder de backend | Alta | Consentimiento consultable por cuenta. |
| ACO-04 | La tabla *audit.audit_log* existe pero nadie escribe en ella. | P2 | No se crearon los disparadores ni se fija *SESSION_CONTEXT(N'user_id')*. | Disparadores de auditoría en las tablas sensibles y contexto de sesión en cada servicio, o retirar la tabla del diseño mediante un ADR. | Líder de backend | Media | Cambios de precios, cuentas de pago y roles visibles en la auditoría. |
| ACO-05 | El endpoint de salud de payment-service responde *UP* con la base caída y el servicio no tiene filtro de *X-Correlation-Id*. | P2 | El endpoint devuelve un valor fijo. | Chequeo de salud de EF Core contra SQL Server y filtro de correlación. | Líder de backend | Media | */actuator/health* responde *DOWN* sin base de datos. (TD-017) |
| ACO-06 | Los textos de reembolso (*Reembolsar*, confirmación y resultado) están fijos en español y no cambian con el idioma. | P3 | Se dejaron en *core/constants/payment-texts.ts* de forma temporal para no editar los archivos de idioma. | Pasar los textos a *ADMIN_PAYMENTS* y *PAYMENT_REVIEW_MODAL* en los cuatro idiomas y borrar el archivo temporal. | Líder de frontend | Media | Textos traducidos en inglés, francés y portugués. |
| ACO-07 | El botón "Reportar avance" del operario muestra "El cliente recibirá la actualización", pero no envía nada. | P3 | La función quedó solo con la confirmación visual. | Enviar una notificación real al cliente o retirar el botón y el mensaje. | Líder de frontend | Media | Notificación recibida o botón eliminado. |
| ACO-08 | La página de bienvenida anuncia un servicio de lavado "donde estés" y el historial del operario muestra medios de pago (tarjeta, PSE) que el sistema no admite. | P3 | Textos de maqueta que no se ajustaron al alcance real. | Ajustar los textos al servicio en el local y a los medios de pago reales. | Líder de frontend | Baja | Textos revisados en los cuatro idiomas. |
| ACO-09 | No existe ruta comodín: una dirección desconocida muestra una página vacía. | P3 | Falta la ruta *\*\** en *app.routes.ts*. | Página 404 con enlace al inicio de cada rol. | Líder de frontend | Baja | Una dirección inexistente muestra la página 404. (TD-009) |
| ACO-10 | El informe de inspección y sus fotos se guardan solo en el navegador; el enlace público no abre en otro equipo. | P2 | RF-027 no tiene todavía un agregado en el backend. | Persistir el informe en un servicio (o en booking-service) con almacenamiento de imágenes. | Líder de backend | Media | El cliente abre el enlace desde su teléfono. |
| ACO-11 | Los datos del negocio de Configuración se guardan solo en el navegador del administrador. | P3 | La extensión de *booking.establishment* espera la definición de sus campos (TD-013). | API de establecimiento para los datos de facturación y ayuda. | Líder de backend | Baja | Los cambios se ven desde otra cuenta. |
| ACO-12 | El README de *lavarapido-infra* y la sección 6 de la guía del equipo describen como pendientes servicios y pantallas que ya existen. | P3 | Documentos no actualizados al integrar operations-service y payment-service. | Actualizar ambos documentos. | Líder de proyecto | Baja | Documentos coherentes con el código. |
| ACO-13 | Las entidades editadas por administradores no usan bloqueo optimista: en ediciones concurrentes gana la última escritura. | P3 | La columna *row_version* existe, pero no se mapea con *@Version*. | Mapear *@Version* en booking, customer y security y responder 409 ante conflicto. | Líder de backend | Baja | Prueba de dos actualizaciones con la misma versión. (TD-008) |

*Nota.* Elaborado por los autores a partir del backlog técnico, del anexo B del Manual Técnico y de la verificación del código al 9 de octubre de 2026.

## 11. Registro de Acciones Preventivas

Las acciones preventivas atacan las causas de riesgos que todavía no se han materializado o que podrían repetirse.

**Tabla 8**

*Acciones Preventivas*

| ID | Riesgo o causa potencial | Acción preventiva | Responsable | Prioridad | Estado | Origen |
|---|---|---|---|---|---|---|
| AP-01 | Regresiones que llegan a *develop* sin detectarse. | Pipeline de Jenkins por repositorio (*./mvnw -B verify*, *dotnet test*, *ng build* y *ng test*) y regla de integrar solo con el pipeline en verde. | Líder de proyecto | Alta | Abierta | R-003, TD-006 |
| AP-02 | Pérdida de un evento entre el commit y la publicación. | Patrón Outbox en security, booking, operations y payment. | Líder de backend | Baja | Aceptada como riesgo hasta salir del alcance académico | R-005, TD-011 |
| AP-03 | Fuga de secretos (*.env*, contraseña de aplicación del correo, *JWT_SECRET*). | Mantener *.env* ignorado, revisar con *git check-ignore* antes de cada implementación y rotar los secretos cada trimestre o ante sospecha. | Todo el equipo | Alta | En ejecución (permanente) | R-004 |
| AP-04 | Pérdida de datos antes de una demostración o en operación. | Respaldo diario automatizado con verificación y prueba mensual de restauración (Manual de Administrador, sección 14). | Administrador de TI | Alta | Abierta | R-008 |
| AP-05 | La documentación vuelve a separarse del código. | Lista de revisión de pull requests que exige actualizar modelos, contratos OpenAPI, ADR y manuales afectados; revisión de los manuales antes de cada implementación. | Autor de cada pull request | Media | En ejecución (permanente) | R-010 |
| AP-06 | Implementar con *MESSAGING_ENABLED=false*, sin *INTERNAL_API_KEY* o con el perfil *dev*. | Lista de verificación del Anexo A del Procedimiento de Implementación. | Administrador de TI | Media | Cerrada (incluida en el procedimiento) | R-I02, R-I03 |
| AP-07 | Defectos de persistencia (bloqueos y disparadores) que solo se ven a mano. | Pruebas de persistencia con Testcontainers y SQL Server real en booking-service. | Líder de backend | Baja | Abierta | TD-010 |
| AP-08 | Uso de la cuenta *sa* por todos los servicios. | Un inicio de sesión por servicio con permisos solo sobre sus esquemas y una cuenta separada para las migraciones. | Líder de backend | Media | Abierta | Política de seguridad |
| AP-09 | Una acción de usuario no puede seguirse entre servicios. | Propagar *X-Correlation-Id* en todos los clientes REST y mensajes y generarlo en el gateway. | Líder de backend | Baja | Abierta | TD-007 |
| AP-10 | Falta de métricas para comprobar el tiempo de respuesta (RNF-001). | *micrometer-registry-prometheus* en los servicios Java y métricas equivalentes en .NET. | Líder de backend | Baja | Abierta | TD-012 |
| AP-11 | Ataques de fuerza bruta o abuso de la API si el sistema se expone. | Límite de solicitudes en el gateway, además de ACO-02. | Líder de backend | Media | Abierta | Política de seguridad |
| AP-12 | Componentes con vulnerabilidades conocidas. | Revisión trimestral con *./mvnw versions:display-dependency-updates*, *dotnet list package --vulnerable* y *npm audit*. | Líderes de backend y frontend | Media | En ejecución (permanente) | OWASP A06 |
| AP-13 | Confusión por la numeración propia de los changelogs de pagos, que repite los números globales. | Documentar la regla en la estrategia de migraciones y usar el prefijo *pay-* en los identificadores. | Líder de backend | Baja | Cerrada (documentada) | TD-019 |
| AP-14 | Funciones construidas que contradicen decisiones ya registradas (causa de AC-11 y AC-12). | Revisar los ADR vigentes y el mapa de navegación antes de iniciar una función, y consultar al equipo ante una contradicción. | Todo el equipo | Media | En ejecución (permanente) | Lección de ADR-015 |

*Nota.* Elaborado por los autores a partir del registro de riesgos, el backlog técnico y la política de seguridad del proyecto.

## 12. Registro de Acciones de Mejoramiento

**Tabla 9**

*Acciones de Mejoramiento*

| ID | Oportunidad de mejora | Beneficio esperado | Responsable | Prioridad | Estado | Origen |
|---|---|---|---|---|---|---|
| AM-01 | Asignación automática de operarios al confirmarse una reserva, reutilizando *AssignmentPolicy*. | El administrador deja de asignar cada reserva a mano (RF-008). | Líder de backend | Media | Abierta | TD-020, ADR-014 |
| AM-02 | Aplicar la matriz de permisos de *security.role_permission* en la autorización real de cada endpoint. | Control de acceso granular configurable desde el panel. | Líder de backend | Baja | Abierta (requiere ADR) | ADR-015 |
| AM-03 | Reprogramación de reservas por el cliente desde la web y la app (la API ya ofrece *PUT /api/v1/bookings/{id}*). | El cliente no tiene que cancelar y reservar de nuevo. | Líder de frontend | Media | Abierta | Manual de Usuario |
| AM-04 | Completar la aplicación móvil y construir una versión con EAS para las notificaciones push. | Avisos inmediatos en el teléfono. | Líder de frontend | Media | En ejecución | ADR-011 |
| AM-05 | Firma RS256 y tokens de actualización (*refresh tokens*). | Menor impacto de una fuga del secreto y sesiones más largas sin volver a iniciar sesión. | Líder de backend | Baja | Abierta | ADR-006 |
| AM-06 | Almacenar comprobantes, códigos QR y fotos fuera de la base de datos. | Base de datos más liviana y respaldos más rápidos. | Líder de backend | Baja | Abierta | Evolución recomendada |
| AM-07 | Separar en *promotion.promotion* los campos de presentación y los de descuento real. | Evita que el paquete mostrado y el descuento aplicado se contradigan. | Líder de backend | Baja | Abierta | ADR-015 |
| AM-08 | Publicar la web compilada detrás del gateway con HTTPS. | Entorno apto para producción, sin servidor de desarrollo. | Líder de frontend | Media | Abierta | Procedimiento de Implementación, R-I08 |
| AM-09 | Herramientas de cobertura (JaCoCo) y análisis estático (SonarQube). | Métricas objetivas de calidad del código. | Líder de proyecto | Baja | Abierta | Estrategia de pruebas |
| AM-10 | Prueba automática de punta a punta entre servicios (registro → reserva → notificación → pago). | Detección temprana de fallas de integración. | Líder de backend | Media | Abierta | Estrategia de pruebas |
| AM-11 | Reemplazar los marcadores de figuras de los manuales por capturas reales de la versión final. | Manuales completos según la guía del SENA. | Líder de frontend | Alta | Abierta | Anexo A de cada manual |
| AM-12 | Usar los estados de ejecución *PAUSED* y *WITH_ISSUE* en la interfaz del operario. | Registrar pausas y novedades del servicio. | Líder de frontend | Baja | Abierta | Modelo de datos |
| AM-13 | Exponer en el panel el envío de avisos generales (*SYSTEM_MESSAGE*) a grupos de usuarios. | Comunicación directa con clientes y operarios sin usar la API. | Líder de frontend | Baja | Abierta | Manual de Administrador |

*Nota.* Elaborado por los autores a partir de la evolución recomendada del Manual Técnico, de los ADR y de las limitaciones documentadas en los manuales.

## 13. Indicadores de Seguimiento

**Tabla 10**

*Indicadores de la Gestión de Acciones*

| Indicador | Fórmula | Meta | Valor al 2026-10-09 |
|---|---|---|---|
| Acciones correctivas cerradas | Correctivas cerradas / correctivas registradas × 100 | ≥ 70 % por entrega | 23 / 36 = 64 % |
| Correctivas P0 y P1 abiertas | Número de ACO con severidad P0 o P1 | 0 antes de una implementación | 2 (ACO-02 y ACO-03) |
| Cierre en plazo | Acciones cerradas dentro del plazo de su severidad / acciones cerradas × 100 | ≥ 90 % | Por medir desde la versión 1.0 |
| Reincidencia | Correctivas cerradas cuyo problema reaparece / correctivas cerradas × 100 | 0 % | 0 % |
| Defectos escapados | Defectos encontrados en aceptación u operación / defectos totales del periodo × 100 | Tendencia a la baja | Por medir desde la primera implementación |
| Pruebas automatizadas | Métodos de prueba del backend (*@Test*, *@ParameterizedTest*, *[Fact]*, *[Theory]*) | Creciente | Aproximadamente 400 (301 en Java y 98 en .NET) |

*Nota.* Elaborado por los autores. El conteo de pruebas corresponde a las anotaciones encontradas en los repositorios el 9 de octubre de 2026; las pruebas parametrizadas pueden ejecutar más casos.

El líder de proyecto revisa los indicadores en cada retrospectiva y antes de cada implementación. Dos correctivas P1 abiertas (ACO-02 y ACO-03) **impiden cumplir el criterio de entrada E6** del Procedimiento de Implementación para un entorno con personas usuarias reales; para una implementación de evaluación académica, el líder de proyecto puede aceptarlas como riesgo documentado.

## 14. Lecciones Aprendidas

**Tabla 11**

*Lecciones Aprendidas*

| N.° | Lección | Acciones relacionadas |
|---|---|---|
| L-01 | Guardar el tiempo en UTC y convertirlo solo en los bordes evita desplazamientos de hora. | AC-01 |
| L-02 | Un servicio no debe arrancar antes de que sus dependencias estén sanas; la orquestación lo debe garantizar. | AC-02 |
| L-03 | Acordar el modelo de datos antes de programar un servicio evita implementaciones duplicadas. | AC-03 |
| L-04 | Toda decisión ya registrada en un ADR debe revisarse antes de construir; una contradicción se consulta antes de programar. | AC-11, AC-12, AP-14 |
| L-05 | Una regla de negocio debe vivir en un solo servicio y las pantallas deben consultarla, no repetirla. | AC-15 |
| L-06 | Una preferencia que la persona usuaria cambia debe guardarse en su cuenta para tener efecto. | AC-16, AC-17 |
| L-07 | Un nuevo servicio no está terminado hasta que tiene contenedor, ruta en el gateway, variables en Compose y eventos publicados. | AC-04, AC-05, AC-06 |
| L-08 | Los endpoints administrativos también necesitan validación estricta de entrada y listas permitidas. | AC-18, AC-19 |
| L-09 | La documentación se actualiza en el mismo pull request que el código; de lo contrario, se desactualiza en días. | AC-23, AP-05 |
| L-10 | Un ledger contable necesita movimientos de reversión y control de concurrencia desde el primer día. | AC-09 |

*Nota.* Elaborado por los autores a partir del registro de riesgos cerrados y de las acciones de este documento.

## 15. Glosario

**Tabla 12**

*Glosario*

| Término | Definición |
|---|---|
| Acción correctiva | Acción que elimina la causa de una no conformidad ocurrida para evitar que se repita. |
| Acción de mejoramiento | Acción que aumenta el valor o la calidad del software sin que exista una falla. |
| Acción preventiva | Acción que elimina la causa de una no conformidad potencial. |
| ADR | Registro de decisión de arquitectura. |
| Causa raíz | Causa fundamental de un problema sobre la que se puede actuar para que no se repita. |
| Corrección | Acción inmediata que elimina el síntoma de una no conformidad sin atacar su causa. |
| Deuda técnica | Trabajo pendiente que hace que el software funcione, pero no como debería. |
| Eficacia | Grado en que una acción logra el resultado planificado. |
| Ledger | Registro contable de movimientos de puntos, cuyo saldo es el del último movimiento. |
| No conformidad | Incumplimiento de un requisito, de una decisión registrada o de lo documentado. |
| PHVA | Ciclo planear, hacer, verificar y actuar de la mejora continua. |
| Post-mortem | Análisis sin culpables de un incidente grave, con su causa y sus acciones. |

*Nota.* Elaborado por los autores a partir de ISO (2015), ISO et al. (2022) y la documentación del proyecto.

## Referencias

Congreso de la República de Colombia. (2012). *Ley Estatutaria 1581 de 2012, por la cual se dictan disposiciones generales para la protección de datos personales*. http://www.secretariasenado.gov.co/senado/basedoc/ley_1581_2012.html

Equipo de Desarrollo Vehicle Washing. (2026a). *Vehicle washing management system: Project documentation* (vehicle-w-docs) [Documentación de proyecto no publicada]. GitHub. https://github.com/code-sena/vehicle-w-docs

International Organization for Standardization. (2015). *Quality management systems — Requirements* (ISO 9001:2015). https://www.iso.org/standard/62085.html

International Organization for Standardization, International Electrotechnical Commission e Institute of Electrical and Electronics Engineers. (2017). *Systems and software engineering — Software life cycle processes* (ISO/IEC/IEEE 12207:2017). https://www.iso.org/standard/63712.html

International Organization for Standardization, International Electrotechnical Commission e Institute of Electrical and Electronics Engineers. (2022). *Software engineering — Software life cycle processes — Maintenance* (ISO/IEC/IEEE 14764:2022). https://www.iso.org/standard/80710.html

Servicio Nacional de Aprendizaje. (2026). *Guía para elaborar manuales de software: Manual de usuario, manual técnico, manual de instalación y manual de administrador* [Material de formación no publicado]. Programa Tecnólogo en Análisis y Desarrollo de Software.

## 16. Anexos

### Anexo A. Formato de Registro de una Acción

**Tabla 13**

*Formato de Registro de una Acción*

| Campo | Contenido |
|---|---|
| ID | AC-NN, ACO-NN, AP-NN o AM-NN |
| Tipo | Correctiva / Preventiva / De mejoramiento |
| Fecha de registro y quién la detectó |  |
| Descripción de la no conformidad, el riesgo o la oportunidad |  |
| Evidencia inicial (registro, captura, prueba, código de error) |  |
| Severidad (P0 a P3) y prioridad (Alta, Media, Baja) |  |
| Corrección inmediata aplicada (si aplica) |  |
| Causa raíz y técnica usada |  |
| Acción planificada, responsable y fecha compromiso |  |
| Rama, pull request y ADR relacionado |  |
| Criterio de cierre |  |
| Verificación de eficacia (quién, cuándo, evidencia) |  |
| Estado y fecha de cierre |  |
| Lección aprendida |  |

### Anexo B. Ejemplo de Análisis de Causa Raíz

**Tabla 14**

*Cinco Porqués de la Acción AC-01 (Horas Corridas Cinco Horas)*

| Pregunta | Respuesta |
|---|---|
| ¿Por qué el cliente veía su reserva a otra hora? | Porque la hora mostrada difería en cinco horas de la elegida. |
| ¿Por qué difería? | Porque la hora se guardaba convertida con una zona y se leía con otra. |
| ¿Por qué se usaban zonas distintas? | Porque la JVM del servicio tomaba la zona del equipo donde corría. |
| ¿Por qué la zona del equipo afectaba los datos? | Porque el código convertía fechas sin una zona explícita. |
| ¿Por qué no había una zona explícita? | Porque no existía una regla del equipo para el manejo del tiempo. |
| **Causa raíz** | Ausencia de una convención de tiempo: se adoptó "guardar en UTC y convertir solo en los bordes con *BOOKING_ZONE*", y la JVM corre en UTC. |

*Nota.* Elaborado por los autores a partir del riesgo cerrado C-001 del proyecto.

### Anexo C. Trazabilidad Entre Acciones, Riesgos y Deuda Técnica

**Tabla 15**

*Trazabilidad*

| Riesgo del proyecto | Deuda técnica | Acciones |
|---|---|---|
| R-002 payment-service parcial | TD-014, TD-015, TD-016, TD-017, TD-018 | AC-04 a AC-10, ACO-05 |
| R-003 Regresiones sin red de seguridad | TD-001, TD-006, TD-010 | ACO-01, AP-01, AP-07, AM-10 |
| R-004 Fuga de secretos | — | AP-03 |
| R-005 Evento perdido | TD-011 | AP-02 |
| R-007 Brechas de requisitos conocidas | TD-002, TD-003, TD-009 | AC-16, AC-17, ACO-02, ACO-09 |
| R-008 Pérdida de datos | — | AP-04 |
| R-010 Desactualización de la documentación | — | AC-23, ACO-12, AP-05 |
| R-001 Integración de operations-service | TD-020 | AM-01 |
| Ley 1581 de 2012 | — | ACO-03 |

*Nota.* Elaborado por los autores a partir del registro de riesgos y del backlog técnico del proyecto.
