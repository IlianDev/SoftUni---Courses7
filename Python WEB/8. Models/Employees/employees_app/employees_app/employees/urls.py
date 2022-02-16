import path as path
from django.urls import path

from employees_app.employees.views import \
    department_details, \
    list_departments, \
    not_found

urlpatterns = (
    # localhost: 8000/department -> department /=> това искаме да се получи departments/ID
    path('<int:idd>/', department_details),
    path('', list_departments, name='list departments'),
    path('not-found/', not_found)
    # localhost: 8000/departments/departments - защото един път едното идва от urls/project а другото от urls/app
    # това е леко неудобно и начина да се реши това е като сложим празен път ''на urls/project, но по добрия начин
    # е да си ги оправим
    # path('departments/create/', create_department),
    # path('departments/update/', update_department'),
    # path('departments/delete/', delete_department')
)

# it can be empty but the app will work properly
