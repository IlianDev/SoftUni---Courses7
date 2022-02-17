from django.http import HttpResponse, HttpResponseNotFound
import random
from django.urls import reverse_lazy

# class based view:
# from django.views.generic import TemplateView
#
#
# class HomeView(TemplateView):
#     template_name = 'index.html'


# function based views:
from django.shortcuts import redirect, render


# def home(request):
#     html = f'<h1>{request.method}: This is home</h1>'
#     # if request.method == 'Post':
#     #     return HttpResponse(
#     #         f'{request.method}: This is home',
#     #         status=201
#     #     )
#     # else:
#     #     return HttpResponse(f'{request.method}: This is home')
#     # return HttpResponseNotFound() # is the same as
#     # return HttpResponse(status=404)

def home(request):
    print(reverse_lazy('index'))
    print(reverse_lazy('go to home'))
    print(reverse_lazy('list departments'))
    print(reverse_lazy('department details', kwargs={
        'id': 1,
    }))

    rand_number = random.randint(0, 1024)
    context = {
        'number': rand_number,
    }

    return render(request, 'index.html', context)


def go_to_home(request):
    # return HttpResponseRedirect()  # няма смисъл да се прави, защото имаме shortcuts
    return redirect('department details', id=random.randint(0, 2000))


def not_found(request):
    return HttpResponseNotFound()
    #  raise http404()


def department_details(request, id):
    return HttpResponse(f'This is department {id}')


def list_departments(request):
    return HttpResponse('This is list of departments')

def create_department(request):
    return HttpResponse('Created')
