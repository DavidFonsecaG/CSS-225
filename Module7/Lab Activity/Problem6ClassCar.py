# David Fonseca
# 11/13/2023
# Problem 6 - Modify the code to add two additional attributes of ‘type’ and ‘manufacturer’. Then add their
# corresponding methods to print those attributes, don’t forget to also modify the method
# fullspecs() to return the additional attributes ‘type’ and ‘manufacturer’.

class Car:
    def __init__(self, model, year, color, type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        return self.model + ' ' + str(self.year) + ' ' + self.color + ' ' + str(self.type) + ' ' + str(self.manufacturer)


car1 = Car("Sports", 2012, "Blue", "SUV", "Tesla")
car2 = Car("Sedan", 2020, "Black", "Sport", "Ferrari")
print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.fullspecs())
print(car2.fullspecs())
