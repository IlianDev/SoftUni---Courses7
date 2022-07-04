from django.db import models


# code-first approach
class Task(models.Model):
    title = models.CharField(
        max_length=15,
        null=False
    )
    text = models.CharField(
        max_length=150,
        null=False
    )

    def __str__(self):
        return f'{self.id}: {self.title}'
