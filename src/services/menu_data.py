import csv
from src.models.ingredient import Ingredient
from src.models.dish import Dish


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load(source_path)

    def load(self, source_path: str):
        new_dish = {}
        with open(source_path) as file:
            reader = csv.DictReader(file)

            for row in reader:
                dish_name = row['dish']
                dish_price = float(row['price'])
                ingredient = Ingredient(row['ingredient'])
                dish_amount = int(row['recipe_amount'])

                if dish_name not in new_dish:
                    new_dish[dish_name] = Dish(dish_name, dish_price)

                new_dish[dish_name].add_ingredient_dependency(
                    ingredient, dish_amount
                )

        self.dishes = set(new_dish.values())
