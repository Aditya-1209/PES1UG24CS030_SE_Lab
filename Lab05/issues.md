# Static analysis issue table

Line numbers refer to the original `digital_wallet.py` at commit `0d188e2`.
Bandit severity labels below are tool output; Pylint categories are not equivalent
security severity ratings. The high and medium security findings are listed first.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Bandit B324: weak SHA-1 | Security, High | 14 | A fast, unsalted SHA-1 digest protects the PIN. | Use PBKDF2-HMAC-SHA256 with 600,000 iterations and a random 16-byte session salt; compare derived hashes with `secrets.compare_digest`. |
| Bandit B306: `mktemp` | Security, Medium | 60 | A temporary filename is returned without creating the file, leaving a race. | Create the file atomically with `NamedTemporaryFile(delete=False)` and close it before returning the path; document caller cleanup. |
| Bandit B105: embedded gateway secret | Security, Low | 6 | The gateway credential is stored in source code. | Read it from the environment or generate an ephemeral demo secret. Apply the same treatment to the demo PIN and update demo calls. |
| Bandit B311: insecure randomness | Security, Low | 64 | `random.randint` is inappropriate for an OTP. | Use `secrets.randbelow(900000) + 100000` to retain the six-digit range. |
| Pylint W0102: mutable default | Bug, Warning | 17 | The default log list persists across calls. | Default to `None`, create a fresh list per call, and preserve explicitly supplied lists. |
| Pylint W0603: global statement | Maintainability, Warning | 28 | Updating the limit rebinds global state. | Keep the limit with the balance in the existing wallet state dictionary. |
| Pylint W0613: unused argument | Maintainability, Warning | 50 | The flat cashback rate does not use merchant type. | Rename it to `_merchant_type` and document that it is reserved; preserve the positional argument and flat rate. |
| Pylint C0103: naming | Convention | 9, 13, 17, 27, 32, 45, 50, 54, 58, 78 | Functions and locals use inconsistent camelCase names. | Use snake_case names and update callers; move the limit into wallet state. |
| Pylint C0114/C0116: missing docstrings | Documentation, Convention | 1, 13, 17, 27, 32, 45, 50, 54, 58, 63 | The module and functions lack documented purpose. | Add module and function docstrings, including the receipt cleanup contract. |
| Flake8 E261 | Style | 76 | Inline comment has only one preceding space. | Insert two spaces. |
| Flake8 E225/E231 | Style | 78-79 | Assignment and argument separators lack spaces. | Add spaces around `=` and after the comma. |
| Flake8 E305 | Style | 80 | The top-level demo call follows a function without two blank lines. | Separate the new `__main__` guard with two blank lines. |

An additional import guard prevents the demo from running when the module is
imported for tests. No analysis rules are disabled and no `nosec` suppressions are
used. The script remains an educational, in-memory demo: a clean scan does not
establish production payment security or validate all business rules.
