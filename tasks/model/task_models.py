from django.db import models
from django.contrib.auth.models import User
from photo_models import Photo


class Task(models.Model):
    PRIORITY_CHOICES = (
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    priority = models.CharField(
        max_length=6, choices=PRIORITY_CHOICES, default="medium"
    )
    completed = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    # Relations
    owner = ForeignKey("User", on_delete=CASCADE, related_name="tasks")

    photos = OneToManyField(Photo, related_name="task", blank=True)

    def __str__(self):
        return self.title


# class Photo(models.Model):
#     image = models.ImageField(upload_to='task_photos')
#     caption = models.CharField(max_length=255, blank=True)
#     upload_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.image.name
