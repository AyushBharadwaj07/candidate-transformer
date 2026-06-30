import uuid


def build_candidate_profile(
    csv_data,
    name,
    emails,
    phones,
    skills
):
    return {
    "candidate_id": str(uuid.uuid4()),
    "full_name": name or csv_data.get("name"),

    "emails": list(
        set(
            emails +
            [csv_data.get("email")]
        )
    ),

    "phones": list(set(phones)),

    "current_company":
        csv_data.get("current_company"),

    "title":
        csv_data.get("title"),

    "skills": [
        {
            "name": skill,
            "confidence": 0.95
        }
        for skill in sorted(
            list(set(skills))
        )
    ],

    "provenance": {
        "full_name": [
            "csv",
            "resume"
        ],
        "emails": [
            "csv",
            "resume"
        ],
        "phones": [
            "resume"
        ],
        "skills": [
            "resume"
        ],
        "current_company": [
            "csv"
        ],
        "title": [
            "csv"
        ]
    },

    "overall_confidence": 0.95
}
