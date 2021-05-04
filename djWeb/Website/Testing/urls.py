from django.urls import path
from . import views

urlpatterns = [
    path('<int:course_id>/',views.Details, name='Details'),
    path('', views.Home, name = 'home-page'),
]