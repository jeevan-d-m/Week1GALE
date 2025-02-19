class Category():
    def __init__(self, name, parent_category):
        self.name = name
        self.parent_category = parent_category


class Products():
    def __init__(self, name,categories):
        self.name=name
        self.categories = categories

    def display_categories(self):
        temp = self.categories
        while temp.parent_category!=None:
            print(temp.name)
            temp=temp.parent_category
        print(temp.name)

def filter_products(leaf_node, all_products:list):
    for products in all_products:
        if products.categories==leaf_node:
            print(products.name)

def filter_all_products(any_node, all_products: list):
    for products in all_products:
        temp = products.categories
        while temp:
            if temp==any_node:
                print(products.name)
                break
            temp = temp.parent_category

clothes = Category("clothes", None)
shirt = Category("Shirt", clothes)
Tshirt = Category("T-shirt", shirt)
hoodies = Category("hoodies", shirt)

electronics = Category("electronics", None)
mobile = Category("mobile", electronics)
laptop = Category("laptop", electronics)
redmi = Category("redmi", mobile)
realme = Category("realme", mobile)
dell = Category("dell", laptop)
macbook = Category("macbook", laptop)


product1 = Products("puma", hoodies)
product2 = Products("nike", Tshirt)
product3 = Products("adidas", Tshirt)

product4 = Products("realmePhone", mobile)
product5 = Products("redmiPhone", redmi)
product6 = Products("DellLaptop", laptop)
product7 = Products("macbook", electronics)


product1.display_categories()
print("\n")
product2.display_categories()
print("\n")
filter_products(hoodies, [product1,product2,product3])
print("\n")
filter_products(Tshirt, [product1,product2,product3])
# filter_products(shirt,[product1,product2,product3])
print("\n")
filter_all_products(electronics, [product4, product5, product6])