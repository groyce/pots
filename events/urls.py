from django.urls import path
from django.contrib.auth import views
from . import views

app_name = 'events'
urlpatterns = [
    path('', views.EventsPage, name='events'),
    path('<int:id>/', views.event_detail, name='event_detail'),
]
