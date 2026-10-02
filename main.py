   # AuraCare Health System Core
APP_VERSION = "2.0.0-Beta"
MODULES_ENABLED = ["appointments", "prescriptions"]



   def get_doctor_schedule(doctor_name):
    schedules = {
        "Dr. Ahmed": ["Mon 9:00-13:00", "Wed 14:00-18:00"],
        "Dr. Sara": ["Tue 10:00-14:00", "Thu 9:00-12:00"],
    }
    return schedules.get(doctor_name, "No schedule found")
  
  

    
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
