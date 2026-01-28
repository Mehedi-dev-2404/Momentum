import datetime

class EnergyModel:
    # Determines if a task can be done at a given time
    # This file determines current energy level based on time.     

    def energy_meter(self, user_profile):
        current_hour = datetime.datetime.now().hour

        if current_hour in user_profile.peak_hours:
            return "HIGH"
        elif current_hour in user_profile.low_energy_hours:
            return "LOW"
        else:
            return "MEDIUM"
        