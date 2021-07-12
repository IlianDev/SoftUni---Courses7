from project_food.food import Food


class Fruit(Food):
    def __init__(self, name=str, expiration_date=str):
        super().__init__(expiration_date)
        self.name = name

# kato dadem na papkata Inheritance_lab_ex desen buton mark as root и импортжаме после само от нея по бързо достъпване