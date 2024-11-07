class Product:
    name = str
    weight = float
    category = str
    def __init__(self, name : str, weight : float, category : str):
        self.name = name
        Product.name = self.name
        self.weight = weight
        Product.weight = self.weight
        self.category = category
        Product.category = self.category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'
    _products = None

    def get_products(self):
        self.__file_name = open(Shop.__file_name, 'r')
        Shop._products = self.__file_name.read()
        self.__file_name.close()
        return f'{Shop._products}'

    def add(self, *products):
        for p in products:
            Shop.get_products(self)
            if p.name and str(p.weight) not in Shop._products:
                self.__file_name = open(Shop.__file_name, 'a')
                Shop._products = self.__file_name.write(f'{p.name}, {p.weight}, {p.category}\n')
                self.__file_name.close()
            else:
                print(f'Продукт {p} уже есть в магазине')
        return Shop._products


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
