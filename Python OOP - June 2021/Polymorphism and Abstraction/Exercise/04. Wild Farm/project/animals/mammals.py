# from project.animals.animal import Mammal
#
#
# class Mouse(Mammal):
#     FOOD = {"vegetable", "fruit"}
#     WEIGHT_INCREASE = 0.10
#
#     def __init__(self, name, weight, living_region):
#         super().__init__(name, weight, living_region)
#
#     def make_sound(self):
#         return f"Squeak"
#
#     def feed(self, food):
#         type_food = food.__class__.__name__
#         if type_food not in Mouse.FOOD:
#             return f"{self.__class__.__name__} does not eat {type_food}!"
#
#         self.weight += food.quantity * Mouse.WEIGHT_INCREASE
#         self.food_eaten += food.quantity
#
#
# class Dog(Mammal):
#     FOOD = {"meat"}
#     WEIGHT_INCREASE = 0.40
#
#     def __init__(self, name, weight, living_region):
#         super().__init__(name, weight, living_region)
#
#     def make_sound(self):
#         return f"Woof!"
#
#     def feed(self, food):
#         type_food = food.__class__.__name__
#         if type_food not in Dog.FOOD:
#             return f"{self.__class__.__name__} does not eat {type_food}!"
#
#         self.weight += food.quantity * Dog.WEIGHT_INCREASE
#         self.food_eaten += food.quantity
#
#
# class Cat(Mammal):
#     FOOD = {"vegetables", "meat"}
#     WEIGHT_INCREASE = 0.30
#
#     def __init__(self, name, weight, living_region):
#         super().__init__(name, weight, living_region)
#
#     def make_sound(self):
#         return f"Meow"
#
#     def feed(self, food):
#         type_food = food.__class__.__name__
#         if type_food not in Cat.FOOD:
#             return f"{self.__class__.__name__} does not eat {type_food}!"
#
#         self.weight += food.quantity * Cat.WEIGHT_INCREASE
#         self.food_eaten += food.quantity
#
#
# class Tiger(Mammal):
#     FOOD = {"vegetables", "meat"}
#     WEIGHT_INCREASE = 1.00
#
#     def __init__(self, name, weight, living_region):
#         super().__init__(name, weight, living_region)
#
#     def make_sound(self):
#         return f"ROAR!!!"
#
#     def feed(self, food):
#         type_food = food.__class__.__name__
#         if type_food not in Tiger.FOOD:
#             return f"{self.__class__.__name__} does not eat {type_food}!"
#
#         self.weight += food.quantity * Tiger.WEIGHT_INCREASE
#         self.food_eaten += food.quantity
