from django.db import models
from tasks.models import Task


class Photo(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    image = models.BinaryField()
    caption = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #relation
    task = ForeignKey('Task', on_delete=CASCADE)

    def __str__(self):
        return f"{self.task.title} - {self.caption}"
