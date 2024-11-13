from django.db import models

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)  # Auto-incremented ID for each task
    description = models.TextField()
    deadline = models.DateField()
    priority = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    intern = models.ForeignKey(
        'Intern', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name="tasks"  # Optional: to access related tasks for an intern
    )

    def __str__(self):
        return f"Task {self.task_id}: {self.description[:20]}..."

class Intern(models.Model):
    intern_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class CryptoProject(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    contact_info = models.EmailField(max_length=100, blank=True, null=True)
    market_cap = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    volume = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name

class Outreach(models.Model):
    outreach_id = models.AutoField(primary_key=True)
    intern = models.ForeignKey(
        'Intern', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="outreach_activities"  # Optional: to access outreach activities for an intern
    )
    project = models.ForeignKey(
        'CryptoProject', 
        on_delete=models.CASCADE, 
        related_name="outreaches"  # Optional: to access all outreaches for a project
    )
    date = models.DateField()
    method = models.CharField(max_length=50)
    response = models.TextField(blank=True, null=True)
    followup = models.DateField(blank=True, null=True)

    def __str__(self):
        intern_name = self.intern.name if self.intern else 'Unknown'
        return f"{self.project.name} Outreach on {self.date} by {intern_name}"
