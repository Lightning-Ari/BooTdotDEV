class Restaurant:
    def __init__(self, name: str, cuisine_type: str) -> None:
        self.restaurant_name: str = name
        self.cusine_type: str = cuisine_type

    def describe_restaurant(self) -> None:
        print(f"The {self.restaurant_name} is {self.cusine_type} restaurant. Who love to share meal with others and known for good test.")

    def open_restaurant(self) -> None:
        print(f"The {self.restaurant_name} is open")



my_restaurant = Restaurant("Golden Wings", "Chiness")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


restaurant1 = Restaurant("Crab me!", "Many countries")
restaurant2 = Restaurant("Wow! Momo", "MOMO")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()

#test
