# Python Dependency Injection Tutorial
# ===================================

# Dependency Injection (DI) is a design pattern that implements the Dependency Inversion Principle.
# It allows a program to remove hard-coded dependencies and make it possible to change them,
# whether at run-time or compile-time.

print("=" * 60)
print("INTRODUCTION TO DEPENDENCY INJECTION")
print("=" * 60)

print("""
Dependency Injection is a technique where one object supplies the dependencies of another object.
A dependency is an object that can be used by another object.

Key concepts:
1. Client: The class that depends on the service
2. Service: The class that provides functionality to the client
3. Injector: The code that passes the service to the client

Types of Dependency Injection:
1. Constructor Injection: Dependencies are provided through a class constructor
2. Setter Injection: Dependencies are provided through setter methods
3. Method Injection: Dependencies are provided through method parameters
""")

print("=" * 60)
print("PROBLEMS WITHOUT DEPENDENCY INJECTION")
print("=" * 60)

print("\n1. Hard-coded dependencies:")

class EmailService:
    def send_email(self, message, recipient):
        print(f"Sending email to {recipient}: {message}")

class UserServiceBad:
    def __init__(self):
        # Hard-coded dependency
        self.email_service = EmailService()
    
    def notify_user(self, user_email, message):
        self.email_service.send_email(message, user_email)

print("Without dependency injection:")
user_service_bad = UserServiceBad()
user_service_bad.notify_user("user@example.com", "Hello!")

print("\n2. Problems with hard-coded dependencies:")
print("""
- Tight coupling: UserServiceBad is tightly coupled to EmailService
- Difficult testing: Can't easily replace EmailService with a mock for testing
- Inflexible: Can't change the notification method without modifying UserServiceBad
- Violates Single Responsibility Principle: UserServiceBad knows how to create EmailService
""")

print("=" * 60)
print("IMPLEMENTING DEPENDENCY INJECTION")
print("=" * 60)

print("\n1. Constructor Injection:")

class NotificationService:
    def send_notification(self, message, recipient):
        pass

class EmailNotificationService(NotificationService):
    def send_notification(self, message, recipient):
        print(f"Sending email to {recipient}: {message}")

class SMSNotificationService(NotificationService):
    def send_notification(self, message, recipient):
        print(f"Sending SMS to {recipient}: {message}")

class UserService:
    def __init__(self, notification_service):
        # Dependency injected through constructor
        self.notification_service = notification_service
    
    def notify_user(self, user_contact, message):
        self.notification_service.send_notification(message, user_contact)

print("With constructor injection:")
# Inject EmailNotificationService
email_service = EmailNotificationService()
user_service = UserService(email_service)
user_service.notify_user("user@example.com", "Hello via email!")

# Easily switch to SMSNotificationService
sms_service = SMSNotificationService()
user_service = UserService(sms_service)
user_service.notify_user("+1234567890", "Hello via SMS!")

print("\n2. Setter Injection:")

class ConfigService:
    def __init__(self):
        self.data_source = None
    
    # Dependency injected through setter method
    def set_data_source(self, data_source):
        self.data_source = data_source
    
    def get_config(self, key):
        if self.data_source is None:
            raise ValueError("Data source not set")
        return self.data_source.get_data(key)

class FileDataSource:
    def get_data(self, key):
        print(f"Getting {key} from file")
        return f"Value for {key} from file"

class DatabaseDataSource:
    def get_data(self, key):
        print(f"Getting {key} from database")
        return f"Value for {key} from database"

print("With setter injection:")
config_service = ConfigService()

# Inject FileDataSource
file_source = FileDataSource()
config_service.set_data_source(file_source)
print(config_service.get_config("api_key"))

# Switch to DatabaseDataSource
db_source = DatabaseDataSource()
config_service.set_data_source(db_source)
print(config_service.get_config("api_key"))

print("\n3. Method Injection:")

class Renderer:
    def render(self, data, formatter):
        # Dependency injected through method parameter
        formatted_data = formatter.format(data)
        print(f"Rendering: {formatted_data}")

class HTMLFormatter:
    def format(self, data):
        return f"<div>{data}</div>"

class JSONFormatter:
    def format(self, data):
        return f'{{"data": "{data}"}}'

print("With method injection:")
renderer = Renderer()
html_formatter = HTMLFormatter()
json_formatter = JSONFormatter()

renderer.render("Hello, World!", html_formatter)
renderer.render("Hello, World!", json_formatter)

print("=" * 60)
print("DEPENDENCY INJECTION CONTAINERS")
print("=" * 60)

print("""
Dependency Injection Containers (DI Containers) are tools that help to manage dependencies.
They automatically create and inject dependencies, reducing boilerplate code.

Python has several DI container libraries:
- injector
- dependency_injector
- punq
- python-inject
""")

print("\nSimple DI Container implementation:")

class DIContainer:
    def __init__(self):
        self.services = {}
    
    def register(self, interface, implementation):
        self.services[interface] = implementation
    
    def resolve(self, interface):
        if interface not in self.services:
            raise ValueError(f"No implementation registered for {interface}")
        return self.services[interface]()

# Example interfaces and implementations
class Logger:
    def log(self, message):
        pass

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"[Console] {message}")

class FileLogger(Logger):
    def log(self, message):
        print(f"[File] {message}")

class UserRepository:
    def save(self, user):
        pass

class SQLUserRepository(UserRepository):
    def save(self, user):
        print(f"Saving user {user} to SQL database")

# Service that depends on Logger and UserRepository
class UserManager:
    def __init__(self, logger, user_repository):
        self.logger = logger
        self.user_repository = user_repository
    
    def create_user(self, username):
        self.logger.log(f"Creating user: {username}")
        self.user_repository.save(username)
        self.logger.log(f"User {username} created successfully")

# Using the DI Container
container = DIContainer()
container.register(Logger, lambda: ConsoleLogger())
container.register(UserRepository, lambda: SQLUserRepository())

# Factory function for UserManager that resolves dependencies
container.register(UserManager, lambda: UserManager(
    container.resolve(Logger),
    container.resolve(UserRepository)
))

# Using the resolved service
print("\nUsing DI Container:")
user_manager = container.resolve(UserManager)
user_manager.create_user("john_doe")

# Changing implementation
print("\nChanging implementation:")
container.register(Logger, lambda: FileLogger())
user_manager = container.resolve(UserManager)
user_manager.create_user("jane_doe")

print("=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

print("\n1. Testing with Dependency Injection:")

import unittest
from unittest.mock import Mock

class EmailSender:
    def send(self, email, subject, body):
        # In a real application, this would send an actual email
        print(f"Sending email to {email} with subject: {subject}")
        return True

class UserNotifier:
    def __init__(self, email_sender):
        self.email_sender = email_sender
    
    def notify_user(self, user_email, message):
        subject = "Notification"
        return self.email_sender.send(user_email, subject, message)

class TestUserNotifier(unittest.TestCase):
    def test_notify_user(self):
        # Create a mock email sender
        mock_email_sender = Mock()
        mock_email_sender.send.return_value = True
        
        # Inject the mock into UserNotifier
        notifier = UserNotifier(mock_email_sender)
        
        # Test the notify_user method
        result = notifier.notify_user("test@example.com", "Test message")
        
        # Verify the result and that send was called with correct parameters
        self.assertTrue(result)
        mock_email_sender.send.assert_called_once_with(
            "test@example.com", "Notification", "Test message"
        )

print("Testing with dependency injection allows us to:")
print("- Replace real dependencies with mocks")
print("- Test components in isolation")
print("- Verify interactions between components")

print("\n2. Configuration-based Dependency Injection:")

class AppConfig:
    def __init__(self):
        # In a real app, this might come from a config file
        self.config = {
            "environment": "development",
            "logger": "console"  # or "file"
        }
    
    def get(self, key):
        return self.config.get(key)

class LoggerFactory:
    @staticmethod
    def create_logger(config):
        logger_type = config.get("logger")
        if logger_type == "file":
            return FileLogger()
        else:
            return ConsoleLogger()

class Application:
    def __init__(self, config):
        self.config = config
        # Dependencies created based on configuration
        self.logger = LoggerFactory.create_logger(config)
    
    def run(self):
        env = self.config.get("environment")
        self.logger.log(f"Application running in {env} environment")

print("Configuration-based dependency injection:")
app_config = AppConfig()
app = Application(app_config)
app.run()

print("\n3. Real-world example: Web API with Dependency Injection:")

class Database:
    def query(self, sql):
        print(f"Executing SQL: {sql}")
        return [{"id": 1, "name": "Product 1"}, {"id": 2, "name": "Product 2"}]

class ProductRepository:
    def __init__(self, database):
        self.database = database
    
    def get_all(self):
        return self.database.query("SELECT * FROM products")
    
    def get_by_id(self, product_id):
        result = self.database.query(f"SELECT * FROM products WHERE id = {product_id}")
        return result[0] if result else None

class ProductService:
    def __init__(self, product_repository):
        self.product_repository = product_repository
    
    def get_all_products(self):
        return self.product_repository.get_all()
    
    def get_product(self, product_id):
        return self.product_repository.get_by_id(product_id)

class ProductController:
    def __init__(self, product_service):
        self.product_service = product_service
    
    def get_products(self):
        products = self.product_service.get_all_products()
        return {"products": products}
    
    def get_product(self, product_id):
        product = self.product_service.get_product(product_id)
        if product:
            return {"product": product}
        return {"error": "Product not found"}

# Setting up the dependency chain
print("Web API with dependency injection:")
database = Database()
product_repository = ProductRepository(database)
product_service = ProductService(product_repository)
product_controller = ProductController(product_service)

# Using the API
print("\nGetting all products:")
response = product_controller.get_products()
print(f"Response: {response}")

print("\nGetting product by ID:")
response = product_controller.get_product(1)
print(f"Response: {response}")

print("=" * 60)
print("BEST PRACTICES")
print("=" * 60)

print("""
1. Inject dependencies through constructors when possible
   - Makes dependencies explicit and required

2. Use interfaces (abstract base classes in Python) for dependencies
   - Allows for different implementations
   - Makes testing easier

3. Keep services focused and cohesive
   - Each service should have a single responsibility

4. Avoid service locator pattern when possible
   - Prefer explicit dependency injection
   - Service locator hides dependencies

5. Consider using a DI container for complex applications
   - Reduces boilerplate code
   - Manages object lifecycles

6. Don't overuse dependency injection
   - Not every class needs to be injected
   - Value objects and entities often don't need DI

7. Use factory methods for complex object creation
   - When creating an object requires complex logic
""")

print("=" * 60)
print("IMPORTANT NOTES")
print("=" * 60)

print("""
1. Dependency Injection is a technique, not a framework
   - You can implement it without any special libraries

2. DI helps implement the Dependency Inversion Principle from SOLID
   - High-level modules depend on abstractions, not concrete implementations

3. Python's dynamic nature allows for more flexible DI approaches
   - Duck typing reduces the need for formal interfaces
   - Monkey patching can be used for testing (though DI is cleaner)

4. DI is particularly valuable in larger applications
   - Small scripts may not benefit as much from formal DI

5. DI works well with other design patterns
   - Factory pattern for creating dependencies
   - Strategy pattern for interchangeable algorithms
   - Repository pattern for data access

6. DI facilitates:
   - Testability: Easy to mock dependencies
   - Maintainability: Loose coupling between components
   - Extensibility: Easy to add new implementations
   - Parallel development: Teams can work on different components
""")

print("\nThank you for learning about Dependency Injection in Python!")