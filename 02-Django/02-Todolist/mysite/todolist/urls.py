from django.urls import path
from .views import tasks, general, auth
from .views.tasks import TaskCreateView, TaskDetailView, TaskUpdateView
from .views.auth import SignUpView

app_name = 'todolist'

urlpatterns = [
    path('', general.landing, name="landing"),
    path('home', tasks.home, name="home"),
    path('login', auth.login_user, name="login"),
    path('logout', auth.logout_user, name="logout"),
    path('signup', SignUpView.as_view(), name="signup"),
    path('new_task', TaskCreateView.as_view(), name="new_task"),
    path('<pk>/', TaskDetailView.as_view(), name="detail_task"),
    path('<pk>/update', TaskUpdateView.as_view(), name="update_task")
]
