from random import choices

from django.db import models


# ако искаме на  department да знаем кога е направено и кога е променено
class AuditEntity(models.Model):
    # при създаване да се добави автоматично
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    # да се променя този запис това да става автоматично
    updated_on = models.DateTimeField(
        auto_now=True,
    )

    # abstract = True, значи че горните полета ще се пренесат долу
    class Meta:
        abstract = True
    # и сега трябя да се наследи къдеъо искаме - департмент


# one to many
# class Department(models.Model):
class Department(AuditEntity):
    name = models.CharField(
        max_length=20,
    )

    # показва името на департмент т.е  не стои дефоут
    def __str__(self):
        return self.name


class Employees(models.Model):
    # job_titles
    SOFTWARE_DEVELOPER = 1
    QA_ENGINEER = 2
    DEVOPS_SPECIALIST = 3

    # companies
    SOFT_UNI = 'SoftUni'
    GOOGLE = 'Google'
    FACEBOOK = 'Facebook'

    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        # за да може да стой празна фамилията трябва да използваме blank
        default='NO NAME'
    )
    egn = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='EGN',
    )
    # choices (tuple ot list with two values) We can choose ONLY between these values!!!
    # job_title = models.IntegerField(
    # choices=(
    #     # в базата стои 1, но в сайта - Software Developer
    #     # !!! нова ни прави валидация на ниво Django!!!, в базата можем да слагаме и стойности, които нямаме
    #     (1, 'Software Developer'),
    #     (2, 'Software Engineer'),
    #     (3, 'DevOps Specialist')
    # )
    job_title = models.IntegerField(
        choices=(
            (SOFTWARE_DEVELOPER, 'Software Developer'),
            (QA_ENGINEER, 'QA_engineer'),
            (DEVOPS_SPECIALIST, 'DevOps Specialist'),
        )
    )

    company = models.CharField(
        max_length=max(len(c) for c in [SOFT_UNI, GOOGLE, FACEBOOK]),
        choices=(
            (SOFT_UNI, SOFT_UNI),
            (GOOGLE, GOOGLE),
            (FACEBOOK, FACEBOOK)
        )
    )
    # ForeignKey - две задължителни неща: 1 модела към който е ForeignKey, 2. on_delete
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    class Meta:
        # пиша си по какво да сортира, ако искам в обратен ред даваме "-"
        ordering = ('company', '-first_name',)


# one to one
class User(models.Model):
    email = models.EmailField()
    employee = models.OneToOneField(
        Employees,
        on_delete=models.CASCADE,
        primary_key=True,
    )


# many to many
class Project(models.Model):
    name = models.CharField(
        max_length=30,
    )
    dead_line = models.DateField(
        null=True,
        blank=True,
    )
    employees = models.ManyToManyField(
        to=Employees,
    )
