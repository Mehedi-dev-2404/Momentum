import datetime

class PriorityEngine:
    # Decides task importance ordering
    #This file ranks tasks based on urgency and importance.

    def rank_tasks(self, tasks, current_energy, current_time):
        for task in tasks:
            if task.status == 'PENDING':
                score = 0
                if task.priority == 'HIGH':
                    score += 3
                elif task.priority == 'MEDIUM':
                    score += 2
                else:
                    score += 1
                
                if task.energy_required == current_energy:
                    score += 2
                
                deadline_hour = int(task.deadline)
                hours_until_deadline = (deadline_hour - current_time) % 24
                if hours_until_deadline <= 24:
                    score += 3
                elif hours_until_deadline <= 72:
                    score += 2
                elif hours_until_deadline <= 168:
                    score += 1
        