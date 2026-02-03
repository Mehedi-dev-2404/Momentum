# Momentum - Energy-Aware Task Scheduler

<div align="center">

**Smart Task Management That Adapts to Your Energy Levels**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-clean-brightgreen.svg)](https://github.com/yourusername/Momentum)

</div>

## Overview

**Momentum** is an intelligent task scheduling system that generates personalized daily schedules by combining three critical factors that traditional planners ignore:

- **Deadline Urgency** - Time-sensitive prioritization
- **Energy Levels** - Peak performance windows throughout the day
- **Cognitive Load** - Task complexity matched to available mental capacity

Instead of treating all tasks equally, Momentum dynamically ranks and schedules work to maximize productivity while minimizing burnout. The system recognizes that people don't fail because they don't know their deadlines—they fail because they plan without accounting for energy and cognitive load.

---

## Key Features

### Intelligent Task Prioritization
- **Dynamic Ranking Algorithm** that weighs deadline urgency, task priority, and current energy levels
- Real-time score calculation considering time-to-deadline (overdue, 1 day, 3 days, 7 days+)
- Energy-task matching to assign high-energy tasks during peak hours

### Personalized Energy Profiling
- User-defined **peak performance hours** for demanding work
- Configurable **low-energy windows** for lighter tasks
- Daily capacity tracking to prevent overcommitment

### Smart Scheduling Engine
- Automated time block allocation based on task duration and energy requirements
- Capacity-aware scheduling that respects daily work limits
- Energy compatibility checking (HIGH/MEDIUM/LOW matching)

### Persistent Data Management
- JSON-based storage for tasks and user profiles
- Simple CRUD operations for task management
- Clean separation of data and business logic

---

## Architecture & Design

### System Components

```
┌─────────────────────────────────────────────────────────┐
│                        Main.py                          │
│              (CLI Interface & Orchestration)            │
└────────────┬────────────────────────────────────────────┘
             │
    ┌────────┴────────┬──────────────┬──────────────┐
    │                 │              │              │
┌───▼────┐    ┌──────▼─────┐  ┌────▼─────┐  ┌────▼────┐
│ Task   │    │User Profile│  │ Storage  │  │ Energy  │
│ Model  │    │   Model    │  │ Layer    │  │  Model  │
└───┬────┘    └──────┬─────┘  └────┬─────┘  └────┬────┘
    │                │              │              │
    └────────┬───────┴──────────────┴──────────────┘
             │
    ┌────────▼────────────────────────────┐
    │      Priority Engine                │
    │  (Task Ranking & Scoring Logic)     │
    └────────┬────────────────────────────┘
             │
    ┌────────▼────────────────────────────┐
    │         Scheduler                   │
    │  (Time Block Allocation Algorithm)  │
    └─────────────────────────────────────┘
```

### Object-Oriented Design

| Module | Responsibility | Key Methods |
|--------|---------------|-------------|
| **`task.py`** | Task entity with validation | `validate()` - Ensures data integrity |
| **`user_profile.py`** | User energy patterns & capacity | `validate()` - Validates profile constraints |
| **`energy_model.py`** | Current energy level detection | `energy_meter()` - Returns HIGH/MEDIUM/LOW |
| **`priority_engine.py`** | Task ranking algorithm | `rank_tasks()` - Scores & sorts by importance |
| **`scheduler.py`** | Time slot allocation | `create_daily_schedule()` - Assigns time blocks |
| **`storage.py`** | Data persistence layer | `save_tasks()`, `load_tasks()` |
| **`main.py`** | CLI orchestration | User interface & workflow coordination |

---

## Getting Started

### Prerequisites

```bash
Python 3.8 or higher
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/Momentum.git
cd Momentum
```

2. **Ensure data directory exists**
```bash
mkdir -p data
touch data/tasks.json data/user_profile.json
```

3. **Initialize data files** (add empty arrays)
```bash
echo "[]" > data/tasks.json
echo "{}" > data/user_profile.json
```

### Running the Application

```bash
python main.py
```

---

## Usage Guide

### Step 1: Create Your Energy Profile

First-time users must configure their personal energy patterns:

```
Choose option: 3
Enter peak hours (comma-separated, e.g., 9,10,11): 9,10,11,15,16
Enter low energy hours (comma-separated, e.g., 14,15,16): 13,14,20,21
Enter daily capacity in minutes: 360
```

**What This Does:**
- Defines when you're most productive (peak hours)
- Identifies your low-energy windows
- Sets a realistic daily work limit (6 hours = 360 minutes)

### Step 2: Add Tasks

```
Choose option: 1
Enter task title: Finish Python Project
Enter task priority (LOW, MEDIUM, HIGH): HIGH
Enter energy required (LOW, MEDIUM, HIGH): HIGH
Enter task deadline (YYYY-MM-DD HH:MM): 2026-02-05 18:00
Enter estimated duration (in minutes): 120
```

**Task Properties:**
- **Priority**: Importance level (affects ranking score)
- **Energy Required**: Cognitive load (HIGH = complex work)
- **Deadline**: Used for urgency calculation
- **Duration**: Must fit within daily capacity

### Step 3: View Today's Schedule

```
Choose option: 2

Today's Schedule

Task: 1.
Finish Python Project
Time: 09:15 → 11:15

Task: 2.
Review Meeting Notes
Time: 11:15 → 11:45

Task: 3.
Email Responses
Time: 13:30 → 14:00
```

**Scheduling Logic:**
- Tasks are ordered by priority score
- High-energy tasks scheduled during peak hours
- Respects daily capacity limits
- Prevents schedule overload

---

## Algorithm Details

### Priority Scoring System

```python
score = base_priority + energy_match + urgency_bonus

# Base Priority (1-3 points)
LOW = 1, MEDIUM = 2, HIGH = 3

# Energy Match (+2 points)
if task.energy_required == current_energy:
    score += 2

# Urgency Bonus (1-5 points)
overdue        → +5
≤ 1 day        → +4
≤ 3 days       → +3
≤ 7 days       → +2
> 7 days       → +1
```

### Scheduling Constraints

1. **Energy Compatibility**: Task energy ≤ Current energy level
2. **Capacity Check**: Task duration ≤ Remaining daily capacity
3. **Sequential Allocation**: Tasks assigned in priority order
4. **Time Block Creation**: Start time → End time calculated from duration

---

## Technical Highlights

### Clean Code Principles
- **Single Responsibility**: Each class handles one concern
- **Data Validation**: Input validation at entity level
- **Separation of Concerns**: Storage, logic, and UI are decoupled
- **Extensibility**: Easy to add new ranking criteria or scheduling rules

### Data Flow
```
User Input → Task/Profile Objects → Storage (JSON) 
                                       ↓
                                   Data Loading
                                       ↓
                        Priority Engine (Scoring & Ranking)
                                       ↓
                          Scheduler (Time Allocation)
                                       ↓
                               CLI Display
```

### Error Handling Features
- Task validation prevents invalid data entry
- Profile validation ensures logical constraints
- Status tracking (PENDING, COMPLETED, SKIPPED)
- Datetime parsing with format specification

---

## Project Structure

```
Momentum/
├── main.py                 # Entry point & CLI interface
├── task.py                 # Task entity with validation
├── user_profile.py         # User energy profile model
├── energy_model.py         # Energy level calculator
├── priority_engine.py      # Task ranking algorithm
├── scheduler.py            # Time block allocation engine
├── storage.py              # JSON data persistence
├── data/
│   ├── tasks.json          # Task storage
│   └── user_profile.json   # User preferences
├── LICENSE                 # MIT License
└── README.md               # This file
```

---

## Learning Outcomes

This project demonstrates proficiency in:

- **Object-Oriented Design** - Modeling real-world entities with proper encapsulation
- **Algorithm Development** - Creating scoring and scheduling heuristics
- **Data Persistence** - JSON serialization and file I/O
- **CLI Development** - Building interactive command-line interfaces
- **Problem Decomposition** - Breaking complex problems into manageable modules
- **Code Organization** - Maintainable architecture with clear responsibilities

---

## Future Enhancements

- [ ] **Task Dependencies** - Enable prerequisite relationships between tasks
- [ ] **Weekly Planning** - Multi-day scheduling with rollover
- [ ] **Analytics Dashboard** - Completion rates and productivity insights
- [ ] **API Integration** - Calendar sync (Google Calendar, Outlook)
- [ ] **Machine Learning** - Learn user patterns to refine energy predictions
- [ ] **Web Interface** - Modern UI with drag-and-drop scheduling
- [ ] **Notifications** - Task reminders and deadline alerts
- [ ] **Collaboration** - Team scheduling and shared tasks

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss proposed changes.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

**Mehedi Mostafa**

- GitHub: [@mehedimostafa](https://github.com/mehedimostafa)
- Project Link: [https://github.com/mehedimostafa/Momentum](https://github.com/mehedimostafa/Momentum)

---

## Acknowledgments

- Inspired by the need for **realistic task planning** that accounts for human energy fluctuations
- Built to solve the common problem of **over-scheduling** and **burnout**
- Designed with **productivity research** principles in mind

---

## Upcoming Upgrades

### Version 2.0 Roadmap

The following features are currently in development and will be released in upcoming versions:

#### Q1 2026
- **Task Completion Tracking** - Mark tasks as completed and view completion history
- **Task Editing & Deletion** - Modify or remove existing tasks from the schedule
- **Recurring Tasks** - Support for daily, weekly, and monthly repeating tasks
- **Export Functionality** - Export schedules to CSV or iCalendar format

#### Q2 2026
- **SQLite Database Integration** - Migrate from JSON to relational database for better scalability
- **Task Dependencies** - Define prerequisite relationships between tasks
- **Multi-day Planning** - Weekly and monthly schedule generation with task rollover
- **Energy Analytics** - Track actual vs. predicted energy levels to improve accuracy

#### Q3 2026
- **Web Dashboard** - Browser-based interface with drag-and-drop scheduling
- **REST API** - Enable third-party integrations and mobile app development
- **Calendar Synchronization** - Two-way sync with Google Calendar and Outlook
- **Smart Notifications** - Email and push notifications for upcoming deadlines

#### Q4 2026
- **Machine Learning Integration** - Adaptive energy prediction based on historical patterns
- **Collaboration Features** - Share tasks and schedules with team members
- **Mobile Applications** - Native iOS and Android apps
- **Voice Commands** - Add tasks and check schedules via voice interface

### Community Feature Requests

We're actively collecting feedback from users. Requested features under consideration:
- Pomodoro timer integration
- Focus mode with distraction blocking
- Habit tracking alongside task management
- Integration with project management tools (Trello, Asana, Jira)
- Dark mode for the web interface
- Custom energy pattern templates

For feature requests or to contribute to development, please visit our [GitHub Issues](https://github.com/mehedimostafa/Momentum/issues) page.

---

<div align="center">

**If you find this project useful, please consider giving it a star on GitHub.**

Developed by Mehedi Mostafa | 2026

</div>
