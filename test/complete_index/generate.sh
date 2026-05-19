#!/bin/bash

PYTHONPATH=../../src python3 -m page_book_generator.program \
  --language "pt" \
  --index-data "index_data.json" \
  --description "description.txt" \
  --screenshot1 "screenshot1.png" \
  --screenshot2 "screenshot2.png" \
  --cover "cover.png" \
  --bibliography "bibliography.bib" \
  --template-type "complete" \
  --output-dir "output"
