"""employees_app URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from employees_app.employees.views import home, department_details, go_to_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index.html'),
    # path('department/', department_details),
    path('go-to-home/', go_to_home, name='go to home'),
    path('departments/', include('employees_app.employees.urls')),
    path('templates/', include('employees_app.template_examples.urls')),

    # path('departments/1/', department_details),
    # path('departments/', list_departments),
    # path('departments/create/', create_department),
    # path('departments/update/', update_department'),
    # path('departments/delete/', delete_department')
    # we use include
    # we can use seperating urls to avoid repeating...
    # това дава грешка, че Джанго се опитва да вземе юрл конфигурацията но не я намира
    # Как дефинираме url конфигурация с urlpatterna
    # path('', include('employees_app.employees.urls')), - празен път

]
