# трябва да се казва точно така
from django.urls import path

from employees_app.employees.views import \
    department_details, \
    list_departments, not_found, go_to_home, create_department

urlpatterns = (
    path('create/', create_department),
    # path('1/', department_details),
    path('<int:id>/', department_details, name='department details'),
    path('', list_departments, name='list departments'),  # departments/id/ =>
    # path('departments/create/', create_department),
    # path('departments/update/', update_department'),
    # path('departments/delete/', delete_department')
    path('not-found/', not_found),  # получаваме 404 грешка


)
