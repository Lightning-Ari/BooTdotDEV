"""class Car:
    def __init__(self, color):
        self.color = color

# Create the two objects
car1 = Car("Red")
car2 = Car("Blue")

# car2 gives itself a reference to car1
car2.target = car1

# car2 changes car1's color directly through that reference
car2.target.color = "Purple"

# Check car1's color
print(car1.color)  # Outputs: Purple
"""

class Car():
	color = "white"
	size = "Big"
car1 = Car()

print(car1)	