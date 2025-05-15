from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import TaskForm

from ..models import Task

class TaskDetailView(DetailView):
    model = Task

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = "todolist/new_task.html"
    success_url = reverse_lazy("todolist:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todolist/task_update_form.html"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)



@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "todolist/home.html", {"tasks": tasks})
