# from django.http import HttpResponse
from django.shortcuts import render


#
# from DjangoProject1.task.models import Task
#
#
# # t = task
# def home(request):
#     items = Task.objects.all()
#     item_strings = (f'<li>{t.title}</li>' for t in items)
#     items_string = ''.join(item_strings)
#     html = f'''
# <h1>It works!</h1>
# <ul>
#     {items_string}
# </ul>
#     '''
#     return HttpResponse(html)

# za da imame view trqbva da imame funckiq s parametyr
# pravi syshtoto kato gore, obache idwa ot template
def home(request):
    return render(request, "home.html")
