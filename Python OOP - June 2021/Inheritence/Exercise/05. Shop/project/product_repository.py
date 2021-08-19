from project.product import Product


class ProductRepository:
    products = []

    def add(self, product):
        self.products.append(product.name)

    def find(self, product_name):
        for prod in self.products:
            if prod.name == product_name:
                return prod

    def remove(self, product_name):
        for prod in self.products:
            if prod.name == product_name:
                self.products.remove(prod)

    def __repr__(self):
        for i in ProductRepository.products:
            return f"{i}: {Product.__name__}"
