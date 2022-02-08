from django.urls import path
from DjangoProject1.task.views import home

urlpatterns = (
    path('', home),
)