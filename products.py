from openfoodfacts import API
from tabulate import tabulate

class Products:
    GRAMS = 100

    def __init__(self):
        self.products = []
        self.select = []

    def find_item(self, index):
        product = self.products[index]
        name = product.get("product_name")
        nutriments = product.get("nutriments", {})
        calories_100 = nutriments.get("energy-kcal_100g")
        if calories_100 == None:
                calories_100 = 0
        return (name, calories_100)
    
    def get_food_list(self, food_name):
        api = API(user_agent="My calories")
        food_dict = api.product.text_search(food_name)
        self.products = food_dict.get("products", [])
        self.size_dict = len(self.products)

        if self.size_dict == 0:
            return None

        results = []
        for i in range(self.size_dict):
            name, calories = self.find_item(i)
            if name:
                results.append((i+1, name, calories))
        return results
    
    def choose_food(self, index, grams):
        if index == 0:
            return None
        if 1 <= index <= self.size_dict:
            name, calories = self.find_item(index-1)
            calories = int(calories) * (grams / Products.GRAMS)
            self.select.append({"Name": name, "Grams/ml": grams, "Calories": calories})
            return
        raise IndexError

    def create_food(self, food_name, calories, grams):
        self.select.append({"Name": food_name, "Grams/ml": grams, "Calories": calories})
        return

    def count_total(self):
        total = sum(product["Calories"] for product in self.select)
        return total

    def show_table(self):
        if not self.select:
            return "There is no products"
        table = self.select + [{"Name": "Total", "Grams/ml": "-", "Calories": self.count_total()}]
        return (tabulate(table, headers="keys", tablefmt="grid"))