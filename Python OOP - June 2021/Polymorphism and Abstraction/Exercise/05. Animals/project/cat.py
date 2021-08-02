from typing import ClassVar
from project.animal import Animal


class Cat(Animal):
    _SOUND: ClassVar[str] = 'Meow meow!'
