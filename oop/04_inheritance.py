class Animal:
    location = 'Australia'
    sound = "generic"

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} makes {self.sound} sound")

class Dog(Animal):
    def make_sound(self):
        return super().make_sound()
    
class Cat(Animal):
    def make_sound(self):
        return super().make_sound()
    
dog = Dog("Truxxi", "Boww")
dog.make_sound()

cat = Cat("Clove", "Meow")
cat.make_sound()