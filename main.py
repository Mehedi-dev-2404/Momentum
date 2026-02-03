# Entry point. Coordinates planner components.
from storage import Storage
from user_profile import UserProfile
from energy_model import EnergyModel
from priority_engine import PriorityEngine
from scheduler import Scheduler
from datetime import datetime
from task import Task

def add_task(storage):
    title = input("Enter task title: ")
    priority = input("Enter task priority (LOW, MEDIUM, HIGH): ").upper()
    energy_required = input("Enter energy required (LOW, MEDIUM, HIGH): ").upper()
    deadline = input("Enter task deadline (YYYY-MM-DD HH:MM): ")
    estimated_duration = int(input("Enter estimated duration (in minutes): "))
    
    new_task = Task(
        title=title,
        priority=priority,
        energy_required=energy_required,
        deadline=deadline,
        estimated_duration=estimated_duration
        status='PENDING'
    )

    tasks = storage.load_tasks()
    tasks.append(new_task.__dict__)
    storage.save_tasks(tasks)

    print("\nTask added successfully!")

    def view_tasks(storage):

        tasks = [Task(**task) for task in storage.load_tasks()]
        user_profile_data = storage.load_user_profile()
        user_profile = UserProfile(**user_profile_data)

        energy_model = EnergyModel()
        priority_engine = PriorityEngine()
        scheduler = Scheduler(user_profile, energy_model)

        ranked_tasks = priority_engine.rank_tasks(
            tasks=tasks,
            current_energy=energy_model.energy_meter(user_profile),
            current_time=datetime.now()
        )

        daily_schedule = scheduler.create_daily_schedule(ranked_tasks)
        print("\n🗓️ Today’s Schedule\n")

        if not daily_schedule:
            print("No tasks scheduled.")
            return
        for block in daily_schedule:
            print(
                block['start_time'].strftime("%H:%M"),
                "→",
                block['end_time'].strftime("%H:%M"),
                block['task'].title
            )

def main():
    storage = Storage()
    tasks = [Task(**task) for task in storage.load_tasks()]
    user_profile_data = storage.load_user_profile()

    user_profile = UserProfile(**user_profile_data)

    energy_model = EnergyModel()
    priority_engine = PriorityEngine()
    scheduler = Scheduler(user_profile, energy_model)

    ranked_tasks = priority_engine.rank_tasks(
        tasks=tasks,
        current_energy=energy_model.energy_meter(user_profile),
        current_time=datetime.now()
    )

    daily_schedule = scheduler.create_daily_schedule(ranked_tasks)

    for block in daily_schedule:
        print(
            block['task'].title,
            block['start_time'],"→",
            block['end_time']
        )

