from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView

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
