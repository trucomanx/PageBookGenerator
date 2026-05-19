#!/bin/bash

python3 ../../src/page_book_generator/main.py \
  --language "en" \
  --index-data "index_data.json" \
  --description "description.txt" \
  --screenshot1 "screenshot1.png" \
  --screenshot2 "screenshot2.png" \
  --cover "cover.png" \
  --template-type "print-only" \
  --output-dir "output"
