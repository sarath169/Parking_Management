from django.conf.urls import url
from operators import views as core_views
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'operators'
urlpatterns = [
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    url(r'^signup/$', core_views.signup, name='signup'),
]