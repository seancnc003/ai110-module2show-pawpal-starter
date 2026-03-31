from dataclasses import dataclass, field
from datetime import datetime, timedelta


@dataclass
class Task:
    description: str
    duration: float
    priority: int
    due_time: str
    frequency: str = "none"
    completed: bool = False

    def toggle_complete(self):
        """Toggle completion. Recurring tasks auto-advance to the next due date."""
        if not self.completed and self.frequency != "none":
            current = datetime.strptime(self.due_time, "%Y-%m-%d %H:%M")
            if self.frequency == "daily":
                next_due = current + timedelta(days=1)
            elif self.frequency == "weekly":
                next_due = current + timedelta(weeks=1)
            self.due_time = next_due.strftime("%Y-%m-%d %H:%M")
            # stays incomplete — it's a new occurrence
        else:
            self.completed = not self.completed


class Pet:
    def __init__(self, name: str, animal_type: str):
        self.name = name
        self.animal_type = animal_type
        self.tasks: list[Task] = []

    def add_task(self, task: Task):
        """Add a task to this pet."""
        self.tasks.append(task)

    def remove_task(self, task: Task):
        """Remove a task from this pet, raises ValueError if not found."""
        if task not in self.tasks:
            raise ValueError(f"Task '{task.description}' not found for pet '{self.name}'")
        self.tasks.remove(task)

    def list_tasks(self) -> list[Task]:
        """Return all tasks for this pet."""
        return self.tasks


class Owner:
    def __init__(self, name: str, time_available: int = 0):
        self.name = name
        self.time_available = time_available
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet to this owner."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet):
        """Remove a pet from this owner, raises ValueError if not found."""
        if pet not in self.pets:
            raise ValueError(f"Pet '{pet.name}' not found for owner '{self.name}'")
        self.pets.remove(pet)

    def get_all_tasks(self) -> list[Task]:
        """Collect and return all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.list_tasks())
        return all_tasks


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def sort_by_time(self, tasks: list[Task]) -> list[Task]:
        """Sort tasks by due time in HH:MM format."""
        return sorted(tasks, key=lambda task: task.due_time)

    def filter_by_pet(self, pet_name: str) -> list[Task]:
        """Return tasks belonging to a specific pet."""
        for pet in self.owner.pets:
            if pet.name == pet_name:
                return pet.list_tasks()
        return []

    def filter_by_status(self, completed: bool) -> list[Task]:
        """Return tasks filtered by completion status."""
        all_tasks = self.owner.get_all_tasks()
        return [task for task in all_tasks if task.completed == completed]

    def generate_plan(self) -> list[Task]:
        """Filter completed tasks and sort remaining by due time."""
        incomplete = self.filter_by_status(completed=False)
        return self.sort_by_time(incomplete)

    def detect_conflicts(self) -> list[str]:
        """Check for overlapping tasks and return warning messages."""
        tasks = self.generate_plan()
        warnings = []
        for i in range(len(tasks)):
            start_a = datetime.strptime(tasks[i].due_time, "%Y-%m-%d %H:%M")
            end_a = start_a + timedelta(minutes=tasks[i].duration)
            for j in range(i + 1, len(tasks)):
                start_b = datetime.strptime(tasks[j].due_time, "%Y-%m-%d %H:%M")
                if start_b < end_a:
                    warnings.append(
                        f"Conflict: '{tasks[i].description}' ({tasks[i].due_time}, {tasks[i].duration} min) "
                        f"overlaps with '{tasks[j].description}' ({tasks[j].due_time}, {tasks[j].duration} min)"
                    )
        return warnings

    def explain_plan(self, plan: list[Task]) -> str:
        """Return a formatted string explaining the scheduled plan."""
        if not plan:
            return "No tasks to schedule."
        lines = []
        for i, task in enumerate(plan, 1):
            lines.append(f"{i}. {task.description} (due: {task.due_time}, duration: {task.duration} min, priority: {task.priority})")
        return "\n".join(lines)
