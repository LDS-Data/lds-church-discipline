#!/bin/sh
./venv/bin/python scripts/extract_json.py > ./discipline.json
./venv/bin/python scripts/json_to_tsv.py
./venv/bin/python scripts/json_to_md.py > ./discipline.md
