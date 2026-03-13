# Microservices Architecture Description – CarpoolConnect

This microservices architecture decomposes CarpoolConnect into 6 independent, loosely-coupled services. Each service has a distinct responsibility, owns its own database, and communicates through REST APIs (synchronous) or message queues (asynchronous). Below is a detailed explanation of each service with clear purpose definitions:

---

## Service 1: Authentication Service

**Primary Purpose:** Secure user identity verification and access control management.

**Distinct Functionality:**
- Validates Corporate Single Sign-On (SSO) credentials against company identity providers
- Issues JWT tokens for authenticated users with role-based access claims
- Manages session lifecycle, token expiration, refresh mechanisms, and revocation
- Enforces role-based access control (RBAC) for five user types: Employees, HR Managers, Sustainability Officers, Facility Managers, IT Administrators
- Ensures GDPR compliance for authentication logs and user session data

**Database:** Auth DB
- Stores: JWT token blacklist, SSO provider configurations, user role mappings, session metadata

**Communication Pattern:**
- Synchronous: API Gateway calls this service on every request before routing to downstream services
- No downstream service dependencies

**Scalability:** Stateless design allows horizontal scaling with load balancing across multiple instances.

**Synergy:** Provides the foundational security layer; all other services rely on authenticated requests validated by this service.

---

## Service 2: User Service

**Primary Purpose:** Centralized management of user profiles and organizational hierarchy.

**Distinct Functionality:**
- Creates, updates, and retrieves employee profiles with personal information and preferences
- Maintains corporate hierarchy relationships (manager-subordinate, department assignments)
- Stores user preferences for commute routes, carpool preferences, and notification settings
- Manages user status (active, inactive, on-leave) to control participation eligibility
- Provides user data consistency across all services through a single source of truth

**Database:** User DB
- Stores: Employee profiles, preferences, corporate hierarchy, contact information, user status flags

**Communication Pattern:**
- Synchronous: Ride Matching Service queries user profiles; Messaging Service retrieves user information; Analytics Service accesses user metadata
- Called by: Ride Matching Service (for user compatibility data), Messaging Service (for participant info), Analytics Service (for user segmentation)

**Scalability:** Read-heavy service; caching strategies reduce direct database queries. Can scale independently based on profile lookup demand.

**Synergy:** Acts as the single source of truth for user data. All services requesting user information call this service to ensure consistency and avoid data duplication.

---

## Service 3: Ride Matching Service

**Primary Purpose:** Intelligent algorithm-driven pairing of employees for carpool arrangements.

**Distinct Functionality:**
- Computes optimal carpool matches based on commute routes, schedules, and user preferences
- Enforces <2 second response time requirement through optimized matching algorithms and caching
- Validates route compatibility using location data and transportation proximity rules
- Creates carpool groups dynamically and manages carpool lifecycle (formation, updates, dissolution)
- Publishes matching events to the message queue for Analytics Service to track utilization metrics

**Database:** Matching DB
- Stores: Carpool matches, route compatibility scores, matching history, active carpool groups, match timestamps

**Communication Pattern:**
- Synchronous: Calls User Service to fetch user profiles; Calls Schedule Service to verify availability compatibility
- Asynchronous: Publishes matching events to message queue for Analytics Service consumption

**Scalability:** CPU-intensive during peak commute hours; can scale horizontally with load balancing. Database indexing on routes and schedules optimizes query performance.

**Synergy:** Acts as the core business logic service. Depends on User Service for profile data and Schedule Service for availability information. Produces events consumed by Analytics Service.

---

## Service 4: Schedule Service

**Primary Purpose:** Management of commute schedules and availability validation.

**Distinct Functionality:**
- Stores and validates recurring commute patterns (e.g., Monday-Friday, 8:00 AM departure)
- Manages availability calendars with exceptions for holidays, time-off, and schedule changes
- Validates scheduling conflicts between potential carpool members
- Provides real-time availability status for compatibility checks during ride matching
- Updates schedule data when users modify commute times or availability

**Database:** Schedule DB
- Stores: Recurring schedules, availability slots, schedule exceptions, time-off periods, schedule modification history

**Communication Pattern:**
- Synchronous: Ride Matching Service queries schedule compatibility before creating matches
- Receives schedule updates from User interactions (via API Gateway)
- No downstream service dependencies

**Scalability:** Time-series data optimization enables efficient range queries during peak hours. Can scale with read replicas for schedule lookups.

**Synergy:** Provides critical availability data to Ride Matching Service. Ensures carpool members have compatible commute times and schedules.

---

## Service 5: Messaging Service

**Primary Purpose:** Internal communication platform for carpool group coordination.

**Distinct Functionality:**
- Maintains conversation threads between carpool members for pickup coordination, delay notification, and schedule adjustments
- Stores message history with timestamps and sender identification for traceability
- Manages notification metadata (read/unread status, delivery confirmation)
- Retrieves conversation context for carpool participants
- Publishes messaging activity events for Analytics Service to track engagement metrics

**Database:** Messaging DB
- Stores: Messages, conversation threads, message timestamps, sender/recipient mapping, carpool group associations, read/unread status

**Communication Pattern:**
- Synchronous: Queries User Service for participant information and validation
- Asynchronous: Publishes messaging events (new messages, thread activity) to message queue for Analytics Service and potential Notification Service integration

**Scalability:** Message volume scales with carpool growth; database sharding by conversation thread ID enables horizontal scaling.

**Synergy:** Enables post-match coordination for carpool members. Works with User Service for participant validation and publishes engagement data to Analytics Service.

---

## Service 6: Analytics Service

**Primary Purpose:** Data aggregation and business intelligence for organizational metrics.

**Distinct Functionality:**
- Consumes events from message queue published by Ride Matching, Schedule, and Messaging services
- Calculates environmental impact metrics: total CO₂ savings, fuel reduction, miles avoided
- Calculates financial metrics: total cost savings per employee, per carpool group, and organization-wide
- Generates participation reports: active carpools, employee engagement, program adoption rates
- Provides dashboards and reports for HR Managers (participation), Sustainability Officers (environmental impact), and Facility Managers (parking utilization trends)

**Database:** Analytics DB
- Stores: Aggregated metrics, calculated KPIs, historical trend data, report snapshots, user segmentation data

**Communication Pattern:**
- Asynchronous: Subscribes to message queue for events from Ride Matching, Schedule, and Messaging services
- Pull-based reporting: HR/Sustainability Officers request reports via API Gateway
- No synchronous service calls (event-driven processing)

**Scalability:** Event processing scales with message queue throughput. Historical data warehousing enables efficient reporting queries without impacting operational databases.

**Synergy:** Acts as the reporting and insights layer. Aggregates data from multiple services to provide executive visibility into program effectiveness and environmental impact.

---

## Architecture Overview

### Communication Patterns:

**Synchronous (REST API):**
- Ride Matching Service → User Service (fetch profiles)
- Ride Matching Service → Schedule Service (verify availability)
- Messaging Service → User Service (retrieve participant info)
- All services ← API Gateway (request routing)

**Asynchronous (Message Queue - RabbitMQ/Kafka):**
- Ride Matching Service → Event Queue (publish match events)
- Schedule Service → Event Queue (publish schedule updates)
- Messaging Service → Event Queue (publish message activity)
- Analytics Service ← Event Queue (consume all events)

### Database Strategy:

| Service | Database | Data Ownership |
|---------|----------|-----------------|
| Authentication Service | Auth DB | JWT tokens, SSO configs, role mappings |
| User Service | User DB | Employee profiles, hierarchy, preferences |
| Ride Matching Service | Matching DB | Carpool matches, compatibility scores |
| Schedule Service | Schedule DB | Recurring schedules, availability slots |
| Messaging Service | Messaging DB | Conversation threads, message history |
| Analytics Service | Analytics DB | Aggregated metrics, KPIs, reports |

### Scalability & Resilience:

**Horizontal Scaling:**
- Authentication Service: Scales with authentication request volume
- Ride Matching Service: Scales during peak commute hours (7-9 AM, 5-7 PM)
- Analytics Service: Scales with event processing backlog
- Schedule Service: Scales with availability query demand

**Fault Isolation:**
- Service failure does not cascade; circuit breakers prevent chain reactions
- Message queue ensures event loss prevention through retry mechanisms
- Timeouts on synchronous calls prevent infinite waits

**Performance Requirements:**
- Ride Matching Service: <2 second response time maintained through algorithm optimization and caching
- User Service: <100ms response time for profile lookups
- Schedule Service: <200ms response time for availability checks
- Analytics Service: Background processing; no real-time latency requirements

### Key Characteristics:

✅ **6 Distinct Services** – Each service has clear, independent responsibility  
✅ **Clear Purpose Definitions** – No ambiguity in functionality; each service owns specific domain  
✅ **Service Synergy** – Services work together through defined synchronous and asynchronous patterns  
✅ **Scalability** – Independent horizontal scaling based on individual demand  
✅ **GDPR Compliance** – Data isolation and security maintained at service level  
✅ **10K+ User Support** – Architecture supports corporate-scale deployment  
✅ **<2 Second Ride Matching** – Performance requirement maintained  
✅ **Technology Flexibility** – Each service can use optimal tech stack for its domain  