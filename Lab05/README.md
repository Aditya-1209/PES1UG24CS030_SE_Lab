# Lab 05 - Static Code Analysis

Static analysis of a Python digital wallet demonstration using **Pylint**, **Bandit**, and **Flake8**, based on the Lab 5 student handout.

## Submission Files

| Deliverable | File |
|---|---|
| Cleaned digital wallet implementation | [digital_wallet.py](digital_wallet.py) |
| Identified issues and fix approaches | [issues.md](issues.md) |
| Reflections on the analysis and fixes | [reflection.md](reflection.md) |

The issue table covers PIN hashing, temporary-file creation, credentials, OTP randomness, mutable defaults, naming, documentation, and formatting. Its original-code line numbers and commit reference refer to the earlier lab development work.

## Run

The demonstration uses Python 3 and only standard-library modules. From the repository root:

```bash
python3 Lab05/digital_wallet.py
```

The demo generates session credentials unless `WALLET_PIN` and `GATEWAY_SECRET` are set in the environment. Its expected final balance is Rs. 1900.0, total credited is Rs. 2500, and cashback is Rs. 8.4. The OTP changes on each run.

## Static Analysis

To run the three tools locally:

```bash
cd Lab05
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pylint bandit flake8
pylint digital_wallet.py
bandit -r digital_wallet.py
flake8 digital_wallet.py
```

This folder contains the three submitted deliverables listed above. The reflections describe results from the earlier development work; its reports and regression tests are not included here.
