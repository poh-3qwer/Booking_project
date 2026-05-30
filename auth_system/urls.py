from django.urls import path
from auth_system import views

urlpatterns = [
    path('register/', views.registation, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login')
]