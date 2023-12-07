from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')  # Fields to display in the list view
    list_filter = ['title']  # Filters you can use on the side
    search_fields = ['title', 'description']  # Fields to search in

# Register your models here.
admin.site.register(Task)