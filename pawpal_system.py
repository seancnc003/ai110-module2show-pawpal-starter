from dataclasses import dataclass, field


@dataclass
class Task:
    description: str
    duration: float
    priority: int
    due_time: str
    completed: bool = False

    def toggle_complete(self):
        """Toggle the task's completion status."""
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

    def generate_plan(self) -> list[Task]:
        """Filter completed tasks and sort remaining by due time."""
        all_tasks = self.owner.get_all_tasks()
        incomplete = [task for task in all_tasks if not task.completed]
        sorted_tasks = sorted(incomplete, key=lambda task: task.due_time)
        return sorted_tasks

    def explain_plan(self, plan: list[Task]) -> str:
        """Return a formatted string explaining the scheduled plan."""
        if not plan:
            return "No tasks to schedule."
        lines = []
        for i, task in enumerate(plan, 1):
            lines.append(f"{i}. {task.description} (due: {task.due_time}, duration: {task.duration} min, priority: {task.priority})")
        return "\n".join(lines)
