from random import choices

from django.db import models

# за да можем обаче да четем sql  заявките е хубаво да си настроим logging
# Model - базовия клас за създаване на модели, базовия клас за създаване на модели, таблици, това което ни дава е
# repr(), str(), i tn. В момента, които стартираме проетка джанго търси всички класове, които наследяват модел
# и ги регистрита така че ние да можем да правим sql заявки (да пишем код, който генерира sql заявки)
#

"""
как се използва prymary_key. рядко се използва освен ако не искаме да сменим някоя ид на някоя таблица
"""


class TestModel(models.Model):
    id2 = models.IntegerField(
        auto_created=True,
        primary_key=True,
    )


# Relations
"""
Как да направим връзката? Искаме едно department да има много employees
Oтдолу в employees си декларираме department = models.foreignKey(...) 
"""


class Department(models.Model):
    name = models.CharField(
        max_length=20,
    )


class Employee(models.Model):
    # Jobs:
    SOFTWARE_DEVELOPER = 1
    QA_ENGINEER = 2
    DevOps_SPECIALIST = 3

    # Companies:
    SOFT_UNI = 'Soft_Uni'
    GOOGLE = 'Google'
    FACEBOOK = 'Facebook'

    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        # it can have null values. НО null не означава празен стринг
        # това идва от Django, не от базата, което изначава когато не подадем нищо иамем None
        max_length=40,
        null=True,
        blank=True,
        default='No name',
    )
    EGN = models.CharField(
        max_length=10,
        unique=True,  # уникален не може да е повтаря
        verbose_name='EGN'  # как искаме да изглежда дефолтния лейбъл примерно. Ако сме г
        # задали с малки букви да искаме в сайта да излиза с големи.
    )

    # choices - решаваме че job_title не искаме да е отделна таблица с която да има връзка
    # ами искаме да е част от. Джанго ми дава възможност да му задам възможни стойностти, които мога да ги
    # избирам - choices.
    # choices - представлява, тюпъл или списък от тюпълчета с по две стойности.
    # като използвайки модела employees, валидните стойности са само измежду тези които съм декларирал в
    # choices. това като го стартирам виждам, че ми позволява да си избирам в админската част.

    # job_title = models.CharField(
    #     max_length=40,
    #     choices=(
    #         ('Software engineer', 1),
    #         ('QA engineer', 2),
    #         ('DevOps specialist', 3),
    #     )
    # )
    # но това по скоро се прави като се декларират горе в класа Employee
    # job_title = models.IntegerField(
    #     choices=(
    #         # 1 - стойността в базата, другото е как изглежа
    #         (1, 'Software engineer'),
    #         (2, 'QA engineer'),
    #         (3, 'DevOps specialist'),
    #     )
    # )

    # TAKA е по добре
    job_title = models.IntegerField(
        choices=(
            # 1 - стойността в базата, другото е как изглежа
            # тука нарочно ги направихме int i str
            (SOFTWARE_DEVELOPER, 'Software engineer'),
            (QA_ENGINEER, 'QA engineer'),
            (DevOps_SPECIALIST, 'DevOps specialist'),
        )
    )
    # така наи лесно се слага max_length=
    company = models.CharField(
        max_length=max(len(c) for c in [SOFT_UNI, GOOGLE, FACEBOOK]),
        choices=(
            # така е препоръчително едни и същи
            (SOFT_UNI, SOFT_UNI),
            (GOOGLE, GOOGLE),
            (FACEBOOK, FACEBOOK),
        )
    )
    # Имаме cascade, do nothing, restrict
    # delete - означава като изтрием department,  всички, employees които са в този департмен също да ги изтрием
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )
