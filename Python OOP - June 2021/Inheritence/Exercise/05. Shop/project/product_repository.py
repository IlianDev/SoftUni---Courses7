from project.product import Product


class ProductRepository:
    products = []

    def add(self, product):
        self.products.append(product.name)

    def find(self, product_name):
        return f"{product_name.name}"

    def remove(self, product_name):
        ProductRepository.products.remove(product_name.name)

    def __repr__(self):
        for i in ProductRepository.products:
            return f"{i}: {Product.__name__}"


