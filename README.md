# Software Engineering Lab Submissions

This repository contains my **Software Engineering Laboratory submissions**, organized by lab with requirements, design artifacts, source code, reports, and supporting evidence.

## Lab Submissions

| Lab | Title | Submission |
|---|---|---|
| Lab 01 | Requirements Engineering and UML Use-Case Modelling | [Requirements, use case, and diagram](Lab01/README.md) |
| Lab 02 | Agile Project Management using Jira | [Submission report](Lab02/Jira_Lab_2_Airport_Lost_Luggage_Submission.pdf) |
| Lab 03 | Airport Lost Luggage Portal - Component Modelling & Architecture | [Architecture and component diagram](Lab03/README.md) |
| Lab 04 | Donkey Kong Repair Lab - AI-Assisted Debugging and Feature Development | [Implementation, tests, and recordings](Lab04/README.md) |

Labs 01–03 cover **Problem Statement #30: Airport Lost Luggage Claim & Tracking Portal**. Lab 04 is a separate Pygame debugging and feature-development exercise.

## Repository Structure

```text
PES1UG24CS030_SE_Lab/
|-- .gitignore
|-- README.md
|-- Lab01/
|   |-- README.md
|   |-- requirements/requirements.md
|   |-- use-case-specification/UC01_Submit_Lost_Baggage_Claim.md
|   `-- uml/use_case_diagram.pdf
|-- Lab02/
|   `-- Jira_Lab_2_Airport_Lost_Luggage_Submission.pdf
|-- Lab03/
|   |-- README.md
|   |-- Lab3_Component_Diagram.pdf
|   `-- Lab3_Architecture_Justification.pdf
`-- Lab04/
    |-- README.md
    |-- game.py
    |-- test_game.py
    |-- requirements.txt
    |-- before.mov
    |-- after.mov
    |-- Chat_History.pdf
    |-- COMMIT_HISTORY.txt
    |-- RUN_AND_HISTORY.txt
    `-- repository-history.bundle
```

## Run Lab 04

Use Python 3.10 or later. From the repository root:

```bash
cd Lab04
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python game.py
```

On Windows, create the environment with `python -m venv .venv` and activate it with `.venv\Scripts\activate.bat` in Command Prompt or `.\.venv\Scripts\Activate.ps1` in PowerShell.

Run the automated checks from `Lab04` with the environment active:

```bash
python -m unittest -v
```

See the [Lab 04 README](Lab04/README.md) for controls, implemented features, and submission evidence.

## Notes

- Each submission is stored in its corresponding `LabXX` folder.
- Diagrams and reports are provided as PDFs; Lab 04 also includes source code, tests, gameplay recordings, and an archived Git history.
- This repository is maintained for academic and educational purposes.

## Author

**Aditya Patil**
