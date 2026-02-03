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
        estimated_duration=estimated_duration,
        status='PENDING'
    )

    task_data = {
    "title": new_task.title,
    "priority": new_task.priority,
    "energy_required": new_task.energy_required,
    "estimated_duration": new_task.estimated_duration,
    "deadline": new_task.deadline.strftime("%Y-%m-%d %H:%M"),
    "status": new_task.status}
    
    tasks = storage.load_tasks(task_data)
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

    task_number = 1

    if not daily_schedule:
        print("No tasks scheduled.")
        return
    for block in daily_schedule:
        print(f"Task: {task_number}.")
        print(
            block['start_time'].strftime("%H:%M"),
            "→",
            block['end_time'].strftime("%H:%M"),
            block['task'].title
        )
        task_number += 1

def main():
    storage = Storage()
    while True:
        print("Welcome to Momnentum Task Scheduler")
        print("1. Add Task")
        print("2. View Today's Schedule")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(storage)
        elif choice == '2':
            view_tasks(storage)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()