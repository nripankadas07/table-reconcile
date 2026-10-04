# table-reconcile

Keyed CSV reconciliation with exact decimal tolerances and duplicate-key errors.

An offline Python 3.10+ MVP with no runtime dependencies.

## Install and first useful result

```sh
git clone https://github.com/nripankadas07/table-reconcile.git
cd table-reconcile
python -m venv .venv
# POSIX; on Windows use .venv\Scripts\activate
. .venv/bin/activate
python -m pip install .
table-reconcile --help
python demo.py
```

The demo creates temporary synthetic inputs and prints the actual report; it does not require accounts, services, API keys or user data. CLI exit status: 0 = accepted/clean; 1 = review findings; 2 = invalid input or operational error.

## CLI example

```sh
table-reconcile old.csv new.csv --key id --tolerance total=0.01
```

Repeat `--key` for composite keys; repeat `--tolerance COLUMN=DECIMAL` for numeric columns.

## Validate

```sh
python -m unittest discover -v
python -m compileall -q table_reconcile.py
python demo.py
```

## Limits

UTF-8 CSV only; exact string keys; whole tables held in memory. Numeric cells and tolerances are limited to 1000 coefficient digits and absolute exponent 1000; finite values are compared without rounding. Decimal tolerances apply only to named columns and do not convert currencies or units. Output contains supplied cell values; do not share sensitive data.

See [RESEARCH.md](RESEARCH.md) for the user brief and dated comparisons, [VALIDATION.md](VALIDATION.md) for exact check coverage, and [SUPPORT.md](SUPPORT.md) for contributions and security reporting. MIT licensed; original implementation, with standard-library dependencies. No competitor code or prose copied.
