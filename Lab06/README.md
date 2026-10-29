# Lab 06 - Code and Branch Coverage

Code (line) and branch coverage analysis of the **L6_L7_29 Smart Thermostat Controller** using **coverage** and **pytest**, based on the Lab 6 student handout.

`thermostat_control.py` picks target temperatures by mode and time of day, chooses heating or cooling actions, and raises energy usage alerts.

## Submission Files

| Deliverable | File |
|---|---|
| Module under test | [thermostat_control.py](thermostat_control.py) |
| Starter test file | [test_thermostat_control.py](test_thermostat_control.py) |
| Test cases for code coverage | [CodeCoverageTest_thermostat_control.py](CodeCoverageTest_thermostat_control.py) |
| Test cases for branch coverage | [BranchCoverageTest_thermostat_control.py](BranchCoverageTest_thermostat_control.py) |
| Code coverage terminal output | [screenshots/code_coverage.png](screenshots/code_coverage.png) |
| Branch coverage terminal output | [screenshots/branch_coverage.png](screenshots/branch_coverage.png) |

## Results

Coverage of `thermostat_control.py`:

| Test file | Tests | Line coverage | Branch coverage | Missing lines |
|---|---|---|---|---|
| `test_thermostat_control.py` (starter) | 2 | 26% | 19% | 4-14, 18-27, 33-34, 37-39 |
| `CodeCoverageTest_thermostat_control.py` | 14 | 94% | 94% (2 partial branches) | 6, 26 |
| `BranchCoverageTest_thermostat_control.py` | 45 | 100% | 100% (28/28 branches) | - |

The code coverage tests exercise the main scenario of each function. The branch coverage tests drive every `if` and `for` decision both ways and add boundary values: the hours 6, 9, 17 and 22, a temperature difference of exactly ±1, outside temperatures of exactly 5 and 30, and exactly half the readings over the limit.

## Run

Install the tools, then run from the `Lab06` folder:

```bash
cd Lab06
python3 -m venv .venv
source .venv/bin/activate
python -m pip install coverage pytest
```

Code coverage:

```bash
coverage run -m pytest CodeCoverageTest_thermostat_control.py
coverage report -m
```

Branch coverage:

```bash
coverage run --branch -m pytest BranchCoverageTest_thermostat_control.py
coverage report -m
```
