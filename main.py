   # AuraCare Health System Core
   APP_VERSION = "1.0.0"
   MODULES_ENABLED = []



   def get_doctor_schedule(doctor_name):
    schedules = {
        "Dr. Ahmed": ["Mon 9:00-13:00", "Wed 14:00-18:00"],
        "Dr. Sara": ["Tue 10:00-14:00", "Thu 9:00-12:00"],
    }
    return schedules.get(doctor_name, "No schedule found")

    
