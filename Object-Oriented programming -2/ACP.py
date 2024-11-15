class MenuItem:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_item_to_menu(self, item):
        self.menu.append(item)

    def display_menu(self):
        print(f"\nWelcome to {self.name}!")
        print("Our Menu:")
        for item in self.menu:
            print(item)
        print()


def main():
    restaurant = Restaurant("Brick Lane Cafe")
    restaurant.add_item_to_menu(MenuItem("Spaghetti Bolognese"))
    restaurant.add_item_to_menu(MenuItem("Grilled Chicken"))
    restaurant.add_item_to_menu(MenuItem("Caesar Salad"))
    restaurant.add_item_to_menu(MenuItem("Cheeseburger"))
    restaurant.add_item_to_menu(MenuItem("Vegetarian Pizza"))
    restaurant.add_item_to_menu(MenuItem("Chocolate Lava Cake"))
    restaurant.display_menu()


if __name__ == "__main__":
    main()
