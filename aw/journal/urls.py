from django.urls import path
from . import views

app_name='journal'

urlpatterns = [
    path("new/", views.CreateEntry.as_view(), name="create"),
]
