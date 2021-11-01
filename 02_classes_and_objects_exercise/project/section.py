#from project.task import Task
#from task import Task
from project.task import Task


class Section:
    def __init__(self, name:str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_tasks = 0
        for task_object in self.tasks:
            if task_object.completed:
                self.tasks.remove(task_object)
                removed_tasks += 1
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        result_string = f"Section {self.name}:"
        for task_object in self.tasks:
            result_string += f"\n{task_object.details()}"
        return result_string


