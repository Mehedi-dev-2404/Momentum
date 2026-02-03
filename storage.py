import json
import os

class Storage:
    # Handles saving and loading data
    # This file saves and loads data from JSON.

    BASE_DIR = os.path.dirname(__file__)
    DATA_DIR = os.path.join(BASE_DIR, "data")

    task_file = os.path.join(DATA_DIR, "tasks.json")
    user_file = os.path.join(DATA_DIR, "user_profile.json")

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