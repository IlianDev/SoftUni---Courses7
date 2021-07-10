class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name):
        if self.name != new_name:
            self.name = new_name
            return new_name
        else:
            return f"Name cannot be the same."

    def change_due_date(self, new_date):
        if self.due_date != new_date:
            self.due_date = new_date
            return new_date
        else:
            return f"Date cannot be the same."

    def add_comment(self, comment):
        self.comments.append(comment)

    def edit_comment(self, comment_number, new_comment):
        if IndexError:
            return "Cannot find comment."
        else:
            self.comments[comment_number] = new_comment
            return f"{f', '.join(self.comments)}"

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"


