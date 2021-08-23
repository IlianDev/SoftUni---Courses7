from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self):
        self.pf = PaintFactory("Test", 100)

    def test_init(self):
        pf = PaintFactory("Test", 100)
        self.assertEqual("Test", pf.name)
        self.assertEqual(100, pf.capacity)
        self.assertEqual({}, pf.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], pf.valid_ingredients)

    # add_ingredient
    def test_add_ingredient_invalid_product_type_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.pf.add_ingredient("purple", 2)
        self.assertEqual("Ingredient of type purple not allowed in PaintFactory", str(ex.exception))

    def test_add_ingredient_invalid_quantity_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.pf.add_ingredient("white", 101)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ingredient(self):
        self.assertEqual({}, self.pf.ingredients)
        self.pf.add_ingredient("white", 2)
        self.assertEqual({"white": 2}, self.pf.ingredients)

    def test_add_ingredient_already_existing_increases(self):
        self.assertEqual({}, self.pf.ingredients)
        self.pf.add_ingredient("white", 2)
        self.assertEqual({"white": 2}, self.pf.ingredients)
        self.pf.add_ingredient("white", 2)
        self.assertEqual({"white": 4}, self.pf.ingredients)

    # remove_ingredient
    def test_remove_invalid_product_type_raises(self):
        with self.assertRaises(KeyError) as ex:
            self.pf.remove_ingredient("test_type", 2)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_remove_ingredient_if_quantity_less_than_0(self):
        self.pf.add_ingredient("white", 2)
        with self.assertRaises(ValueError) as ex:
            self.pf.remove_ingredient("white", 3)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient(self):
        self.pf.add_ingredient("white", 2)
        self.pf.remove_ingredient("white", 1)
        self.assertEqual({"white": 1}, self.pf.ingredients)

    def test_product_property(self):
        self.pf.add_ingredient("white", 2)
        self.assertEqual({"white": 2}, self.pf.products)


if __name__ == '__main__':
    main()
