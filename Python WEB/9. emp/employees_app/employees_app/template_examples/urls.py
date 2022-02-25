from django.urls import path

from employees_app.template_examples.views import index1

urlpatterns = (
    path('', index1, name='templates.index.html'),
)