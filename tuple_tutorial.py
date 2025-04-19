# Python Tuple Tutorial
# ===================

# A tuple is an ordered, immutable collection of elements.
# Tuples can contain elements of different types, just like lists.

print("=" * 50)
print("TUPLE BASICS")
print("=" * 50)

# Creating tuples
print("\n1. Creating tuples:")

# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# Tuple with one element (note the comma)
singleton = (1,)  # Without the comma, (1) would be interpreted as the integer 1
print(f"Singleton tuple: {singleton}")

# Tuple with multiple elements
numbers = (1, 2, 3, 4, 5)
print(f"Numbers tuple: {numbers}")

# Mixed types
mixed = (1, "hello", 3.14, True, (1, 2, 3))
print(f"Mixed types tuple: {mixed}")

# Tuple packing (without parentheses)
coordinates = 10, 20, 30  # This is also a tuple
print(f"Coordinates tuple: {coordinates}")

# Using tuple() constructor
chars = tuple("hello")  # Creates a tuple of characters
print(f"Characters tuple: {chars}")

# Creating a tuple from a list
from_list = tuple([1, 2, 3, 4, 5])
print(f"Tuple from list: {from_list}")

print("\n2. Accessing tuple elements:")
# Indexing (0-based)
fruits = ("apple", "banana", "cherry", "date", "elderberry")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")  # Negative indexing starts from the end

# Slicing [start:end:step]
print(f"First three fruits: {fruits[0:3]}")  # or fruits[:3]
print(f"Last three fruits: {fruits[-3:]}")
print(f"Every other fruit: {fruits[::2]}")
print(f"Reversed tuple: {fruits[::-1]}")

print("\n3. Tuple operations:")
a = (1, 2, 3)
b = (4, 5, 6)

# Concatenation
c = a + b
print(f"a + b = {c}")

# Repetition
d = a * 3
print(f"a * 3 = {d}")

# Length
print(f"Length of c: {len(c)}")

# Membership testing
print(f"Is 5 in c? {5 in c}")
print(f"Is 7 in c? {7 in c}")

# Min and max
print(f"Min of c: {min(c)}")
print(f"Max of c: {max(c)}")

# Sum
print(f"Sum of c: {sum(c)}")

print("\n4. Tuple immutability:")
# Tuples are immutable - you cannot change their content after creation
try:
    numbers = (1, 2, 3, 4, 5)
    numbers[0] = 10  # This will raise TypeError
except TypeError as e:
    print(f"Error: {e}")

# However, if a tuple contains mutable objects, those objects can be modified
mutable_in_tuple = ([1, 2, 3], [4, 5, 6])
print(f"Original tuple with lists: {mutable_in_tuple}")
mutable_in_tuple[0].append(4)  # This works because the list itself is mutable
print(f"After modifying the list inside: {mutable_in_tuple}")

print("=" * 50)
print("TUPLE METHODS")
print("=" * 50)

print("\n1. Tuple methods:")
# Tuples have only two methods since they're immutable
numbers = (1, 2, 3, 1, 4, 5, 1)

# count() - returns the number of occurrences of a value
print(f"Count of 1: {numbers.count(1)}")

# index() - returns the index of the first occurrence of a value
print(f"Index of 3: {numbers.index(3)}")
# print(f"Index of 7: {numbers.index(7)}")  # Would raise ValueError if element not found

# Safe way to find index
element = 7
try:
    index = numbers.index(element)
    print(f"Index of {element}: {index}")
except ValueError:
    print(f"{element} not found in the tuple")

print("\n2. Converting between tuples and other collections:")
# Tuple to list
tuple_to_list = list((1, 2, 3))
print(f"Tuple to list: {tuple_to_list}")

# List to tuple
list_to_tuple = tuple([4, 5, 6])
print(f"List to tuple: {list_to_tuple}")

# Tuple to set (removes duplicates)
tuple_to_set = set((1, 2, 2, 3, 3, 3))
print(f"Tuple to set: {tuple_to_set}")

# String to tuple
string_to_tuple = tuple("hello")
print(f"String to tuple: {string_to_tuple}")

print("=" * 50)
print("ADVANCED TUPLE OPERATIONS")
print("=" * 50)

print("\n1. Tuple unpacking:")
# Basic unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"Unpacked coordinates: x={x}, y={y}, z={z}")

# Unpacking with * (star) operator to collect remaining items
first, *rest = (1, 2, 3, 4, 5)
print(f"First: {first}, Rest: {rest}")  # Rest becomes a list

*beginning, last = (1, 2, 3, 4, 5)
print(f"Beginning: {beginning}, Last: {last}")

first, *middle, last = (1, 2, 3, 4, 5)
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Ignoring values with _
a, _, b, _, c = (1, 2, 3, 4, 5)
print(f"Selected values: {a}, {b}, {c}")

print("\n2. Tuple as return values:")
# Functions often return multiple values as a tuple
def get_dimensions():
    return (1920, 1080)  # Returns a tuple

width, height = get_dimensions()  # Unpacks the tuple
print(f"Screen dimensions: {width}x{height}")

# Implicit tuple packing and unpacking
def get_user_info():
    return "John", 30, "john@example.com"  # Implicitly returns a tuple

name, age, email = get_user_info()  # Unpacks the tuple
print(f"User: {name}, {age}, {email}")

print("\n3. Named tuples:")
# Named tuples are a memory-efficient way to define simple classes
from collections import namedtuple

# Define a named tuple type
Point = namedtuple('Point', ['x', 'y', 'z'])

# Create instances
p1 = Point(1, 2, 3)
p2 = Point(x=4, y=5, z=6)  # Can use keyword arguments

print(f"Point 1: {p1}")
print(f"Point 2: {p2}")

# Access by name or index
print(f"p1.x: {p1.x}, p1[0]: {p1[0]}")

# Convert to dictionary
p1_dict = p1._asdict()
print(f"Point 1 as dict: {p1_dict}")

# Create a new instance with updated values
p3 = p1._replace(x=10, y=20)
print(f"Point 3 (updated Point 1): {p3}")

# Named tuples are still immutable
try:
    p1.x = 10  # This will raise AttributeError
except AttributeError as e:
    print(f"Error: {e}")

print("\n4. Tuple performance considerations:")
# Time complexity:
# - Access by index: O(1)
# - Search (in operator): O(n)
# - Immutability means no insertion/deletion operations

# Memory usage example
import sys
small_tuple = (1, 2, 3)
small_list = [1, 2, 3]
print(f"Memory used by small_tuple: {sys.getsizeof(small_tuple)} bytes")
print(f"Memory used by equivalent list: {sys.getsizeof(small_list)} bytes")

# Tuples generally use less memory than lists because they're immutable
# and don't need to allocate extra space for potential growth

print("\n5. Tuple as dictionary keys:")
# Since tuples are immutable, they can be used as dictionary keys
coordinate_values = {
    (0, 0): "Origin",
    (1, 0): "East",
    (0, 1): "North",
    (1, 1): "Northeast"
}

print(f"Value at origin: {coordinate_values[(0, 0)]}")
print(f"All coordinates: {coordinate_values}")

# Lists cannot be used as dictionary keys because they're mutable
try:
    bad_dict = {[1, 2]: "value"}  # This will raise TypeError
except TypeError as e:
    print(f"Error using list as key: {e}")

print("=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

print("\n1. Using tuples for multiple assignment:")
# Swap values without temporary variable
a, b = 10, 20
print(f"Before swap: a={a}, b={b}")
a, b = b, a  # Tuple packing and unpacking for swapping
print(f"After swap: a={a}, b={b}")

# Multiple assignment
x, y, z = 1, 2, 3
print(f"Multiple assignment: x={x}, y={y}, z={z}")

print("\n2. Using tuples to return multiple values from a function:")
def find_min_max(numbers):
    return min(numbers), max(numbers)

result = find_min_max([5, 3, 8, 1, 9, 2])
print(f"Result tuple: {result}")

# Unpack immediately
min_val, max_val = find_min_max([5, 3, 8, 1, 9, 2])
print(f"Min: {min_val}, Max: {max_val}")

print("\n3. Using tuples for data integrity:")
def get_user_data():
    # Using a tuple ensures the data structure can't be modified
    return ("John Doe", 30, "john@example.com")

user_data = get_user_data()
print(f"User data: {user_data}")

# If we need to modify, we create a new tuple
name, age, email = user_data
updated_user_data = (name, age + 1, email)  # Increment age
print(f"Updated user data: {updated_user_data}")

print("\n4. Using tuples in a database context:")
# Tuples are often used to represent database records
users = [
    (1, "Alice", "alice@example.com"),
    (2, "Bob", "bob@example.com"),
    (3, "Charlie", "charlie@example.com")
]

print("User database:")
for user_id, name, email in users:  # Unpacking in a loop
    print(f"  ID: {user_id}, Name: {name}, Email: {email}")

print("\n5. Using named tuples for clearer code:")
from collections import namedtuple

# Define a structure for a student record
Student = namedtuple('Student', ['id', 'name', 'gpa'])

# Create student records
students = [
    Student(1, "Alice", 3.9),
    Student(2, "Bob", 3.7),
    Student(3, "Charlie", 4.0)
]

# Find the student with the highest GPA
top_student = max(students, key=lambda s: s.gpa)
print(f"Top student: {top_student.name} with GPA {top_student.gpa}")

# Calculate average GPA
avg_gpa = sum(student.gpa for student in students) / len(students)
print(f"Average GPA: {avg_gpa:.2f}")

print("\n6. Using tuples for function arguments:")
# Tuples can be used with * to pass multiple arguments to a function
def add(a, b, c):
    return a + b + c

values = (1, 2, 3)
result = add(*values)  # Unpacks the tuple into the function arguments
print(f"Result of add(*{values}): {result}")

print("=" * 50)
print("IMPORTANT NOTES")
print("=" * 50)

print("""
1. Tuples are ordered collections that can contain elements of different types.

2. Tuples are immutable - you cannot change, add, or remove elements after creation.

3. Tuple indices start at 0, and negative indices count from the end (-1 is the last element).

4. Tuples have only two methods: count() and index().

5. Tuples are more memory-efficient than lists and have a slightly faster performance.

6. Use tuples for heterogeneous data (different types) and lists for homogeneous data (same type).

7. Tuples can be used as dictionary keys because they're immutable.

8. Named tuples provide a way to create simple, immutable classes with named fields.

9. When creating a singleton tuple, remember to include a trailing comma: (1,)

10. Tuple unpacking is a powerful feature for working with multiple return values.
""")

print("\nWhen to use tuples:")
print("""
1. When you need an immutable sequence
2. When you want to ensure data integrity (values that shouldn't change)
3. As dictionary keys (lists can't be used as keys)
4. For returning multiple values from a function
5. For heterogeneous data collections (items of different types)
6. When you want a slightly more memory-efficient data structure than a list
""")

print("\nWhen to use named tuples:")
print("""
1. When you need a lightweight, immutable object type
2. As an alternative to a simple class with just attributes and no methods
3. When you want both tuple-like efficiency and the readability of attribute names
4. For representing database records or CSV data
5. When you need hashable objects (can be used in sets or as dictionary keys)
""")

print("\nTuple vs List:")
print("""
Feature         | Tuple          | List
----------------|----------------|------------------
Mutability      | Immutable      | Mutable
Syntax          | (1, 2, 3)      | [1, 2, 3]
Methods         | Only 2         | Many (append, insert, etc.)
Performance     | Slightly faster | Slightly slower
Memory usage    | Less           | More
Use as dict key | Yes            | No
Typical use     | Heterogeneous  | Homogeneous data
                | data (records) | (collections of same type)
""")

print("\nThank you for learning about Python tuples!")