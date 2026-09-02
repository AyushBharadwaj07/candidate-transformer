# Multi-Source Candidate Data Transformer

An AI/data-processing pipeline that combines candidate information from structured and unstructured sources and generates a clean, standardized candidate profile.

## Overview

Recruitment data often comes from multiple sources such as recruiter spreadsheets, resumes, and other candidate records. These sources can contain inconsistent formats, missing information, duplicate records, and unstructured text.

The **Candidate Transformer** addresses this problem by ingesting candidate data from multiple sources, extracting relevant information, normalizing the data, removing duplicate records, and generating a canonical candidate profile in JSON format.

The resulting structured profile can be used as a foundation for downstream recruitment systems such as candidate search, matching, ranking, and AI-powered screening.

## Problem Statement

Candidate information is often fragmented across:

- Recruiter CSV files
- Resume PDFs
- Different naming and formatting conventions
- Duplicate candidate records
- Unstructured resume content

Manually cleaning and combining this information is time-consuming and error-prone.

This project automates that transformation process.

## Key Features

- Multi-source candidate data ingestion
- CSV and PDF processing
- Resume information extraction
- Candidate data normalization
- Phone number normalization using E.164 format
- Skill extraction
- Duplicate candidate detection and removal
- Canonical candidate profile generation
- Confidence scoring
- Provenance tracking
- Runtime-configurable output
- JSON export
- Modular processing pipeline

## Data Sources

### Structured Data

Recruiter-provided CSV files containing candidate information such as:

- Name
- Email
- Phone
- Skills
- Experience
- Other candidate attributes

### Unstructured Data

Resume PDFs containing information such as:

- Candidate name
- Contact information
- Skills
- Education
- Experience
- Resume content

## Pipeline Architecture

```text
             ┌──────────────────┐
             │   Recruiter CSV  │
             └────────┬─────────┘
                      │
                      ▼
             ┌──────────────────┐
             │ Data Ingestion   │
             └────────┬─────────┘
                      │
                      │
             ┌────────▼─────────┐
             │ Data Processing  │
             │ & Normalization  │
             └────────┬─────────┘
                      │
                      │
     ┌────────────────┴────────────────┐
     │                                 │
     ▼                                 ▼
┌──────────────┐                ┌──────────────┐
│ Resume PDF   │                │ Candidate    │
│ Extraction   │                │ Data         │
└──────┬───────┘                └──────┬───────┘
       │                               │
       └───────────────┬───────────────┘
                       ▼
              ┌──────────────────┐
              │ Merge & Dedup    │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Canonical Profile│
              │ Generation       │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ JSON Output      │
              └──────────────────┘
