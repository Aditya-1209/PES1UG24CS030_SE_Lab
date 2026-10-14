# Lab reflections

The supplied three-page handout requests reflections but does not list the
questions. The repository README refers to four questions. These four prompts
are therefore based on the lab objectives, not quoted from the handout.

## 1. What did each tool contribute?

Pylint identified the shared mutable default, global rebinding, unused argument,
inconsistent names, and missing documentation. Bandit identified the weak PIN
hash, unsafe temporary-file creation, hardcoded gateway credential, and
non-cryptographic OTP generator. Flake8 identified spacing and blank-line errors.
Together they covered code quality, security patterns, and consistent formatting.

## 2. Which findings were prioritized, and why?

The high-severity SHA-1 finding and medium-severity `mktemp` finding came first.
PIN hashing now uses a salted, deliberately expensive derivation, and receipt
creation now reserves the file atomically. The lower-severity embedded credential
and OTP randomness findings were fixed in the same security commit. The mutable
default was also a meaningful correctness issue because its list survives across
calls and can accumulate unrelated operations.

## 3. How were the fixes verified without changing the demonstration?

All three tools were run before and after the changes, without disabling rules.
Pylint improved from 5.69/10 to 10.00/10, Bandit went from four findings to zero,
and Flake8 went from four findings to zero. Six regression tests verify the demo
output apart from its random OTP, import behavior, top-ups, payment rejection and
acceptance, credential checks, and private unique receipt files. The demo still
ends with Rs. 1900.0, Rs. 2500 total credited, and Rs. 8.4 cashback.

## 4. What are the benefits and limitations of static analysis?

Static analysis gives fast, repeatable feedback before code is executed. The
reports also provide a concrete checklist for review. However, passing these
checks does not prove that business rules are correct or that a payment system is
secure. For example, this demo still needs validation of non-finite/nonpositive
payment inputs, cumulative daily spending, and production credential storage.
Runtime tests and human review remain necessary. The randomly generated fallback
credentials and salt are intentionally ephemeral demo state, not persistent
account credentials.
