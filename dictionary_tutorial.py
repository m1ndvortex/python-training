# Python Dictionary Tutorial
# =========================

# A dictionary is a collection of key-value pairs.
# It is mutable, unordered, and indexed by keys.

print("=" * 50)
print("DICTIONARY BASICS")
print("=" * 50)

# Creating dictionaries
print("\n1. Creating dictionaries:")

# Empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")

# Dictionary with initial values
student = {
    "name": "John",
    "age": 20,
    "courses": ["Math", "Physics", "Computer Science"],
    "active": True
}
print(f"Student dictionary: {student}")

# Using dict() constructor
contact = dict(name="Alice", phone="123-456-7890", email="alice@example.com")
print(f"Contact dictionary: {contact}")

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares dictionary: {squares}")

# NOTE: Dictionary keys must be immutable (strings, numbers, tuples of immutables)
# This works:
valid_dict = {("a", 1): "tuple key is valid because tuples are immutable"}
print(f"Dictionary with tuple key: {valid_dict}")

# This would cause an error:
# invalid_dict = {["a", 1]: "list key is invalid because lists are mutable"}

print("\n2. Accessing dictionary values:")
# Accessing values using keys
print(f"Student name: {student['name']}")
print(f"Student age: {student['age']}")

# Using get() method (safer, returns None or default value if key doesn't exist)
print(f"Student grade: {student.get('grade')}")  # Returns None
print(f"Student grade (with default): {student.get('grade', 'N/A')}")  # Returns 'N/A'

print("\n3. Modifying dictionaries:")
# Adding or updating items
student["grade"] = "A"
print(f"After adding grade: {student}")

student["age"] = 21  # Update existing key
print(f"After updating age: {student}")

# Using update() method to add/update multiple items at once
student.update({"semester": "Fall", "year": 2023, "age": 22})
print(f"After update(): {student}")

print("\n4. Removing items:")
# pop() - removes item with specified key and returns its value
removed_age = student.pop("age")
print(f"Removed age: {removed_age}")
print(f"After pop('age'): {student}")

# popitem() - removes and returns the last inserted key-value pair as a tuple
last_item = student.popitem()
print(f"Last item removed: {last_item}")
print(f"After popitem(): {student}")

# del - removes item with specified key
del student["active"]
print(f"After del student['active']: {student}")

# clear() - removes all items
contact.clear()
print(f"After clear(): {contact}")

print("=" * 50)
print("DICTIONARY METHODS")
print("=" * 50)

# Recreate the student dictionary
student = {
    "name": "John",
    "age": 20,
    "courses": ["Math", "Physics", "Computer Science"],
    "active": True,
    "grade": "A"
}

print("\n1. Common dictionary methods:")

# keys() - returns a view object of all keys
keys = student.keys()
print(f"Keys: {keys}")
# Note: views are dynamic and reflect changes to the dictionary
student["semester"] = "Spring"
print(f"Keys after adding 'semester': {keys}")  # 'semester' is now in keys

# values() - returns a view object of all values
values = student.values()
print(f"Values: {values}")

# items() - returns a view object of all key-value pairs as tuples
items = student.items()
print(f"Items: {items}")

# copy() - returns a shallow copy of the dictionary
student_copy = student.copy()
print(f"Copy of student: {student_copy}")
print(f"Is it the same object? {student is student_copy}")  # False

# fromkeys() - creates a new dictionary with specified keys and value
new_student_template = dict.fromkeys(["name", "age", "major"], "Not Set")
print(f"Template from fromkeys(): {new_student_template}")

# setdefault() - returns value of specified key, if key doesn't exist inserts key with specified value
print(f"setdefault('name'): {student.setdefault('name', 'Unknown')}")  # Returns 'John' (existing)
print(f"setdefault('address', 'Unknown'): {student.setdefault('address', 'Unknown')}")  # Adds key with default
print(f"After setdefault(): {student}")

print("=" * 50)
print("ADVANCED DICTIONARY OPERATIONS")
print("=" * 50)

print("\n1. Dictionary unpacking:")
# Unpacking dictionaries
defaults = {"language": "Python", "level": "Beginner"}
preferences = {"theme": "Dark", "level": "Advanced"}
# The ** operator unpacks dictionaries - later values override earlier ones for duplicate keys
settings = {**defaults, **preferences}
print(f"Unpacked dictionaries: {settings}")  # 'level' from preferences overrides the one from defaults

print("\n2. Nested dictionaries:")
# Dictionaries can contain other dictionaries
university = {
    "name": "Tech University",
    "departments": {
        "CS": {"head": "Dr. Smith", "students": 200},
        "Math": {"head": "Dr. Johnson", "students": 150}
    },
    "location": "New York"
}
print(f"University: {university}")
print(f"CS department head: {university['departments']['CS']['head']}")

print("\n3. Dictionary as a switch/case:")
# Dictionaries can be used as an alternative to switch/case statements
def perform_operation(a, b, operation):
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else "Cannot divide by zero"
    }
    # Get the function and call it with a and b, or return error message
    return operations.get(operation, lambda x, y: "Invalid operation")(a, b)

print(f"10 + 5 = {perform_operation(10, 5, 'add')}")
print(f"10 - 5 = {perform_operation(10, 5, 'subtract')}")
print(f"10 * 5 = {perform_operation(10, 5, 'multiply')}")
print(f"10 / 5 = {perform_operation(10, 5, 'divide')}")
print(f"10 / 0 = {perform_operation(10, 0, 'divide')}")
print(f"10 % 5 = {perform_operation(10, 5, 'modulo')}")  # Invalid operation

print("\n4. Dictionary and memory management:")
# Shallow vs Deep copy
import copy

original = {
    "name": "John",
    "scores": [90, 85, 88],
    "address": {"city": "New York", "zip": "10001"}
}

# Shallow copy - nested objects are shared
shallow = original.copy()  # or dict(original) or {**original}

# Deep copy - nested objects are also copied
deep = copy.deepcopy(original)

# Modify nested objects
original["scores"].append(95)
original["address"]["zip"] = "10002"

print(f"Original: {original}")
print(f"Shallow copy: {shallow}")  # scores and address changes are reflected
print(f"Deep copy: {deep}")  # No changes reflected

print("\n5. Dictionary performance considerations:")
# Dictionaries are highly optimized hash tables
# Time complexity:
# - Access, insertion, update, deletion: O(1) average case
# - Iteration: O(n) where n is the size of the dictionary

# Memory usage example
import sys
small_dict = {"a": 1, "b": 2, "c": 3}
print(f"Memory used by small_dict: {sys.getsizeof(small_dict)} bytes")

# NOTE: Python dictionaries preserve insertion order since Python 3.7
# This is an implementation detail in CPython 3.6 and a language feature in 3.7+
ordered_dict = {}
for i in range(5):
    ordered_dict[i] = i * 10
print(f"Ordered dictionary: {ordered_dict}")
print(f"Keys in order: {list(ordered_dict.keys())}")

print("=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

print("\n1. Counting word frequency:")
text = "the quick brown fox jumps over the lazy dog the fox was quick"
word_count = {}

for word in text.split():
    # Increment count for word, starting at 0 if word not seen before
    word_count[word] = word_count.get(word, 0) + 1

print(f"Word frequency: {word_count}")

print("\n2. Grouping data:")
students = [
    {"name": "Alice", "grade": "A", "course": "Math"},
    {"name": "Bob", "grade": "B", "course": "Physics"},
    {"name": "Charlie", "grade": "A", "course": "Math"},
    {"name": "David", "grade": "C", "course": "Physics"},
    {"name": "Eve", "grade": "B", "course": "Math"}
]

# Group students by course
by_course = {}
for student in students:
    course = student["course"]
    if course not in by_course:
        by_course[course] = []
    by_course[course].append(student["name"])

print(f"Students by course: {by_course}")

# Group students by grade using a more concise approach with setdefault
by_grade = {}
for student in students:
    by_grade.setdefault(student["grade"], []).append(student["name"])

print(f"Students by grade: {by_grade}")

print("\n3. Caching/Memoization:")
# Using a dictionary to cache expensive function results

def fibonacci_with_cache(n, cache={}):
    # Check if we have already computed this value
    if n in cache:
        return cache[n]
    
    # Base cases
    if n <= 1:
        result = n
    else:
        # Recursive case with caching
        result = fibonacci_with_cache(n-1, cache) + fibonacci_with_cache(n-2, cache)
    
    # Store result in cache before returning
    cache[n] = result
    return result

print("Computing Fibonacci numbers with caching:")
for i in range(10):
    print(f"fibonacci({i}) = {fibonacci_with_cache(i)}")

print("\n4. Dictionary as a simple database:")
# Using a dictionary to store and query data
users_db = {
    "user1": {
        "username": "john_doe",
        "email": "john@example.com",
        "active": True,
        "posts": [101, 102, 103]
    },
    "user2": {
        "username": "jane_smith",
        "email": "jane@example.com",
        "active": False,
        "posts": [104, 105]
    }
}

# Query: Find all active users
active_users = [user_data["username"] for user_id, user_data in users_db.items() 
                if user_data["active"]]
print(f"Active users: {active_users}")

# Query: Count total posts
total_posts = sum(len(user_data["posts"]) for user_data in users_db.values())
print(f"Total posts: {total_posts}")

print("=" * 50)
print("IMPORTANT NOTES")
print("=" * 50)

print("""
1. Dictionary keys must be immutable (strings, numbers, tuples of immutables).

2. Since Python 3.7, dictionaries maintain insertion order. Before that, they were unordered.

3. Dictionary operations are generally very fast (O(1) for lookups, insertions, and deletions).

4. For ordered dictionaries with additional functionality, consider collections.OrderedDict.

5. For dictionaries with default values, consider collections.defaultdict.

6. For counting elements, consider collections.Counter.

7. When iterating through a dictionary during modification, use a list to store the keys first:
   for key in list(my_dict.keys()):
       # Now you can modify my_dict safely

8. Memory usage: Dictionaries have some overhead, so they use more memory than lists for the same data.

9. Dictionary comprehensions provide a concise way to create dictionaries.

10. The dict.get() method is safer than direct key access when keys might not exist.
""")

print("\nAdditional collections from the collections module:")
import collections

# defaultdict - dictionary with default factory for missing keys
print("\ndefaultdict example:")
word_lengths = collections.defaultdict(int)
for word in "the quick brown fox jumps over the lazy dog".split():
    word_lengths[word] = len(word)
print(f"Word lengths: {dict(word_lengths)}")
print(f"Missing key returns: {word_lengths['missing']}")  # Returns 0 (default for int)

# Counter - specialized dictionary for counting hashable objects
print("\nCounter example:")
inventory = collections.Counter(["apple", "orange", "apple", "banana", "apple", "orange"])
print(f"Inventory count: {inventory}")
print(f"Most common items: {inventory.most_common(2)}")

# OrderedDict - dictionary that remembers insertion order (less important since Python 3.7)
print("\nOrderedDict example:")
ordered = collections.OrderedDict([('first', 1), ('second', 2), ('third', 3)])
print(f"OrderedDict: {ordered}")
ordered.move_to_end('first')  # Move 'first' to the end
print(f"After move_to_end: {ordered}")

print("\nThank you for learning about Python dictionaries!")