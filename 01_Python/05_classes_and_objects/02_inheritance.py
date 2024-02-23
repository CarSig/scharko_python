class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "makes a sound."
        
    def sayName(self):
        return (f'{self.name} {self.speak()}')    

    def changeName(self, newName):
        self.name = newName

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "barks"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "meows"

# Create instances of the classes
animal = Animal("Generic Animal")
dog = Dog("Ozzy")
cat = Cat("Parki")




print (animal.speak())
print (dog.speak())
print (cat.speak())
print (dog.sayName())  # Output: Ozzy barks
print (cat.sayName())  # Output: Parki meows
print (animal.sayName())  # Output: Generic Animal makes a sound.

cat.changeName("Otis")
print (cat.sayName())  # Output: Otis meows


# what  is self?
# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class. 

# What is super()?
# The super() function is used to give access to methods and properties of a parent or sibling class.

# What is inheritance?
# Inheritance is the process by which one class takes on the attributes and methods of another. Newly formed classes are called child classes, and the classes that child classes are derived from are called parent classes. Child classes can override or extend the attributes and methods of parent classes.