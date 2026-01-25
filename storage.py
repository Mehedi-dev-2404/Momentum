class Storage:
    # Handles saving and loading data
    # This file saves and loads data from JSON.

    task_file = '/Users/mehedimostafa/Desktop/PROJECTS/New Projectxx/Momentum/data/tasks.json'

    try:
        with open(task_file, 'w') as file:
            file.write('[]')
    except FileNotFoundError:
        with open(task_file, 'w') as file:
            file.write('[]')