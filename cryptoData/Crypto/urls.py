from django.urls import path
from . import views
from .views import (
    CryptoProjectListView, CryptoProjectCreateView, CryptoProjectUpdateView, CryptoProjectDeleteView
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # User authentication URLs
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  

    # Crypto project management URLs
    path('', CryptoProjectListView.as_view(), name='crypto_project_list'),  
    path('tasks/', views.task_list, name='task_list'),  
    path('create/', CryptoProjectCreateView.as_view(), name='crypto_create'),  
    path('<int:pk>/update/', CryptoProjectUpdateView.as_view(), name='crypto_update'),  
    path('<int:pk>/delete/', CryptoProjectDeleteView.as_view(), name='crypto_delete'),  
    # Outreach management URL
    path('<int:project_id>/outreach/', views.project_outreach_list, name='project_outreach_list'),  
]
