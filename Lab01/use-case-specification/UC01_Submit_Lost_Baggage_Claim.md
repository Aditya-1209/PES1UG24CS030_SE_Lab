# UC-01: Submit Lost Baggage Claim

| Field | Specification |
|---|---|
| Use-case ID | UC-01 |
| Use-case name | Submit Lost Baggage Claim |
| Scope | Airport Lost Luggage Claim & Tracking Portal |
| Level | User goal |
| Primary actor | Passenger |
| Supporting actor | Baggage Service Agent |
| Goal | Create a traceable claim so the airline can locate and recover the passenger's missing baggage. |
| Trigger | The passenger determines that checked baggage has not arrived and chooses to report it. |

## Preconditions

1. The passenger travelled on a valid airline booking.
2. The passenger has a baggage tag number associated with the journey.
3. The passenger can access the portal.
4. Flight and baggage scan information is available to the system.

## Postconditions

### Success guarantees

- A lost baggage claim is stored.
- A unique Claim ID is generated.
- Available baggage scans are associated with the claim.
- The current status and last known scan location are recorded.
- The passenger can track the claim and receives a registration notification.

### Minimal guarantees

- No claim is created when mandatory information cannot be validated.
- The attempted submission does not alter unrelated baggage or claim records.

## Main success scenario

1. The passenger opens the portal.
2. The passenger selects **Report Lost Baggage**.
3. The system displays the lost baggage claim form.
4. The passenger enters passenger details, flight number, travel date, baggage tag number, baggage description, and contact information.
5. The passenger submits the form.
6. The system validates the mandatory fields and baggage tag number.
7. The system retrieves scan records associated with the baggage tag.
8. The system cross-references those scans with unmatched or unrouted baggage records.
9. The system creates the claim.
10. The system generates a unique Claim ID.
11. The system records the current baggage status and last known scan location.
12. The system displays the Claim ID and current status.
13. The system sends a claim-registration notification to the passenger.
14. The passenger can use the Claim ID to track recovery progress.

## Alternate and exception flows

### A1 - Invalid or unrecognized baggage tag

Begins at step 6.

1. The system determines that the baggage tag is incorrectly formatted, unknown, or not associated with the passenger's journey.
2. The system does not create a claim.
3. The system highlights the baggage-tag field and displays: **The baggage tag number could not be verified. Please check the number and try again.**
4. The passenger corrects the baggage tag and resubmits.
5. The use case resumes at step 6.

### A2 - Missing mandatory information

Begins at step 6.

1. The system identifies each missing or invalid mandatory field.
2. The system preserves the valid entries and displays field-level guidance.
3. The passenger supplies or corrects the information and resubmits.
4. The use case resumes at step 6.

### A3 - Scan service temporarily unavailable

Begins at step 7.

1. The system cannot retrieve baggage scans.
2. The system creates the claim with status **Claim Registered - Scan Data Pending**.
3. The system generates and displays the Claim ID.
4. The system queues scan retrieval for retry and notifies the passenger that tracking data may be delayed.
5. The main flow resumes at step 13.

### A4 - Potential duplicate claim

Begins at step 9.

1. The system finds an open claim for the same passenger, flight, and baggage tag.
2. The system does not create a duplicate claim.
3. The system displays the existing Claim ID and provides access to its current status.
4. The use case ends.

## Business rules

- BR-01: A baggage tag must be linked to the passenger's journey before a standard claim can be created.
- BR-02: Each claim must have a unique Claim ID.
- BR-03: Only authorized users may view or update a claim.
- BR-04: Compensation processing is available only after the airline-defined recovery deadline and eligibility verification.

## Related requirements

- Primary: FR-001
- Supporting: FR-002, FR-003, FR-004, NFR-001, NFR-002

