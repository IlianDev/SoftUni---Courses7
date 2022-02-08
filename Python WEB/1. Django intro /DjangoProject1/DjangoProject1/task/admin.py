from django.contrib import admin
from DjangoProject1.task.models import Task


# Variant 1
# admin.site.register(Task)

# Variant 2
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')  # това ми дава готово сортиране в джанго
    list_filter = ('title',)  # sortira po title
