from dataclasses import dataclass, field


@dataclass
class Pet:
    name: str
    animal_type: str


@dataclass
class Task:
    task_type: str
    duration: int
    priority: int
    pet: Pet


class Owner:
    def __init__(self, name: str, time_available: int = 0):
        self.name = name
        self.time_available = time_available
        self.pets: list[Pet] = []
        self.tasks: list[Task] = []

    def add_pet(self, pet: Pet):
        pass

    def remove_pet(self, pet: Pet):
        pass

    def add_task(self, task: Task):
        pass

    def remove_task(self, task: Task):
        pass


class Scheduler:
    def generate_plan(self, tasks: list[Task], time_available: int) -> list[Task]:
        pass

    def explain_plan(self, plan: list[Task]) -> str:
        pass
