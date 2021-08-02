# from project.animals.animal import Bird
#
#
# class Owl(Bird):
#     FOOD = {"meat"}
#     WEIGHT_INCREASE = 0.25
#
#     def __init__(self, name, weight, wing_size):
#         super().__init__(name, weight, wing_size)
#
#     def make_sound(self):
#         return "Hoot Hoot"
#
#     def feed(self, food):
#         type_food = food.__class__.__name__
#         if type(food) not in Owl.FOOD:
#             return f"{self.__class__.__name__} does not eat {type_food}!"
#
#         self.weight += food.quantity * Owl.WEIGHT_INCREASE
#         self.food_eaten += food.quantity
#
#
# class Hen(Bird):
#     FOOD = {"vegetables", 'Fruit', 'Meat', 'Seed'}
#     WEIGHT_INCREASE = 0.35
#
#     def __init__(self, name, weight, wing_size):
#         super().__init__(name, weight, wing_size)
#
#     def make_sound(self):
#         return f"Cluck"
#
#     def feed(self, food):
#         type_food = food.__class__.__name__
#         if type(food) not in Hen.FOOD:
#             return f"{self.__class__.__name__} does not eat {type_food}!"
#
#         self.weight += food.quantity * Hen.WEIGHT_INCREASE
#         self.food_eaten += food.quantity
