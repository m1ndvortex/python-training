# Python Class and Object-Oriented Programming Tutorial
# ===================================================

# Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects",
# which can contain data (attributes) and code (methods). Python is a multi-paradigm language
# that fully supports object-oriented programming.

print("=" * 60)
print("INTRODUCTION TO OBJECT-ORIENTED PROGRAMMING")
print("=" * 60)

print("""
Object-Oriented Programming (OOP) is based on four main principles:

1. Encapsulation: Bundling data and methods that work on that data within a single unit (class)
2. Inheritance: Creating new classes that are built upon existing classes
3. Polymorphism: Using a single interface with different underlying forms
4. Abstraction: Hiding complex implementation details and showing only the necessary features
""")

print("=" * 60)
print("CLASSES AND OBJECTS BASICS")
print("=" * 60)

print("\n1. Defining a simple class:")
# A class is a blueprint for creating objects
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor (initializer) method
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Creating instances (objects) of the class
print("\n2. Creating objects:")
dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 3)

print(f"Dog 1: {dog1.name}, {dog1.age} years old")
print(f"Dog 2: {dog2.name}, {dog2.age} years old")

# Accessing class attributes
print(f"\nDog 1 species: {dog1.species}")
print(f"Dog 2 species: {dog2.species}")
print(f"Dog class species: {Dog.species}")

# Calling instance methods
print(f"\nDescription: {dog1.description()}")
print(f"Speak: {dog1.speak('Woof!')}")

print("\n3. Understanding self:")
print("""
'self' is a reference to the current instance of the class.
It's used to access variables and methods associated with the instance.
'self' is just a convention - you could name it differently, but it's not recommended.
""")

print("\n4. Class vs Instance attributes:")
# Modifying class attribute affects all instances
Dog.species = "Canis lupus familiaris"
print(f"After changing class attribute - Dog 1 species: {dog1.species}")

# Modifying instance attribute only affects that instance
dog1.name = "Buddy Jr."
print(f"After changing instance attribute - Dog 1: {dog1.name}")
print(f"Dog 2 remains: {dog2.name}")

print("=" * 60)
print("CONSTRUCTORS AND DESTRUCTORS")
print("=" * 60)

print("""
1. __init__: Constructor method that initializes a new object
2. __del__: Destructor method called when an object is about to be destroyed
""")

class Person:
    def __init__(self, name, age):
        print(f"Creating a new Person object for {name}")
        self.name = name
        self.age = age
    
    def __del__(self):
        print(f"Person object for {self.name} is being destroyed")

# Creating and destroying objects
print("\nDemonstrating constructor and destructor:")
person = Person("Alice", 30)
print(f"Person created: {person.name}, {person.age}")
del person  # Explicitly destroy the object

print("\nNote: The destructor is also called when objects go out of scope or when the program ends.")

print("=" * 60)
print("INSTANCE, CLASS, AND STATIC METHODS")
print("=" * 60)

class MathOperations:
    # Class variable
    pi = 3.14159
    
    def __init__(self, value):
        # Instance variable
        self.value = value
    
    # Instance method (needs an instance to be called)
    def double(self):
        return self.value * 2
    
    # Class method (bound to the class, not instances)
    @classmethod
    def from_string(cls, value_str):
        value = float(value_str)
        return cls(value)  # Creates a new instance
    
    # Static method (doesn't need class or instance state)
    @staticmethod
    def add(x, y):
        return x + y

print("\n1. Using different types of methods:")
# Instance method
math_obj = MathOperations(5)
print(f"Instance method - double: {math_obj.double()}")

# Class method
math_obj2 = MathOperations.from_string("10.5")
print(f"Class method - from_string: {math_obj2.value}")

# Static method
print(f"Static method - add: {MathOperations.add(3, 4)}")
print(f"Static method from instance: {math_obj.add(3, 4)}")  # Can also be called from instance

print("\n2. When to use each type of method:")
print("""
- Instance methods: When you need to access or modify instance state
- Class methods: When you need to access or modify class state, or create alternative constructors
- Static methods: When you need a utility function related to the class but not dependent on class/instance state
""")

print("=" * 60)
print("ENCAPSULATION AND ACCESS MODIFIERS")
print("=" * 60)

print("""
Python doesn't have true private attributes, but uses conventions:
- No prefix: Public (accessible from anywhere)
- Single underscore (_): Protected (should not be accessed outside the class/subclasses)
- Double underscore (__): Name mangled (harder to access from outside, but not truly private)
""")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner           # Public attribute
        self._balance = balance       # Protected attribute
        self.__account_number = "12345"  # "Private" attribute (name mangled)
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self._balance
    
    def get_account_info(self):
        # Can access "private" attribute inside the class
        return f"Owner: {self.owner}, Account: {self.__account_number}"

print("\nDemonstrating encapsulation:")
account = BankAccount("John Doe", 1000)
print(f"Public attribute - Owner: {account.owner}")
print(f"Protected attribute - Balance: {account._balance}")  # Not truly protected

# Trying to access "private" attribute
try:
    print(account.__account_number)  # This will fail
except AttributeError as e:
    print(f"Error accessing private attribute: {e}")

# Name mangling - how Python actually stores "private" attributes
print(f"Accessing 'private' attribute with name mangling: {account._BankAccount__account_number}")

# Using proper methods to interact with the object
account.deposit(500)
print(f"After deposit - Balance: {account.get_balance()}")
account.withdraw(200)
print(f"After withdrawal - Balance: {account.get_balance()}")
print(f"Account info: {account.get_account_info()}")

print("\nProperty decorators for controlled access:")

class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    # Getter
    @property
    def celsius(self):
        return self._celsius
    
    # Setter
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value
    
    # Getter
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    # Setter
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"Celsius: {temp.celsius}")
print(f"Fahrenheit: {temp.fahrenheit}")

# Using the setter
temp.celsius = 30
print(f"After setting celsius - Fahrenheit: {temp.fahrenheit}")

temp.fahrenheit = 68
print(f"After setting fahrenheit - Celsius: {temp.celsius}")

# Validation in action
try:
    temp.celsius = -300
except ValueError as e:
    print(f"Validation error: {e}")

print("=" * 60)
print("INHERITANCE")
print("=" * 60)

print("""
Inheritance allows a class to inherit attributes and methods from another class.
- Parent/Base/Super class: The class being inherited from
- Child/Derived/Sub class: The class that inherits
""")

print("\n1. Basic inheritance:")
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic animal sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"

class Cat(Animal):
    def __init__(self, name, breed):
        # Call the parent class's __init__ method
        super().__init__(name, species="Cat")
        self.breed = breed
    
    # Override the parent method
    def make_sound(self):
        return "Meow!"
    
    # Add a new method
    def purr(self):
        return f"{self.name} is purring..."

# Create an instance of the child class
cat = Cat("Whiskers", "Siamese")
print(f"Cat info: {cat.info()}")
print(f"Cat breed: {cat.breed}")
print(f"Cat sound: {cat.make_sound()}")
print(f"Cat action: {cat.purr()}")

print("\n2. Multiple inheritance:")
class Flyable:
    def fly(self):
        return "Flying high!"

class Swimmable:
    def swim(self):
        return "Swimming deep!"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name, species="Duck")
    
    def make_sound(self):
        return "Quack!"

duck = Duck("Donald")
print(f"Duck info: {duck.info()}")
print(f"Duck sound: {duck.make_sound()}")
print(f"Duck flying: {duck.fly()}")
print(f"Duck swimming: {duck.swim()}")

print("\n3. Method Resolution Order (MRO):")
print("""
When a class inherits from multiple classes, Python uses the C3 Linearization algorithm
to determine the order in which it looks for methods and attributes.
""")
print(f"Duck's MRO: {[cls.__name__ for cls in Duck.__mro__]}")

print("\n4. isinstance() and issubclass():")
print(f"Is duck an instance of Duck? {isinstance(duck, Duck)}")
print(f"Is duck an instance of Animal? {isinstance(duck, Animal)}")
print(f"Is duck an instance of Flyable? {isinstance(duck, Flyable)}")
print(f"Is Cat a subclass of Animal? {issubclass(Cat, Animal)}")
print(f"Is Duck a subclass of Swimmable? {issubclass(Duck, Swimmable)}")

print("=" * 60)
print("POLYMORPHISM")
print("=" * 60)

print("""
Polymorphism allows objects of different classes to be treated as objects of a common superclass.
The most common use is through method overriding.
""")

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

print("\nDemonstrating polymorphism:")
shapes = [Rectangle(5, 3), Circle(4)]

for shape in shapes:
    print(f"{type(shape).__name__}:")
    print(f"  Area: {shape.area()}")
    print(f"  Perimeter: {shape.perimeter()}")

print("\nDuck typing (a form of polymorphism):")
print("""
Python uses duck typing: "If it walks like a duck and quacks like a duck, it's a duck."
This means objects are compatible with operations based on what methods they implement,
not their actual type.
""")

class NonShape:
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

# We can add this to our shapes list even though it doesn't inherit from Shape
shapes.append(NonShape(2))

for shape in shapes:
    print(f"{type(shape).__name__}:")
    print(f"  Area: {shape.area()}")
    print(f"  Perimeter: {shape.perimeter()}")

print("=" * 60)
print("ABSTRACT CLASSES AND INTERFACES")
print("=" * 60)

print("""
Abstract classes are classes that cannot be instantiated and are designed to be subclassed.
They can contain abstract methods (methods without implementation) that must be implemented by subclasses.
""")

from abc import ABC, abstractmethod

class AbstractShape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    # Concrete method
    def description(self):
        return f"This is a {type(self).__name__} with area {self.area()} and perimeter {self.perimeter()}"

class Square(AbstractShape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

print("\nDemonstrating abstract classes:")
# This would raise an error:
# shape = AbstractShape()  # Can't instantiate abstract class

square = Square(5)
print(f"Square area: {square.area()}")
print(f"Square description: {square.description()}")

print("\nPython doesn't have formal interfaces, but abstract classes with only abstract methods serve the same purpose.")

print("=" * 60)
print("MAGIC METHODS (DUNDER METHODS)")
print("=" * 60)

print("""
Magic methods (also called dunder methods for "double underscore") allow you to define
how your objects behave with built-in Python operations.
""")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # String representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Formal representation
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Addition
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # Subtraction
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    # Equality
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    # Length (magnitude)
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    # Make the object callable
    def __call__(self, scale):
        return Vector(self.x * scale, self.y * scale)

print("\nDemonstrating magic methods:")
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1: {v1}")  # Uses __str__
print(f"v1 + v2: {v1 + v2}")  # Uses __add__
print(f"v1 - v2: {v1 - v2}")  # Uses __sub__
print(f"v1 == v2: {v1 == v2}")  # Uses __eq__
print(f"|v1|: {abs(v1)}")  # Uses __abs__
print(f"v1(2): {v1(2)}")  # Uses __call__

print("\nCommon magic methods:")
print("""
- __init__: Constructor
- __del__: Destructor
- __str__: String representation (for humans)
- __repr__: Formal string representation (for developers)
- __len__: Length
- __getitem__, __setitem__: Indexing
- __iter__, __next__: Iteration
- __enter__, __exit__: Context management (with statement)
- __add__, __sub__, __mul__, etc.: Arithmetic operations
- __eq__, __lt__, __gt__, etc.: Comparison operations
- __call__: Make the object callable
""")

print("=" * 60)
print("ADVANCED OOP CONCEPTS")
print("=" * 60)

print("\n1. Descriptors:")
print("""
Descriptors are objects that define how attribute access is handled.
They implement __get__, __set__, and/or __delete__ methods.
""")

class Validator:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
        self.name = None  # Will be set when the descriptor is assigned to a class
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be at least {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be at most {self.max_value}")
        instance.__dict__[self.name] = value

class Person:
    age = Validator(0, 150)
    height = Validator(0, 300)
    
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

print("\nDemonstrating descriptors:")
person = Person("John", 30, 180)
print(f"Person: {person.name}, {person.age} years, {person.height} cm")

try:
    person.age = -5
except ValueError as e:
    print(f"Validation error: {e}")

print("\n2. Metaclasses:")
print("""
Metaclasses are classes of classes - they define how classes behave.
The default metaclass for all classes is 'type'.
""")

# A simple metaclass
class Meta(type):
    def __new__(mcs, name, bases, attrs):
        # Add a new attribute to the class
        attrs['added_by_meta'] = True
        
        # Print all method names
        methods = [key for key, value in attrs.items() 
                  if callable(value) and not key.startswith('__')]
        print(f"Class {name} has methods: {methods}")
        
        return super().__new__(mcs, name, bases, attrs)

class WithMeta(metaclass=Meta):
    def method1(self):
        return "Method 1"
    
    def method2(self):
        return "Method 2"

print(f"\nDoes WithMeta have 'added_by_meta'? {'added_by_meta' in dir(WithMeta)}")
print(f"Value of added_by_meta: {WithMeta.added_by_meta}")

print("\n3. Class decorators:")
print("""
Class decorators are functions that take a class as an argument and return a modified class.
""")

def add_greeting(cls):
    def say_hello(self):
        return f"Hello, I'm {self.name}"
    
    cls.say_hello = say_hello
    return cls

@add_greeting
class Greeter:
    def __init__(self, name):
        self.name = name

greeter = Greeter("Bob")
print(f"Greeter says: {greeter.say_hello()}")

print("\n4. Mixins:")
print("""
Mixins are classes designed to provide additional functionality to other classes through multiple inheritance.
They typically don't have their own __init__ method.
""")

class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {message}")
    
    def log_method_call(self, method_name):
        self.log(f"Calling method {method_name}")

class Service(LoggerMixin):
    def process(self):
        self.log_method_call("process")
        return "Processing data..."

service = Service()
result = service.process()
service.log("Process completed")

print("=" * 60)
print("BEST PRACTICES AND PERFORMANCE")
print("=" * 60)

print("""
1. Follow naming conventions:
   - Class names: CamelCase
   - Method/attribute names: snake_case
   - Private attributes: _name or __name

2. Use properties instead of getter/setter methods when appropriate

3. Favor composition over inheritance when possible

4. Keep classes focused (Single Responsibility Principle)

5. Use @classmethod for alternative constructors

6. Use @staticmethod for utility functions related to the class

7. Use abstract base classes to define interfaces

8. Document your classes and methods with docstrings

9. Use __slots__ for memory optimization when creating many instances

10. Be careful with mutable default arguments
""")

print("\nUsing __slots__ for memory optimization:")

class RegularPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class SlottedPerson:
    __slots__ = ['name', 'age']
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

import sys
regular = RegularPerson("John", 30)
slotted = SlottedPerson("John", 30)

print(f"Memory used by regular object: {sys.getsizeof(regular)} bytes")
print(f"Memory used by slotted object: {sys.getsizeof(slotted)} bytes")
print(f"Regular object __dict__ size: {sys.getsizeof(regular.__dict__)} bytes")
print(f"Slotted object has no __dict__: {'__dict__' in dir(slotted)}")

print("\nMutable default arguments issue:")

def bad_append(item, items=[]):
    items.append(item)
    return items

def good_append(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(f"First call to bad_append: {bad_append(1)}")
print(f"Second call to bad_append: {bad_append(2)}")  # Oops, [1, 2] instead of [2]

print(f"First call to good_append: {good_append(1)}")
print(f"Second call to good_append: {good_append(2)}")  # Correctly returns [2]

print("=" * 60)
print("CONCLUSION")
print("=" * 60)

print("""
Object-Oriented Programming in Python provides powerful tools for structuring your code:

1. Classes and objects help organize code around data and behavior
2. Inheritance promotes code reuse and establishes relationships
3. Polymorphism enables flexibility and extensibility
4. Encapsulation protects data and implementation details
5. Abstract classes define interfaces for subclasses
6. Magic methods customize object behavior with Python's built-in operations
7. Advanced features like descriptors, metaclasses, and mixins provide sophisticated solutions

Remember that while OOP is powerful, it's not always the best approach for every problem.
Python supports multiple programming paradigms, so choose the right tool for the job.
""")

print("\nThank you for learning about Python classes and OOP!")