# Python Design Patterns Tutorial
# ==============================

# Design patterns are typical solutions to common problems in software design.
# They are like pre-made blueprints that you can customize to solve recurring
# design problems in your code.

print("=" * 60)
print("INTRODUCTION TO DESIGN PATTERNS")
print("=" * 60)

print("""
Design patterns are categorized into three main types:

1. Creational Patterns: These patterns provide ways to create objects while hiding the creation logic.
   - Singleton, Factory Method, Abstract Factory, Builder, Prototype

2. Structural Patterns: These patterns explain how to assemble objects and classes into larger structures.
   - Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy

3. Behavioral Patterns: These patterns are concerned with algorithms and the assignment of responsibilities.
   - Chain of Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor

Design patterns help you:
- Solve common problems with proven solutions
- Use best practices for specific situations
- Communicate designs using well-known, shared concepts
- Apply principles like SOLID more effectively
""")

print("=" * 60)
print("CREATIONAL PATTERNS")
print("=" * 60)

print("\n1. Singleton Pattern:")
print("""
The Singleton pattern ensures a class has only one instance and provides a global point of access to it.
Use cases: Database connections, configuration managers, logging
""")

print("\nImplementation:")

class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = None
        return cls._instance

# Usage
print("Singleton example:")
singleton1 = Singleton()
singleton1.value = "First instance"
print(f"singleton1 value: {singleton1.value}")

singleton2 = Singleton()
print(f"singleton2 value: {singleton2.value}")  # Same value as singleton1
print(f"Are they the same object? {singleton1 is singleton2}")  # True

print("\nThread-safe Singleton with lazy initialization:")

import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
                cls._instance.value = None
        return cls._instance

print("\n2. Factory Method Pattern:")
print("""
The Factory Method pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate.
Use cases: When a class cannot anticipate the type of objects it needs to create, or when a class wants its subclasses to specify the objects it creates.
""")

print("\nImplementation:")

from abc import ABC, abstractmethod

# Product interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creator abstract class
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass
    
    def get_animal_sound(self):
        animal = self.create_animal()
        return animal.speak()

# Concrete creators
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

# Usage
print("Factory Method example:")
dog_factory = DogFactory()
print(f"Dog says: {dog_factory.get_animal_sound()}")

cat_factory = CatFactory()
print(f"Cat says: {cat_factory.get_animal_sound()}")

print("\n3. Builder Pattern:")
print("""
The Builder pattern separates the construction of a complex object from its representation.
Use cases: When an object needs to be created with many optional parameters or configurations.
""")

print("\nImplementation:")

class Computer:
    def __init__(self):
        self.cpu = None
        self.memory = None
        self.storage = None
        self.gpu = None
    
    def __str__(self):
        return f"Computer [CPU: {self.cpu}, Memory: {self.memory}GB, Storage: {self.storage}GB, GPU: {self.gpu}]"

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()
    
    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self
    
    def set_memory(self, memory):
        self.computer.memory = memory
        return self
    
    def set_storage(self, storage):
        self.computer.storage = storage
        return self
    
    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self
    
    def build(self):
        return self.computer

# Usage
print("Builder example:")
gaming_pc = ComputerBuilder() \
    .set_cpu("Intel i9") \
    .set_memory(32) \
    .set_storage(1000) \
    .set_gpu("NVIDIA RTX 3080") \
    .build()

office_pc = ComputerBuilder() \
    .set_cpu("Intel i5") \
    .set_memory(16) \
    .set_storage(512) \
    .build()  # No GPU for office PC

print(f"Gaming PC: {gaming_pc}")
print(f"Office PC: {office_pc}")

print("=" * 60)
print("STRUCTURAL PATTERNS")
print("=" * 60)

print("\n1. Adapter Pattern:")
print("""
The Adapter pattern allows objects with incompatible interfaces to collaborate.
Use cases: When you need to use an existing class with an interface that doesn't match what you need.
""")

print("\nImplementation:")

# Existing class with incompatible interface
class OldSystem:
    def old_operation(self, data):
        return f"OldSystem processed: {data}"

# Target interface
class NewSystemInterface(ABC):
    @abstractmethod
    def new_operation(self, data):
        pass

# Adapter
class SystemAdapter(NewSystemInterface):
    def __init__(self, old_system):
        self.old_system = old_system
    
    def new_operation(self, data):
        # Adapt the call to the old system
        return self.old_system.old_operation(data)

# Client code that works with the new interface
def client_code(system, data):
    return system.new_operation(data)

# Usage
print("Adapter example:")
old_system = OldSystem()
adapter = SystemAdapter(old_system)
result = client_code(adapter, "test data")
print(result)

print("\n2. Decorator Pattern:")
print("""
The Decorator pattern lets you attach new behaviors to objects by placing them inside wrapper objects.
Use cases: When you need to add responsibilities to objects dynamically without affecting other objects.
""")

print("\nImplementation:")

# Component interface
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass
    
    @abstractmethod
    def description(self):
        pass

# Concrete component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5
    
    def description(self):
        return "Simple coffee"

# Decorator base class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost()
    
    def description(self):
        return self._coffee.description()

# Concrete decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2
    
    def description(self):
        return f"{self._coffee.description()}, milk"

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1
    
    def description(self):
        return f"{self._coffee.description()}, sugar"

# Usage
print("Decorator example:")
coffee = SimpleCoffee()
print(f"{coffee.description()}: ${coffee.cost()}")

coffee_with_milk = MilkDecorator(coffee)
print(f"{coffee_with_milk.description()}: ${coffee_with_milk.cost()}")

coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
print(f"{coffee_with_milk_and_sugar.description()}: ${coffee_with_milk_and_sugar.cost()}")

print("\n3. Facade Pattern:")
print("""
The Facade pattern provides a simplified interface to a complex subsystem.
Use cases: When you need to provide a simple interface to a complex system.
""")

print("\nImplementation:")

# Complex subsystem classes
class CPU:
    def freeze(self):
        print("CPU: Freezing...")
    
    def jump(self, address):
        print(f"CPU: Jumping to address {address}")
    
    def execute(self):
        print("CPU: Executing instructions")

class Memory:
    def load(self, address, data):
        print(f"Memory: Loading data '{data}' at address {address}")

class HardDrive:
    def read(self, sector, size):
        print(f"HardDrive: Reading {size} bytes from sector {sector}")
        return "data from hard drive"

# Facade
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()
    
    def start(self):
        print("\nComputer starting...")
        self.cpu.freeze()
        self.memory.load(0, "boot data")
        self.cpu.jump(0)
        self.cpu.execute()
        data = self.hard_drive.read(0, 1024)
        self.memory.load(1, data)
        print("Computer started successfully")

# Usage
print("Facade example:")
computer = ComputerFacade()
computer.start()

print("=" * 60)
print("BEHAVIORAL PATTERNS")
print("=" * 60)

print("\n1. Observer Pattern:")
print("""
The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
Use cases: When changes to one object require changing others, and you don't know how many objects need to change.
""")

print("\nImplementation:")

# Subject interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass
    
    @abstractmethod
    def detach(self, observer):
        pass
    
    @abstractmethod
    def notify(self):
        pass

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

# Concrete subject
class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = 0
    
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)
    
    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify()
    
    def get_temperature(self):
        return self._temperature

# Concrete observers
class TemperatureDisplay(Observer):
    def update(self, subject):
        print(f"Temperature Display: {subject.get_temperature()}°C")

class FanController(Observer):
    def update(self, subject):
        if subject.get_temperature() > 25:
            print("Fan Controller: Turning fan on")
        else:
            print("Fan Controller: Turning fan off")

# Usage
print("Observer example:")
weather_station = WeatherStation()

display = TemperatureDisplay()
fan = FanController()

weather_station.attach(display)
weather_station.attach(fan)

print("\nSetting temperature to 20°C:")
weather_station.set_temperature(20)

print("\nSetting temperature to 30°C:")
weather_station.set_temperature(30)

print("\n2. Strategy Pattern:")
print("""
The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.
Use cases: When you want to define a class that will have one behavior that is similar to other behaviors in a list.
""")

print("\nImplementation:")

# Strategy interface
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

# Concrete strategies
class QuickSort(SortStrategy):
    def sort(self, data):
        print("Sorting using QuickSort")
        # Actual implementation would be here
        return sorted(data)

class MergeSort(SortStrategy):
    def sort(self, data):
        print("Sorting using MergeSort")
        # Actual implementation would be here
        return sorted(data)

class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Sorting using BubbleSort")
        # Actual implementation would be here
        return sorted(data)

# Context
class Sorter:
    def __init__(self, strategy=None):
        self._strategy = strategy
    
    def set_strategy(self, strategy):
        self._strategy = strategy
    
    def sort(self, data):
        if self._strategy is None:
            raise ValueError("Sorting strategy not set")
        return self._strategy.sort(data)

# Usage
print("Strategy example:")
data = [5, 3, 1, 4, 2]
sorter = Sorter()

# Use different strategies
sorter.set_strategy(QuickSort())
print(f"Original data: {data}")
print(f"Sorted data: {sorter.sort(data)}")

sorter.set_strategy(MergeSort())
print(f"Sorted data: {sorter.sort(data)}")

print("\n3. Command Pattern:")
print("""
The Command pattern turns a request into a stand-alone object that contains all information about the request.
Use cases: When you want to parameterize objects with operations, queue operations, or support undoable operations.
""")

print("\nImplementation:")

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass

# Receiver
class Light:
    def __init__(self, name):
        self.name = name
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        print(f"{self.name} light turned ON")
    
    def turn_off(self):
        self.is_on = False
        print(f"{self.name} light turned OFF")

# Concrete commands
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_on()
    
    def undo(self):
        self.light.turn_off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_off()
    
    def undo(self):
        self.light.turn_on()

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None
        self.history = []
    
    def set_command(self, command):
        self.command = command
    
    def press_button(self):
        if self.command:
            self.command.execute()
            self.history.append(self.command)
    
    def press_undo_button(self):
        if self.history:
            last_command = self.history.pop()
            last_command.undo()

# Usage
print("Command example:")
living_room_light = Light("Living Room")
kitchen_light = Light("Kitchen")

living_room_on = LightOnCommand(living_room_light)
living_room_off = LightOffCommand(living_room_light)
kitchen_on = LightOnCommand(kitchen_light)
kitchen_off = LightOffCommand(kitchen_light)

remote = RemoteControl()

print("\nTurning on living room light:")
remote.set_command(living_room_on)
remote.press_button()

print("\nTurning on kitchen light:")
remote.set_command(kitchen_on)
remote.press_button()

print("\nTurning off kitchen light:")
remote.set_command(kitchen_off)
remote.press_button()

print("\nUndo last action (turn kitchen light back on):")
remote.press_undo_button()

print("=" * 60)
print("APPLYING DESIGN PATTERNS WITH SOLID PRINCIPLES")
print("=" * 60)

print("""
Design patterns and SOLID principles work together to create maintainable, flexible code:

1. Single Responsibility Principle (SRP):
   - Decorator pattern: Each decorator has a single responsibility to add one behavior
   - Command pattern: Each command encapsulates a single action

2. Open/Closed Principle (OCP):
   - Strategy pattern: Add new algorithms without changing existing code
   - Factory Method: Add new product types without modifying existing factory code

3. Liskov Substitution Principle (LSP):
   - All patterns that use inheritance ensure that subclasses can substitute for their base classes
   - Template Method pattern relies on proper inheritance hierarchies

4. Interface Segregation Principle (ISP):
   - Observer pattern: Subjects and observers have focused interfaces
   - Command pattern: Commands have a simple, focused interface

5. Dependency Inversion Principle (DIP):
   - Strategy pattern: High-level modules depend on strategy abstractions
   - Factory Method: Creators depend on product abstractions
""")

print("=" * 60)
print("PRACTICAL EXAMPLE: COMBINING PATTERNS")
print("=" * 60)

print("\nExample: Document Processing System")

# Abstract Product
class Document(ABC):
    @abstractmethod
    def open(self):
        pass
    
    @abstractmethod
    def save(self):
        pass

# Concrete Products
class PDFDocument(Document):
    def __init__(self, filename):
        self.filename = filename
    
    def open(self):
        print(f"Opening PDF document: {self.filename}")
    
    def save(self):
        print(f"Saving PDF document: {self.filename}")

class WordDocument(Document):
    def __init__(self, filename):
        self.filename = filename
    
    def open(self):
        print(f"Opening Word document: {self.filename}")
    
    def save(self):
        print(f"Saving Word document: {self.filename}")

# Factory Method
class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self, filename):
        pass

class PDFFactory(DocumentFactory):
    def create_document(self, filename):
        return PDFDocument(filename)

class WordFactory(DocumentFactory):
    def create_document(self, filename):
        return WordDocument(filename)

# Strategy Pattern
class PrintStrategy(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class ColorPrintStrategy(PrintStrategy):
    def print_document(self, document):
        print(f"Printing {document.filename} in color")

class BlackAndWhitePrintStrategy(PrintStrategy):
    def print_document(self, document):
        print(f"Printing {document.filename} in black and white")

# Observer Pattern
class DocumentObserver(ABC):
    @abstractmethod
    def update(self, document):
        pass

class Logger(DocumentObserver):
    def update(self, document):
        print(f"Logger: Document {document.filename} has been modified")

class AutoSave(DocumentObserver):
    def update(self, document):
        print(f"AutoSave: Automatically saving {document.filename}")
        document.save()

# Facade
class DocumentManager:
    def __init__(self, factory):
        self.factory = factory
        self.print_strategy = None
        self.observers = []
        self.current_document = None
    
    def create_document(self, filename):
        self.current_document = self.factory.create_document(filename)
        self.notify_observers()
        return self.current_document
    
    def open_document(self):
        if self.current_document:
            self.current_document.open()
    
    def save_document(self):
        if self.current_document:
            self.current_document.save()
    
    def set_print_strategy(self, strategy):
        self.print_strategy = strategy
    
    def print_document(self):
        if self.current_document and self.print_strategy:
            self.print_strategy.print_document(self.current_document)
    
    def add_observer(self, observer):
        self.observers.append(observer)
    
    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.current_document)

# Usage
print("Document Processing System Example:")
# Create a PDF document manager
pdf_factory = PDFFactory()
doc_manager = DocumentManager(pdf_factory)

# Add observers
logger = Logger()
auto_save = AutoSave()
doc_manager.add_observer(logger)
doc_manager.add_observer(auto_save)

# Create and work with a document
print("\nCreating a new PDF document:")
doc_manager.create_document("report.pdf")
doc_manager.open_document()

# Set print strategy and print
print("\nPrinting the document:")
doc_manager.set_print_strategy(ColorPrintStrategy())
doc_manager.print_document()

# Change print strategy
print("\nChanging print strategy:")
doc_manager.set_print_strategy(BlackAndWhitePrintStrategy())
doc_manager.print_document()

# Switch to Word documents
print("\nSwitching to Word documents:")
word_factory = WordFactory()
doc_manager = DocumentManager(word_factory)
doc_manager.add_observer(logger)
doc_manager.create_document("letter.docx")
doc_manager.open_document()
doc_manager.set_print_strategy(ColorPrintStrategy())
doc_manager.print_document()

print("=" * 60)
print("BEST PRACTICES")
print("=" * 60)

print("""
1. Don't overuse design patterns
   - Use them only when they provide clear benefits
   - Simple solutions are often better than complex patterns

2. Understand the problem before applying a pattern
   - Patterns are solutions to specific problems
   - Using the wrong pattern can make code more complex

3. Combine patterns when appropriate
   - Many real-world solutions use multiple patterns together
   - Patterns often complement each other

4. Focus on the intent, not the implementation
   - Adapt patterns to your specific needs
   - The implementation may vary based on language features

5. Document your use of patterns
   - Make it clear which patterns you're using
   - Explain why you chose a particular pattern

6. Consider performance implications
   - Some patterns add overhead
   - Measure performance before and after applying patterns

7. Refactor to patterns
   - Start with simple code and refactor to patterns as needed
   - Don't try to apply patterns from the beginning
""")

print("=" * 60)
print("IMPORTANT NOTES")
print("=" * 60)

print("""
1. Design patterns are not silver bullets
   - They don't solve all problems
   - They may introduce unnecessary complexity if misused

2. Python's dynamic nature affects pattern implementation
   - Some patterns are simpler in Python than in static languages
   - Some patterns may be unnecessary due to Python's features

3. Python-specific pattern implementations:
   - Singleton can be implemented using modules (they're singletons by default)
   - Strategy pattern can use simple functions instead of classes
   - Decorators can use Python's built-in decorator syntax

4. The Gang of Four (GoF) book is the original source for many patterns
   - "Design Patterns: Elements of Reusable Object-Oriented Software"
   - Written by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides

5. Anti-patterns are common solutions that create more problems
   - God Object: A class that knows or does too much
   - Spaghetti Code: Tangled, unstructured code
   - Golden Hammer: Using a familiar tool for every problem

6. Modern Python features that complement patterns:
   - Type hints help document interfaces
   - Abstract base classes formalize interfaces
   - Context managers implement resource management patterns
""")

print("\nThank you for learning about Design Patterns in Python!")