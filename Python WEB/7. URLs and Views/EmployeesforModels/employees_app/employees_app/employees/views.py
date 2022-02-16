import random

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect


# a function is Django view if:
# - accepts request param. as first parameter
# - returns HttpResponse

# def home(request):
#     html = f'<h1>{request.method}: This is home </h1>'
#     if request.method == 'POST':
#         # request.method - gives the request method we use
#         # респонсите в http имат статус кодове, примерно 200-ок. 201-created
#         return HttpResponse(
#             html,
#             content_type='application/xml',
#             headers={
#                 'x=doncho-header': 'Django',
#             },
#             # f'{request.method}: This is home',
#             # status=201
#         )
#     # else:
#     #     return HttpResponse(f'{request.method}: This is home')
#     #     # for example:
#     #     # return HttpResponseNotFound()
#     #     # == (the same)
#     # return HttpResponse(status=404)

# за да покажем index.html
# def render(request, template_name, context=None, content_type=None, status=None, using=None):
# content_type - приема че е нон, но ние можем да го сменим това. примерно:
from django.urls import reverse_lazy


def home(request):
    print(reverse_lazy('index'))
    print(reverse_lazy('go to home'))
    print(reverse_lazy('list departments'))
    # render() Context - просто можем да използваме дикт и после да го добавим в render(), kato трети параметър
    # правейки това вече в  html фаийла можем да го покажем. примерно като header2
    rand_number = random.randint(0, 2024)
    context = {
        'number': rand_number,
    }
    return render(request, 'index.html', context)


def not_found(request):
    return HttpResponseNotFound()


def department_details(request, idd):
    return HttpResponse(f'This is department {idd}')


def list_departments(request):
    return HttpResponse("This is list of departments")


def go_to_home(request):
    # като информация в () можем да му дадем инфо къде искаме да отиде
    # return HttpResponseRedirect()

    # 2.
    # това обаче не е нужно да го правим, защото в Джанго си имаме django.shortcuts
    # затова използваме:

    return redirect(to='localhost:8000')

    # return redirect('department details', id =
    #     id: random.randint(1, 1024),
    #

    # ==
    # return redirect(to='/') - it means again home page
    # с което казваме като се отвори redirect_to_home да отиде на homepage
