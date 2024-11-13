from django.db import models
from django.conf import settings

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)  # Auto-incremented ID for each task
    description = models.TextField()
    deadline = models.DateField()
    priority = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    intern = models.ForeignKey('Intern', on_delete=models.CASCADE, null=True, blank=True)  # Link to Intern

    def __str__(self):
        return f"Task {self.task_id}: {self.description[:20]}..."  # Improved __str__ for clarity

class Intern(models.Model):
    intern_id = models.AutoField(primary_key=True)  # Auto-incremented ID for each intern
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)  # Ensures each email is unique

    def __str__(self):
        return self.name

class CryptoProject(models.Model):
    project_id = models.AutoField(primary_key=True)  # Auto-incremented ID for each project
    name = models.CharField(max_length=100, unique=True)  # Unique name for each project
    website = models.URLField(max_length=200, blank=True, null=True)  # Optional website URL
    contact_info = models.EmailField(max_length=100, blank=True, null=True)  # Optional contact email
    market_cap = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)  # Market cap in USD or other currency
    volume = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)  # Trading volume in USD or other currency

    def __str__(self):
        return self.name

class Outreach(models.Model):
    outreach_id = models.AutoField(primary_key=True)  # Primary Key
    intern = models.ForeignKey('Intern', on_delete=models.SET_NULL, null=True, blank=True)  # Link to your Intern model
    project = models.ForeignKey('CryptoProject', on_delete=models.CASCADE)  # Links to CryptoProject
    date = models.DateField()  # Date of the outreach
    method = models.CharField(max_length=50)  # Method of outreach, e.g., email, call
    response = models.TextField(blank=True, null=True)  # Response from outreach
    followup = models.DateField(blank=True, null=True)  # Date for follow-up if needed

    def __str__(self):
        intern_name = self.intern.name if self.intern else 'Unknown'
        return f"{self.project.name} Outreach on {self.date} by {intern_name}"
