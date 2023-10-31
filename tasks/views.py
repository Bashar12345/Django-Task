from django.shortcuts import render

# Create your views here.



from django.views.generic import ListView
from .models import Task
from django.views.generic import DetailView
from .models import Task

from django.views.generic import CreateView
from .models import Task
from .forms import TaskForm

from django.views.generic import UpdateView
from .models import Task
from .forms import TaskForm

from django.views.generic import DeleteView
from .models import Task


#  TaskListView:
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/list.html'



# b. TaskCreateView:
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = '/tasks/'



# c. TaskDetailView:
class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/detail.html'



# d. TaskUpdateView:
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = '/tasks/'


# e. TaskDeleteView:
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = '/tasks/'