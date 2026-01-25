import json

class Storage:
    # Handles saving and loading data
    # This file saves and loads data from JSON.

    task_file = '/Users/mehedimostafa/Desktop/PROJECTS/New Projectxx/Momentum/data/tasks.json'
    user_file = '/Users/mehedimostafa/Desktop/PROJECTS/New Projectxx/Momentum/data/user_profile.json'

    def save_tasks(self, tasks):
        with open(self.task_file, 'w') as file:
                json.dump(tasks, file)
    
    def load_tasks(self):
        with open(self.task_file, 'r') as file:
            tasks_data = json.load(file)
            return tasks_data
    
    def save_user_profile(self, user_profile):
        with open(self.user_file, 'w') as file:
            json.dump(user_profile, file)
    
    def load_user_profile(self):
        with open(self.user_file, 'r') as file:
            user_profile_data = json.load(file)
            return user_profile_data