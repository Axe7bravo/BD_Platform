from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import CryptoProject, Outreach, Task
from .forms import CryptoProjectForm, CustomUserCreationForm
from .forms import TaskForm
# Registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, "Registration successful!")
            return redirect('crypto_list')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('crypto_list')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid login credentials.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# List view for displaying crypto projects
class CryptoProjectListView(ListView):
    model = CryptoProject
    template_name = 'crypto/crypto_project_list.html'  
    context_object_name = 'crypto_project'

#Create view for adding a new task
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new task to the database
            return redirect('task_list')  # Redirect to the task list page
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

# Detail view for task list
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

# Create view for adding a new crypto project
class CryptoProjectCreateView(CreateView):
    model = CryptoProject
    form_class = CryptoProjectForm
    template_name = 'crypto/crypto_create.html'  
    success_url = reverse_lazy('crypto_project_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Crypto project successfully added!")
        return response

# Update view for updating an existing crypto project
class CryptoProjectUpdateView(UpdateView):
    model = CryptoProject
    form_class = CryptoProjectForm
    template_name = 'crypto/crypto_update.html' 
    success_url = reverse_lazy('crypto_project_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Crypto project successfully updated!")
        return response

# Delete view for deleting a crypto project
class CryptoProjectDeleteView(DeleteView):
    model = CryptoProject
    template_name = 'crypto/crypto_delete.html'  
    success_url = reverse_lazy('crypto_project_list')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Crypto project successfully deleted!")
        return response

# View for listing outreach by project
def project_outreach_list(request, project_id):
    project = get_object_or_404(CryptoProject, id=project_id)
    outreach_list = Outreach.objects.filter(project=project)
    return render(request, 'crypto/outreach_list.html', {'project': project, 'outreach_list': outreach_list})

