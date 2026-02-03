# Entry point. Coordinates planner components.
from storage import Storage
from user_profile import UserProfile
from energy_model import EnergyModel
from priority_engine import PriorityEngine
from scheduler import Scheduler
from datetime import datetime

def main():
    storage = Storage()
    tasks = storage.load_tasks()
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


if __name__ == "__main__":
    main()