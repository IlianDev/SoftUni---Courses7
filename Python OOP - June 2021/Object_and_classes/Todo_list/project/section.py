class Section:
    def __init__(self, name):
        self.name = name
        self.task = []
        self.amount = 0

    def add_task(self, new_task):
        if new_task in self.task:
            return f"Task is already in the section {self.name}"

        self.task.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name, task):
        if task_name not in self.task:
            return f"Could not find task with the name {task_name}"
        task.completed = True
        self.amount += 1
        return f"Completed task {task_name}"

    def clean_section(self, task):
        if task.completed:
            pass
            return f"Cleared {self.amount} tasks."

    def view_section(self, task):
        return f"Section {self.name}" \
               f"{task.details(self.name)}"



