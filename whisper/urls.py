from django.urls import path
from . import views

app_name = 'whisper'

urlpatterns = [
    path('', views.whisper_home, name='whisper_home'),
    path('log-activity/', views.log_whisper_activity, name='log_whisper_activity'),

]
