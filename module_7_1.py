class Product:
    def __init__(self, name : str, weight : float, category : str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        self._file = None

    def get_products(self):
        self._file = open(Shop.__file_name, 'r')
        read_file = self._file.read()
        self._file.close()
        return f'{read_file}'

    def add(self, *products):
        products_in_file = self.get_products()
        self._file = open(Shop.__file_name, 'a')
        for p in products:
            if str(p) not in products_in_file:
                self._file.write(f'{str(p)}\n')
            else:
                print(f'Продукт {p} уже есть в магазине')
        self._file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

