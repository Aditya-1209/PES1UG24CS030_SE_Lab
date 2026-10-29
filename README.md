# Software Engineering Lab Submissions

This repository contains my **Software Engineering Laboratory submissions**, organized by lab with requirements, design artifacts, source code, reports, and supporting evidence.

## Lab Submissions

| Lab | Title | Submission |
|---|---|---|
| Lab 01 | Requirements Engineering and UML Use-Case Modelling | [Requirements, use case, and diagram](Lab01/README.md) |
| Lab 02 | Agile Project Management using Jira | [Submission report](Lab02/Jira_Lab_2_Airport_Lost_Luggage_Submission.pdf) |
| Lab 03 | Airport Lost Luggage Portal - Component Modelling & Architecture | [Architecture and component diagram](Lab03/README.md) |
| Lab 04 | Donkey Kong Repair Lab - AI-Assisted Debugging and Feature Development | [Implementation, tests, and recordings](Lab04/README.md) |
| Lab 05 | Static Code Analysis | [Digital wallet, issue table, and reflections](Lab05/README.md) |
| Lab 06 | Code and Branch Coverage Analysis | [Coverage tests and terminal screenshots](Lab06/README.md) |

Labs 01–03 cover **Problem Statement #30: Airport Lost Luggage Claim & Tracking Portal**. Lab 04 is a separate Pygame debugging and feature-development exercise. Lab 05 applies static analysis to a Python digital wallet demonstration. Lab 06 measures code and branch coverage of a Python smart thermostat controller.

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
|-- Lab04/
|   |-- README.md
|   |-- game.py
|   |-- test_game.py
|   |-- requirements.txt
|   |-- before.mov
|   |-- after.mov
|   |-- Chat_History.pdf
|   |-- COMMIT_HISTORY.txt
|   |-- RUN_AND_HISTORY.txt
|   `-- repository-history.bundle
|-- Lab05/
|   |-- README.md
|   |-- digital_wallet.py
|   |-- issues.md
|   `-- reflection.md
`-- Lab06/
    |-- README.md
    |-- thermostat_control.py
    |-- test_thermostat_control.py
    |-- CodeCoverageTest_thermostat_control.py
    |-- BranchCoverageTest_thermostat_control.py
    `-- screenshots/
        |-- code_coverage.png
        `-- branch_coverage.png
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

## Run Lab 05

From the repository root:

```bash
python3 Lab05/digital_wallet.py
```

See the [Lab 05 README](Lab05/README.md) for the deliverables and static analysis commands.

## Run Lab 06

Install `coverage` and `pytest` (`python -m pip install coverage pytest`), then from the repository root:

```bash
cd Lab06
coverage run --branch -m pytest BranchCoverageTest_thermostat_control.py
coverage report -m
```

See the [Lab 06 README](Lab06/README.md) for the code coverage run and the coverage results.

## Notes

- Each submission is stored in its corresponding `LabXX` folder.
- Diagrams and reports are provided as PDFs; Lab 04 also includes source code, tests, gameplay recordings, and an archived Git history; Lab 06 includes coverage terminal screenshots.
- This repository is maintained for academic and educational purposes.

## Author

**Aditya Patil**
