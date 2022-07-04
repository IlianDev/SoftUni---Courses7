from django.contrib import admin

# Register your models here.
from employees_app.employees.models import Employees, Department


@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    # list_display - с лист дисплей, ако стартирам без него джанго се показва без полонки (например само ако сложа pass)
    list_display = ('id', 'first_name', 'last_name',
                    'job_title', 'company',)
    # pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


