#!/bin/bash

python3 ../src/page_book_generator/main.py \
  --language "en" \
  --index-data "index_data.json" \
  --description "description.txt" \
  --bibliography "bibliography.bib" \
  --output-dir "output"
