class UserProfile:
    # Represents user capacity and energy patterns
    # This file defines the user’s energy patterns and daily limits.
    def __init__(self, peak_hours, low_energy_hours, daily_capacity_minutes):
        self.peak_hours = peak_hours  # List of hours when user is most energetic
        self.low_energy_hours = low_energy_hours  # List of hours when user is least energetic
        self.daily_capacity_minutes = daily_capacity_minutes  # Total minutes user can work daily
        self.validate()
    
    def validate(self):
        # Validate user profile data
        if not isinstance(self.peak_hours, list) :
            raise ValueError("Peak hours must be a list")
        if not isinstance(self.low_energy_hours, list):
            raise ValueError("Low energy hours must be a list")
        if not isinstance(self.daily_capacity_minutes, int) or self.daily_capacity_minutes <= 0:
            raise ValueError("Daily capacity must be a positive integer.")