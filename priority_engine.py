from datetime import datetime, timedelta

class PriorityEngine:
    # Decides task importance ordering
    #This file ranks tasks based on urgency and importance.

    def rank_tasks(self, tasks, current_energy, current_time):

        ranked_tasks = []

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
                
                deadline = task.deadline
                time_left = (deadline - current_time)

                if time_left <= timedelta(0):
                    score += 5
                elif time_left <= timedelta(days=1):
                    score += 4
                elif time_left <= timedelta(days=3):
                    score += 3
                elif time_left <= timedelta(days=7):
                    score += 2
                else:
                    score += 1

                ranked_tasks.append((score, task))

        ranked_tasks.sort(key=lambda x: x[0], reverse=True) 
        return [task for score, task in ranked_tasks]