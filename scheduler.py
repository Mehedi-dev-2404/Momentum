from datetime import datetime, timedelta

class Scheduler:
    # Allocates tasks into time slots
    # This file assigns tasks to time slots based on constraints.
    def __init__(self, user_profile, energy_model):
        self.user_profile = user_profile
        self.energy_model = energy_model
    
    def create_daily_schedule(self, ranked_tasks):
        """
        Returns a list of scheduled task blocks for today. 
        Each block will later contain:
        - task
        - start_time
        - end_time
        """
        current_time = datetime.now()
        remaining_capacity = self.user_profile.daily_capacity_minutes

        daily_schedule = []
        energy_levels = {'HIGH': 3, 'MEDIUM': 2, 'LOW': 1}

        for task in ranked_tasks:  
            current_energy = self.energy_model.energy_meter(self.user_profile)
            if remaining_capacity <= 0:
                continue
            elif task.estimated_duration > remaining_capacity:
                continue
            if energy_levels[current_energy] >= energy_levels[task.energy_required]:
                start_time = current_time
                end_time = start_time + timedelta(minutes=task.estimated_duration)

                daily_schedule.append({
                    'task': task,
                    'start_time': start_time,
                    'end_time': end_time
                })
                current_time = end_time
                remaining_capacity -= task.estimated_duration
            else:
                continue

        return daily_schedule