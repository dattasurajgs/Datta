class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def display(self):
        print("Brand:", self.brand)
        print("Color:", self.color)
class Car(Vehicle):
    def __init__(self, brand, color, model):
        super().__init__(brand, color)
        self.model = model
    def display_car(self):
        self.display()
        print("Model:", self.model)
car1 = Car("Toyota", "Red", "Innova")
car1.display_car()