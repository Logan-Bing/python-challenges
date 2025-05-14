from django.urls import path
from . import views
from .views import SignUpView, TaskCreateView

app_name = 'todolist'

urlpatterns = [
    path('', views.landing, name="landing"),
    path('home', views.home, name="home"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('signup', SignUpView.as_view(), name="signup"),
    path('new_task', TaskCreateView.as_view(), name="new_task"),
]
