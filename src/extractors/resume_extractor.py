import re


def extract_email(text):
    emails = re.findall(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        text
    )
    return list(set(emails))


def extract_phone(text):
    phones = re.findall(
        r'(\(?\+?\d[\d\s\-\(\)]{8,}\d)',
        text
    )
    return list(set(phones))


def extract_name(text):
    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if line:
            return line.title()

    return None

def extract_skills(text):
    skill_set = {
        "Python",
        "SQL",
        "C",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "Matplotlib",
        "Seaborn",
        "LangChain",
        "Ollama",
        "Llama",
        "Git",
        "GitHub",
        "Streamlit",
        "REST APIs",
        "Machine Learning",
        "Artificial Intelligence",
        "Prompt Engineering"
    }

    found = []

    lower_text = text.lower()

    for skill in skill_set:
        if skill.lower() in lower_text:
            found.append(skill)

    return sorted(list(set(found)))