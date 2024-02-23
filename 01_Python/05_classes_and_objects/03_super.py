# The super() function in Python is used to refer to the parent class or superclass of a derived class. It allows you to call methods and access attributes defined in the parent class from within the child class.

# When you create a subclass, it inherits all the methods and attributes from its parent class. However, there may be cases where you want to extend or override the behavior of the parent class while still retaining its functionality. This is where super() comes in handy.

# By using super(), you can call a method defined in the parent class and use it in the child class. This is particularly useful when you want to add some extra functionality to the existing method without completely rewriting it.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return super().speak() + f" but also he barks."
        
animal = Animal("Generic Animal")
dog = Dog("Ozzy", "Corgi")

print(animal.speak())  # Output: Generic Animal makes a sound.
print(dog.speak())  # Output: Ozzy makes a sound. It barks.