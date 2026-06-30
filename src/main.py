from extractors.csv_parser import read_csv
from extractors.pdf_parser import read_pdf

from extractors.resume_extractor import (
    extract_name,
    extract_email,
    extract_phone,
    extract_skills
)

from normalizers.phone_normalizer import (
    normalize_phone
)

from merger.profile_merger import (
    build_candidate_profile
)

from projector.config_projector import (
    project_profile
)

from validator.schema_validator import (
    validate_profile
)

import json


# -----------------------------
# Read Sources
# -----------------------------

csv_data = read_csv(
    "input/recruiter.csv"
)

resume_text = read_pdf(
    "input/AYUSH_BHARADWAJ_RESUME.pdf"
)

with open(
    "input/config.json",
    "r",
    encoding="utf-8"
) as f:
    config = json.load(f)


# -----------------------------
# Extract Resume Fields
# -----------------------------

name = extract_name(
    resume_text
)

emails = extract_email(
    resume_text
)

phones = extract_phone(
    resume_text
)

skills = extract_skills(
    resume_text
)


# -----------------------------
# Normalize Phones
# -----------------------------

normalized_phones = []

for phone in phones:
    p = normalize_phone(phone)

    if p:
        normalized_phones.append(p)


# -----------------------------
# Build Canonical Profile
# -----------------------------

candidate = build_candidate_profile(
    csv_data,
    name,
    emails,
    normalized_phones,
    skills
)


# -----------------------------
# Validate
# -----------------------------

candidate = validate_profile(
    candidate
)


# -----------------------------
# Project Config Output
# -----------------------------

projected_profile = project_profile(
    candidate,
    config
)


# -----------------------------
# Print
# -----------------------------

print("\n===== FINAL OUTPUT =====")

print(
    json.dumps(
        projected_profile,
        indent=4
    )
)


# -----------------------------
# Save JSON
# -----------------------------

with open(
    "output/candidate_profile.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        projected_profile,
        f,
        indent=4
    )

print(
    "\nProfile saved successfully!"
)