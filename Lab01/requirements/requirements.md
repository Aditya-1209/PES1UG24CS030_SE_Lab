# Requirements Specification

## Problem Statement #30: Airport Lost Luggage Claim & Tracking Portal

### Functional requirements

| ID | Type | Description | Priority | Acceptance criteria | Rationale |
|---|---|---|---|---|---|
| FR-001 | Functional | The system shall allow a passenger to submit a lost baggage claim using the baggage tag number, flight details, passenger information, contact information, and baggage description. | High | **Pass:** A claim is created and assigned a unique Claim ID when all mandatory details and a valid baggage tag are provided. **Fail:** A claim is not created when mandatory details are missing or the baggage tag cannot be validated. | Initiates the baggage recovery process with the information needed to identify the passenger and bag. |
| FR-002 | Functional | The system shall cross-reference a lost baggage claim with unrouted or unmatched baggage scan logs across connected airport terminals. | High | **Pass:** Relevant scan records are found and associated with the claim. **Fail:** Unrelated baggage records are not associated with the claim. | Uses airport scan data to locate misplaced baggage efficiently. |
| FR-003 | Functional | The system shall allow passengers and Baggage Service Agents to view a baggage tracking timeline containing the airport, terminal, scan location, date, and time for each available scan. | High | **Pass:** Authorized users see the available scan history in chronological order. **Fail:** A user cannot view scan history belonging to an unrelated claim. | Gives passengers transparency and agents the evidence needed to investigate. |
| FR-004 | Functional | The system shall notify the passenger whenever the baggage status changes, including Claim Registered, Bag Located, In Transit, and Ready for Delivery or Pickup. | Medium | **Pass:** One notification is generated after each relevant status change. **Fail:** No duplicate notification is generated when the status has not changed. | Keeps passengers informed without requiring repeated portal checks. |
| FR-005 | Functional | The system shall allow a Baggage Service Agent to approve an eligible compensation claim and initiate the compensation workflow when baggage is not recovered within the airline-defined time limit. | High | **Pass:** A verified, eligible claim can proceed to compensation processing after the recovery deadline. **Fail:** An incomplete, ineligible, or premature claim cannot initiate compensation. | Supports a controlled resolution when baggage cannot be recovered. |

### Non-functional requirements

| ID | Type | Description | Priority | Acceptance criteria | Rationale |
|---|---|---|---|---|---|
| NFR-001 | Performance | The baggage tracking timeline API shall return the complete available multi-leg scan history within 200 ms during normal and simulated peak loads. | High | **Pass:** The 95th-percentile response time is at most 200 ms under the agreed normal and peak test profiles. **Fail:** The 95th percentile exceeds 200 ms. | Fast responses improve passenger experience and agent productivity. |
| NFR-002 | Security | The system shall protect passenger, baggage, claim, and compensation data through authenticated, role-based access and encrypted network communication. | High | **Pass:** Access-control tests prevent unauthorized claim access, and all external traffic uses TLS 1.2 or later. **Fail:** Protected data is accessible without authorization or transmitted without encryption. | The portal processes sensitive personal, travel, and financial information. |

## Assumptions and constraints

- Airline booking, baggage-tag, and airport scan systems expose the data required for validation and matching.
- The airline defines the recovery deadline and compensation eligibility policy.
- A passenger can access only claims associated with their verified identity.
- A Baggage Service Agent acts within an authenticated, role-authorized session.

