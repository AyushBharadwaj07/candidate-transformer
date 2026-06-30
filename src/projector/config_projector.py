def project_profile(candidate, config):
    projected = {}

    fields = config.get("fields", [])

    for field in fields:
        projected[field] = candidate.get(field)

    return projected