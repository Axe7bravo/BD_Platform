from django.contrib import admin
from .models import Task, Intern, CryptoProject, Outreach

# Inline admin for the Task model, as it is linked to Intern
class TaskInline(admin.TabularInline):
    model = Task
    extra = 1  # Number of empty forms to show
    fields = ('description', 'deadline', 'priority', 'status')

# Inline admin for the Outreach model, as it is linked to both Intern and CryptoProject
class OutreachInline(admin.TabularInline):
    model = Outreach
    extra = 1  # Number of empty forms to show
    fields = ('date', 'method', 'response', 'followup')

# Customizing the admin for Task model
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'description', 'deadline', 'priority', 'status', 'intern')
    search_fields = ('description', 'intern__name')  # Searching by description and intern's name
    list_filter = ('status', 'priority', 'intern')

# Customizing the admin for Intern model
class InternAdmin(admin.ModelAdmin):
    list_display = ('intern_id', 'name', 'email')
    search_fields = ('name', 'email')
    inlines = [TaskInline, OutreachInline]  # Display tasks and outreach associated with the intern

# Customizing the admin for CryptoProject model
class CryptoProjectAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'name', 'market_cap', 'volume', 'website')
    search_fields = ('name', 'market_cap', 'volume')
    inlines = [OutreachInline]  # Display outreach associated with the project

# Customizing the admin for Outreach model
class OutreachAdmin(admin.ModelAdmin):
    list_display = ('outreach_id', 'intern', 'project', 'date', 'method', 'response')
    search_fields = ('intern__name', 'project__name', 'method')
    list_filter = ('method', 'date')
    date_hierarchy = 'date'  # Add date-based navigation

# Registering models with their respective custom admin classes
admin.site.register(Task, TaskAdmin)
admin.site.register(Intern, InternAdmin)
admin.site.register(CryptoProject, CryptoProjectAdmin)
admin.site.register(Outreach, OutreachAdmin)
