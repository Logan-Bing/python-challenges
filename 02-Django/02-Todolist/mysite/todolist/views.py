from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Task


class TaskCreateView(CreateView):
    model = Task
    fields = ["name", "description", "status", "priority", "deadline", "category"]
    template_name = "todolist/new_task.html"
    success_url = reverse_lazy("todolist:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



def landing(request):
    return render(request, "todolist/landing.html")

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "todolist/home.html", {"tasks": tasks})

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("todolist:home")
    template_name = "todolist/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('todolist:home')
        else:
            messages.success(request, "error")
            return redirect('todolist:login')

    return render(request, "todolist/login.html")

def logout_user(request):
    logout(request)
    return redirect('todolist:landing')
