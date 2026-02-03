import datetime

class Task:
    # Represents a single unit of work
    # This file defines what a task is and validates its data.
    def __init__(self, title, deadline, estimated_duration, priority, energy_required, status='PENDING'):
        self.title = title
        self.deadline = deadline
        self.estimated_duration = estimated_duration
        self.priority = priority
        self.energy_required = energy_required
        self.status = status  # possible statuses: PENDING, COMPLETED, SKIPPED
        self._created_at = datetime.datetime.now()  # to be set when the task is created
        self.deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d %H:%M")
        self.validate()
    
    def validate(self):
        # Validate task data
        if not self.title or not isinstance(self.title, str):
            raise ValueError("Title must be a non-empty string.")
        if not isinstance(self.deadline, datetime.datetime):
            raise ValueError("Deadline must be a datetime object.")
        if not isinstance(self.estimated_duration, int) or self.estimated_duration <= 0:
            raise ValueError("Estimated duration must be a positive integer.")
        if self.priority not in ['LOW', 'MEDIUM', 'HIGH']:
            raise ValueError("Priority must be one of: LOW, MEDIUM, HIGH.")
        if not self.energy_required in ['HIGH', 'MEDIUM', 'LOW']:
            raise ValueError("Energy required must be one of: HIGH, MEDIUM, LOW.")
        if self.status not in ['PENDING', 'COMPLETED', 'SKIPPED']:
            raise ValueError("Status must be one of: PENDING, COMPLETED, SKIPPED.")