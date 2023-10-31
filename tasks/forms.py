from django import forms
from .models import Task, TaskComment, TaskTag, Photo, PhotoComment, PhotoTag


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "priority"]


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "priority"]



