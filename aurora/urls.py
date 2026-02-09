from django.urls import path
from . import views

app_name = "aurora"

urlpatterns = [
    path("", views.aurora_home, name="aurora_home"),
    path('log-activity/', views.log_aurora_activity, name='log_aurora_activity'),

]