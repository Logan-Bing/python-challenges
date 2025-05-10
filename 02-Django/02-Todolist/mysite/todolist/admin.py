from django.contrib import admin
from .models import Task, Category

class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'priority', 'deadline']
    list_filter = ['status', 'priority', 'category', 'user']
    search_fields = ['name', 'description']


admin.site.register(Task, TaskAdmin)
admin.site.register(Category)
