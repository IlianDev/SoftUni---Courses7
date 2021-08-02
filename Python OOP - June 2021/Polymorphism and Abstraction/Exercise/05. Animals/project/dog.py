from typing import ClassVar
from project.animal import Animal


class Dog(Animal):
    _SOUND: ClassVar[str] = 'Woof!'