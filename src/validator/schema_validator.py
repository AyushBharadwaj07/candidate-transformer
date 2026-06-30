def validate_profile(profile):
    required_fields = [
        "full_name",
        "emails",
        "phones"
    ]

    for field in required_fields:
        if field not in profile:
            profile[field] = None

    return profile