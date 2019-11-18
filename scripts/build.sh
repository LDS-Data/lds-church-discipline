#!/bin/sh
#./venv/bin/python scripts/extract_json.py > ./discipline.json
./venv/bin/python scripts/expand_json.py ./discipline_base.json > ./discipline.json
./venv/bin/python scripts/json_to_tsv.py ./discipline.json
./venv/bin/python scripts/json_to_md.py ./discipline.json > ./discipline.md

./venv/bin/python scripts/expand_json.py ./unconfirmed_base.json > ./unconfirmed.json
./venv/bin/python scripts/json_to_tsv.py ./unconfirmed.json
./venv/bin/python scripts/json_to_md.py ./unconfirmed.json > ./unconfirmed.md
