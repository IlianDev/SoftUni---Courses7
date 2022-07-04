from django.shortcuts import render

from employees_app.employees.models import Department, Employees


def index1(request):
    # ifchanged
    employees = [e for e in Employees.objects.order_by('Department__name', 'first_name', 'last_name').all()]

    # ако искаме да покажем данни трябва да подадем context
    context = {
        # if else
        'number_1': 123,
        'number_2': 231,
        # for tag
        'numbers': [123, 321, 200],
        # 'employees': Employees.objects.all(),
        # 'employees': Employees.objects.order_by('first_name', 'last_name').all(),

        'title': 'Employees list',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipis',
        # zaqwka kym bazata
        'department_name': [d.name for d in Department.objects.all()]
    }
    return render(request, 'templates_examples/../../templates/templates_examples/index.html', context)
