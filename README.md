# Multi-Source Candidate Data Transformer

## Overview
This project ingests candidate information from multiple sources and generates one canonical candidate profile.

## Sources
- Structured: Recruiter CSV
- Unstructured: Resume PDF

## Features
- Multi-source ingestion
- Data extraction
- Phone normalization (E.164)
- Skill extraction
- Deduplication
- Canonical profile generation
- Confidence scoring
- Provenance tracking
- Runtime configurable output
- JSON export

## Installation

pip install -r requirements.txt

## Run

python src/main.py

## Output

Generated file:

output/candidate_profile.json

## Project Structure

candidate-transformer/
├── input/
├── output/
├── src/
├── tests/
├── requirements.txt
└── README.md