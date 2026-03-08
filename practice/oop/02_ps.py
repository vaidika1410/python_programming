class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} - {self.age}"
    
person1 = Person("Vaidika", 22)
print(person1.get_info())