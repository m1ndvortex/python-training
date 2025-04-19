# Python SOLID Principles Tutorial
# ===============================

# SOLID is an acronym for five design principles intended to make software designs
# more understandable, flexible, and maintainable.

print("=" * 60)
print("INTRODUCTION TO SOLID PRINCIPLES")
print("=" * 60)

print("""
SOLID stands for:
1. S - Single Responsibility Principle (SRP)
2. O - Open/Closed Principle (OCP)
3. L - Liskov Substitution Principle (LSP)
4. I - Interface Segregation Principle (ISP)
5. D - Dependency Inversion Principle (DIP)

These principles were introduced by Robert C. Martin (Uncle Bob) and are
widely used in object-oriented design.
""")

print("=" * 60)
print("SINGLE RESPONSIBILITY PRINCIPLE (SRP)")
print("=" * 60)

print("""
The Single Responsibility Principle states that a class should have only one reason to change,
meaning it should have only one responsibility or job.
""")

print("\n1. Violating SRP:")

class UserBad:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        return self.name
    
    def save(self) -> None:
        print(f"Saving user {self.name} to database")  # Database logic
    
    def send_email(self, message: str) -> None:
        print(f"Sending email to {self.name}: {message}")  # Email logic

user_bad = UserBad("John")
print("Bad example (violating SRP):")
user_bad.save()  # User class handling database operations
user_bad.send_email("Hello!")  # User class handling email operations

print("\n2. Following SRP:")

class User:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        return self.name

class UserRepository:
    def save(self, user: User) -> None:
        print(f"Saving user {user.get_name()} to database")

class EmailService:
    def send_email(self, user: User, message: str) -> None:
        print(f"Sending email to {user.get_name()}: {message}")

user = User("John")
user_repository = UserRepository()
email_service = EmailService()

print("Good example (following SRP):")
user_repository.save(user)  # Separate class for database operations
email_service.send_email(user, "Hello!")  # Separate class for email operations

print("=" * 60)
print("OPEN/CLOSED PRINCIPLE (OCP)")
print("=" * 60)

print("""
The Open/Closed Principle states that software entities (classes, modules, functions, etc.)
should be open for extension but closed for modification.
""")

print("\n1. Violating OCP:")

class DiscountCalculatorBad:
    def calculate_discount(self, product_type: str, price: float) -> float:
        if product_type == "electronics":
            return price * 0.1  # 10% discount
        elif product_type == "clothing":
            return price * 0.2  # 20% discount
        elif product_type == "furniture":
            return price * 0.3  # 30% discount
        return 0  # No discount

calculator_bad = DiscountCalculatorBad()
print("Bad example (violating OCP):")
print(f"Electronics discount: ${calculator_bad.calculate_discount('electronics', 1000)}")
print(f"Clothing discount: ${calculator_bad.calculate_discount('clothing', 1000)}")
# If we want to add a new product type, we need to modify the existing class

print("\n2. Following OCP:")

from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, price: float) -> float:
        pass

class ElectronicsDiscount(DiscountStrategy):
    def calculate_discount(self, price: float) -> float:
        return price * 0.1  # 10% discount

class ClothingDiscount(DiscountStrategy):
    def calculate_discount(self, price: float) -> float:
        return price * 0.2  # 20% discount

class FurnitureDiscount(DiscountStrategy):
    def calculate_discount(self, price: float) -> float:
        return price * 0.3  # 30% discount

class DiscountCalculator:
    def calculate_discount(self, strategy: DiscountStrategy, price: float) -> float:
        return strategy.calculate_discount(price)

calculator = DiscountCalculator()
electronics_discount = ElectronicsDiscount()
clothing_discount = ClothingDiscount()

print("Good example (following OCP):")
print(f"Electronics discount: ${calculator.calculate_discount(electronics_discount, 1000)}")
print(f"Clothing discount: ${calculator.calculate_discount(clothing_discount, 1000)}")

# To add a new product type, we just create a new strategy class without modifying existing code
class BooksDiscount(DiscountStrategy):
    def calculate_discount(self, price: float) -> float:
        return price * 0.15  # 15% discount

books_discount = BooksDiscount()
print(f"Books discount: ${calculator.calculate_discount(books_discount, 1000)}")

print("=" * 60)
print("LISKOV SUBSTITUTION PRINCIPLE (LSP)")
print("=" * 60)

print("""
The Liskov Substitution Principle states that objects of a superclass should be replaceable
with objects of a subclass without affecting the correctness of the program.
""")

print("\n1. Violating LSP:")

class BirdBad:
    def fly(self):
        print("Flying high!")

class OstrichBad(BirdBad):
    def fly(self):
        raise Exception("Ostriches can't fly!")  # Breaks LSP

def make_bird_fly_bad(bird: BirdBad):
    bird.fly()

print("Bad example (violating LSP):")
try:
    bird = BirdBad()
    make_bird_fly_bad(bird)  # Works fine
    
    ostrich = OstrichBad()
    make_bird_fly_bad(ostrich)  # Throws exception, breaking LSP
except Exception as e:
    print(f"Error: {e}")

print("\n2. Following LSP:")

class Animal:
    def move(self):
        pass

class FlyingBird(Animal):
    def move(self):
        print("Flying high!")

class NonFlyingBird(Animal):
    def move(self):
        print("Walking along!")

def make_animal_move(animal: Animal):
    animal.move()

print("Good example (following LSP):")
flying_bird = FlyingBird()
non_flying_bird = NonFlyingBird()

make_animal_move(flying_bird)  # Works fine
make_animal_move(non_flying_bird)  # Also works fine, no exceptions

print("=" * 60)
print("INTERFACE SEGREGATION PRINCIPLE (ISP)")
print("=" * 60)

print("""
The Interface Segregation Principle states that clients should not be forced to depend on
interfaces they do not use. In other words, many client-specific interfaces are better than
one general-purpose interface.
""")

print("\n1. Violating ISP:")

from abc import ABC, abstractmethod

class WorkerBad(ABC):
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def sleep(self):
        pass

class HumanBad(WorkerBad):
    def work(self):
        print("Human working")
    
    def eat(self):
        print("Human eating")
    
    def sleep(self):
        print("Human sleeping")

class RobotBad(WorkerBad):
    def work(self):
        print("Robot working")
    
    def eat(self):
        # Robots don't eat, but forced to implement this method
        raise NotImplementedError("Robots don't eat")
    
    def sleep(self):
        # Robots don't sleep, but forced to implement this method
        raise NotImplementedError("Robots don't sleep")

print("Bad example (violating ISP):")
human_bad = HumanBad()
human_bad.work()
human_bad.eat()

robot_bad = RobotBad()
robot_bad.work()
try:
    robot_bad.eat()  # This will raise an exception
except NotImplementedError as e:
    print(f"Error: {e}")

print("\n2. Following ISP:")

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass

class Human(Workable, Eatable, Sleepable):
    def work(self):
        print("Human working")
    
    def eat(self):
        print("Human eating")
    
    def sleep(self):
        print("Human sleeping")

class Robot(Workable):
    def work(self):
        print("Robot working")
    # No need to implement eat() or sleep()

print("Good example (following ISP):")
human = Human()
human.work()
human.eat()
human.sleep()

robot = Robot()
robot.work()
# No need to call eat() or sleep() on robot

print("=" * 60)
print("DEPENDENCY INVERSION PRINCIPLE (DIP)")
print("=" * 60)

print("""
The Dependency Inversion Principle states that:
1. High-level modules should not depend on low-level modules. Both should depend on abstractions.
2. Abstractions should not depend on details. Details should depend on abstractions.
""")

print("\n1. Violating DIP:")

class LightBulbBad:
    def turn_on(self):
        print("LightBulb: turned on")
    
    def turn_off(self):
        print("LightBulb: turned off")

class SwitchBad:
    def __init__(self, bulb: LightBulbBad):
        self.bulb = bulb
        self.is_on = False
    
    def press(self):
        if self.is_on:
            self.bulb.turn_off()
            self.is_on = False
        else:
            self.bulb.turn_on()
            self.is_on = True

print("Bad example (violating DIP):")
bulb_bad = LightBulbBad()
switch_bad = SwitchBad(bulb_bad)
switch_bad.press()  # Turn on
switch_bad.press()  # Turn off

print("\n2. Following DIP:")

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on")
    
    def turn_off(self):
        print("LightBulb: turned off")

class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on")
    
    def turn_off(self):
        print("Fan: turned off")

class Switch:
    def __init__(self, device: Switchable):
        self.device = device
        self.is_on = False
    
    def press(self):
        if self.is_on:
            self.device.turn_off()
            self.is_on = False
        else:
            self.device.turn_on()
            self.is_on = True

print("Good example (following DIP):")
bulb = LightBulb()
switch = Switch(bulb)
switch.press()  # Turn on
switch.press()  # Turn off

# We can easily switch to a different device
fan = Fan()
switch = Switch(fan)
switch.press()  # Turn on
switch.press()  # Turn off

print("=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

print("\n1. Combining SOLID principles in a real-world example:")

# Define abstractions
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class OrderRepository(ABC):
    @abstractmethod
    def save(self, order_id: str, amount: float, items: list) -> None:
        pass

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message: str, recipient: str) -> None:
        pass

# Implementations
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing credit card payment of ${amount}")
        return True

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing PayPal payment of ${amount}")
        return True

class SQLOrderRepository(OrderRepository):
    def save(self, order_id: str, amount: float, items: list) -> None:
        print(f"Saving order {order_id} to SQL database")

class EmailNotificationService(NotificationService):
    def send_notification(self, message: str, recipient: str) -> None:
        print(f"Sending email to {recipient}: {message}")

class SMSNotificationService(NotificationService):
    def send_notification(self, message: str, recipient: str) -> None:
        print(f"Sending SMS to {recipient}: {message}")

# High-level module
class OrderService:
    def __init__(self, payment_processor: PaymentProcessor, 
                 order_repository: OrderRepository,
                 notification_service: NotificationService):
        self.payment_processor = payment_processor
        self.order_repository = order_repository
        self.notification_service = notification_service
    
    def place_order(self, order_id: str, amount: float, items: list, customer_email: str) -> bool:
        # Process payment
        payment_successful = self.payment_processor.process_payment(amount)
        
        if payment_successful:
            # Save order
            self.order_repository.save(order_id, amount, items)
            
            # Notify customer
            self.notification_service.send_notification(
                f"Your order {order_id} has been placed successfully!",
                customer_email
            )
            return True
        else:
            self.notification_service.send_notification(
                f"Payment failed for order {order_id}.",
                customer_email
            )
            return False

# Usage
print("Placing an order with credit card payment and email notification:")
order_service = OrderService(
    CreditCardProcessor(),
    SQLOrderRepository(),
    EmailNotificationService()
)
order_service.place_order("ORD-12345", 99.99, ["Item1", "Item2"], "customer@example.com")

print("\nPlacing an order with PayPal payment and SMS notification:")
order_service = OrderService(
    PayPalProcessor(),
    SQLOrderRepository(),
    SMSNotificationService()
)
order_service.place_order("ORD-67890", 149.99, ["Item3", "Item4"], "+1234567890")

print("=" * 60)
print("COMMON PITFALLS AND BEST PRACTICES")
print("=" * 60)

print("""
Common Pitfalls:

1. Over-engineering: Applying SOLID principles excessively can lead to unnecessary complexity.
   - Solution: Apply principles pragmatically based on the specific needs of your project.

2. Premature abstraction: Creating abstractions before they're needed.
   - Solution: Follow the "Rule of Three" - wait until you have at least three similar implementations
     before creating an abstraction.

3. Ignoring trade-offs: SOLID principles may sometimes conflict with performance or simplicity.
   - Solution: Balance principles with practical considerations.

Best Practices:

1. Start simple and refactor: Begin with a simple implementation and refactor as needed.

2. Use composition over inheritance: Favor object composition over class inheritance when possible.

3. Write tests first: Test-driven development helps ensure your design meets requirements.

4. Focus on the problem domain: Design your classes to reflect the problem domain, not technical details.

5. Continuous refactoring: Regularly review and refactor your code to maintain SOLID principles.
""")

print("=" * 60)
print("IMPORTANT NOTES")
print("=" * 60)

print("""
1. SOLID principles are guidelines, not strict rules. Use them wisely.

2. Python is dynamically typed, which affects how some principles are applied:
   - Duck typing often replaces formal interfaces
   - Abstract base classes (ABC) can be used to define interfaces

3. The goal of SOLID is to create code that is:
   - Easy to understand and maintain
   - Flexible and adaptable to change
   - Testable and robust

4. SOLID principles work best when combined with other good practices:
   - DRY (Don't Repeat Yourself)
   - KISS (Keep It Simple, Stupid)
   - YAGNI (You Aren't Gonna Need It)

5. Remember that different projects have different needs:
   - Small scripts may not benefit from full SOLID implementation
   - Large, long-lived applications benefit most from SOLID principles
""")

print("\nThank you for learning about SOLID principles in Python!")