from django.urls import path

from . import views

app_name = 'auth_app'
urlpatterns = [
    path('', views.login_user, name='login'),
    path('home', views.home, name='home'),
    path('logout', views.logout_user, name="logout")
]
