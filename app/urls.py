from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('admin/', views.admin_login, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user/', views.user_login, name='user_login'),
    path('event/', views.event, name='event'),
    path('logout/', views.logout_view, name='logout_view'),
]
