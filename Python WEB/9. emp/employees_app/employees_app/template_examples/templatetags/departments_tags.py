from django import template

from employees_app.employees.models import Department

register = template.Library()


@register.inclusion_tag('tags/departments_list.html')  # малко view с малък темплейт
# резултатът он inclusion_tag е просто контекста, който искаме да има
# това са преизползвамеми конпоненти
def departments_list():
    departments = Department.objects.all()

    # context
    return {
        'departments': departments
    }
