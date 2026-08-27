# Airport Lost Luggage Claim & Tracking Portal

Software Engineering Lab 1 submission for **Problem Statement #30**.

## Deliverables

- [Requirements](requirements/requirements.md) - five functional and two non-functional requirements
- [Use-case specification](use-case-specification/UC01_Submit_Lost_Baggage_Claim.md) - detailed UC-01 flow
- [UML use-case diagram](uml/use_case_diagram.pdf) - submission-ready PDF

## System overview

The portal lets passengers report missing baggage and track its recovery. Baggage Service Agents use baggage scan logs to locate bags, update claim status, and process compensation when a bag remains unrecovered beyond the airline-defined time limit.

## Actors

- Passenger
- Baggage Service Agent

## Repository structure

```text
airport-lost-luggage-portal/
|-- README.md
|-- requirements/
|   `-- requirements.md
|-- uml/
|   `-- use_case_diagram.pdf
`-- use-case-specification/
    `-- UC01_Submit_Lost_Baggage_Claim.md
```

## Traceability summary

| Requirement | Related use case(s) |
|---|---|
| FR-001 | Submit Lost Baggage Claim; Validate Baggage Tag |
| FR-002 | Match Lost Bag; Search Baggage Scan Logs |
| FR-003 | Track Baggage Status; View Scan Timeline |
| FR-004 | Update Baggage Status; Receive Status Notification |
| FR-005 | Process Compensation |

