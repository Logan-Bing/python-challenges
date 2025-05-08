from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index" ),
    path('<int:article_id>/', views.detail, name="detail"),
    path('<int:article_id>/comment/', views.add_comment, name="comment" ),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name="edit_comment"),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name="delete_comment")
]
