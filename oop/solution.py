class Car:
    # brand = None
    # model = None

    total_cars = 0 # class variable to keep track of the total number of cars created

    def __init__(self, brand, model):
        self.__brand = brand # private attribute
        self.__model = model
        # self.total_cars += 1 # increment the total_cars variable each time a new car is created --> prints 0 because self.total_cars refers to an instance variable that is not defined, so it creates a new instance variable total_cars for each object instead of modifying the class variable.
        Car.total_cars += 1 # we can also use the class name to access the class variable instead of self.

    def get_brand(self):
        return self.__brand

    def full_name(self):
        print(f"{self.__brand} - {self.__model}")

    def fuel_type(self):
        print("This car uses gasoline.")

    @staticmethod # static method does not take self as the first parameter and can be called on the class itself without creating an instance.
    def general_description():
        return "Cars are vehicles that run on roads. They typically have four wheels and an internal combustion engine, although there are also electric cars and hybrid cars that use different types of engines. Cars are used for transportation and can vary greatly in size, style, and features."
    
    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        print("This electric car uses electricity.")



my_car = Car("Toyota", "Corolla")
# print(my_car.__brand) --> AttributeError: 'Car' object has no attribute '__brand' --> because __brand is a private attribute and cannot be accessed directly from outside the class.
print(my_car.get_brand()) # we can access the private attribute __brand using the public method get_brand()
print(my_car.model)
my_car.fuel_type()

# my_car.model = 'City' #AttributeError: property 'model' of 'Car' object has no setter

print(my_car.general_description()) # we can call the general_description method to get a description of cars in general, which is not specific to any instance of the Car class.

print()

my_new_car = Car("Honda", "Civic")
# print(my_new_car.__brand)
print(my_new_car.get_brand()) # we can access the private attribute __brand using the public method get_brand()
print(my_new_car.model)
my_new_car.fuel_type()

print()

my_car.full_name()
my_new_car.full_name()

print()

my_electric_car = ElectricCar("Tesla", "Model 3", "75 kWh")
# print(my_electric_car.brand)
print(my_electric_car.get_brand()) # we can access the private attribute __brand using the public method get_brand() inherited from the Car class
print(my_electric_car.model)
print(my_electric_car.battery_size)
my_electric_car.full_name()
my_electric_car.fuel_type() # this will call the overridden method in the ElectricCar class

print()

print("checking if electric car is an instance of Electric car class or not: ")
print(isinstance(my_electric_car, ElectricCar))

print()

print("Total cars created:", Car.total_cars)  

print()

print(my_car.general_description()) # we can call the general_description method on an instance of the Car class, but it will still return the same description since it's a static method and does not depend on the instance.

print()

print(my_new_car.general_description()) # we can also call the general_description method on another instance of the Car class, and it will return the same description.

print()

print(Car.general_description()) # we can call the general_description method directly on the Car class without creating an instance, and it will return the same description.

print()

# polymorphism with arguments
class Operation:
    def sum(self, a, b):
        return a + b
    
op1 = Operation()
print(op1.sum(5, 10)) # this will call the sum method with integer arguments
print(op1.sum(5.5, 10.2)) # this will call the sum method with float arguments
print(op1.sum("Hello, ", "world!")) # this will call the sum method with string arguments; in Python, dynamic typing allows the same method to work with different types, unlike traditional method overloading.


class Battery:
    def battery_info(self):
        print("this is battery")

class Engine:
    def engine_info(self):
        print("this is engine")

class ElectricCarTwo(Battery, Engine, Car):
    pass


print()
my_tesla = ElectricCarTwo("Tesla", "Model S")
my_tesla.battery_info() # this will call the battery_info method from the Battery class, demonstrating multiple inheritance.
my_tesla.engine_info() 