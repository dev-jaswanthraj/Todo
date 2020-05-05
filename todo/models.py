from django.db import models

class todo_item(models.Model):
    content = models.CharField(max_length = 100, blank = True, null = True)

    def __str__(self):
        return self.content
