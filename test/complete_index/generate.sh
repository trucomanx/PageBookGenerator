#!/bin/bash

python3 ../../src/page_book_generator/main.py \
  --language "pt" \
  --index-data "index_data.json" \
  --description "description.txt" \
  --bibliography "bibliography.bib" \
  --template-type "complete" \
  --output-dir "output"
