   # AuraCare Health System Core
   APP_VERSION = "1.0.0"
   MODULES_ENABLED = []

def get_priority(symptom):
    if symptom in ("no pulse", "not breathing"):
        return 1
    elif symptom in ("chest pain", "stroke"):
        return 2
    elif symptom in ("broken bone", "high fever"):
        return 3
    elif symptom in ("sprained ankle", "minor cut"):
        return 4
    return 5