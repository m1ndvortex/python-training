# Python List Tutorial
# ===================

# A list is an ordered, mutable collection of elements.
# Lists can contain elements of different types and allow duplicates.

print("=" * 50)
print("LIST BASICS")
print("=" * 50)

# Creating lists
print("\n1. Creating lists:")

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with initial values
numbers = [1, 2, 3, 4, 5]
print(f"Numbers list: {numbers}")

# Mixed types
mixed = [1, "hello", 3.14, True, [1, 2, 3]]
print(f"Mixed types list: {mixed}")

# Using list() constructor
chars = list("hello")  # Creates a list of characters
print(f"Characters list: {chars}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares list: {squares}")

# Creating a list of repeated values
repeated = [0] * 5
print(f"Repeated list: {repeated}")

print("\n2. Accessing list elements:")
# Indexing (0-based)
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")  # Negative indexing starts from the end

# Slicing [start:end:step]
print(f"First three fruits: {fruits[0:3]}")  # or fruits[:3]
print(f"Last three fruits: {fruits[-3:]}")
print(f"Every other fruit: {fruits[::2]}")
print(f"Reversed list: {fruits[::-1]}")

print("\n3. Modifying lists:")
# Lists are mutable - we can change their content
colors = ["red", "green", "blue"]
print(f"Original colors: {colors}")

# Changing an element
colors[1] = "yellow"
print(f"After changing element: {colors}")

# Adding elements
colors.append("purple")  # Add to the end
print(f"After append(): {colors}")

colors.insert(1, "orange")  # Insert at specific position
print(f"After insert(): {colors}")

colors.extend(["pink", "brown"])  # Add multiple elements
print(f"After extend(): {colors}")

# Removing elements
colors.remove("yellow")  # Remove by value (first occurrence)
print(f"After remove(): {colors}")

popped = colors.pop()  # Remove and return the last element
print(f"Popped element: {popped}")
print(f"After pop(): {colors}")

popped_index = colors.pop(1)  # Remove and return element at index
print(f"Popped element at index 1: {popped_index}")
print(f"After pop(1): {colors}")

# Clear the list
colors.clear()
print(f"After clear(): {colors}")

print("\n4. List operations:")
a = [1, 2, 3]
b = [4, 5, 6]

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

print("=" * 50)
print("LIST METHODS")
print("=" * 50)

print("\n1. Common list methods:")
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"Original list: {numbers}")

# Sorting
numbers.sort()  # In-place sort
print(f"After sort(): {numbers}")

numbers.sort(reverse=True)  # Descending sort
print(f"After sort(reverse=True): {numbers}")

# Note: sorted() returns a new sorted list instead of modifying the original
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(f"Original: {original}")
print(f"sorted(original): {sorted_list}")

# Reversing
numbers.reverse()  # In-place reverse
print(f"After reverse(): {numbers}")

# Counting occurrences
print(f"Count of 5: {numbers.count(5)}")

# Finding index of first occurrence
print(f"Index of 5: {numbers.index(5)}")
# print(f"Index of 7: {numbers.index(7)}")  # Would raise ValueError if element not found

# Safe way to find index
element = 7
if element in numbers:
    print(f"Index of {element}: {numbers.index(element)}")
else:
    print(f"{element} not found in the list")

# Copy
numbers_copy = numbers.copy()  # Same as numbers[:] or list(numbers)
print(f"Copy of numbers: {numbers_copy}")
print(f"Is it the same object? {numbers is numbers_copy}")  # False

print("\n2. Advanced sorting:")
# Sorting with key function
words = ["apple", "Banana", "cherry", "Date", "elderberry"]
print(f"Original words: {words}")

# Sort by lowercase string
words.sort(key=str.lower)
print(f"Sorted case-insensitive: {words}")

# Sort by length
words.sort(key=len)
print(f"Sorted by length: {words}")

# Sort by custom criteria
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "David", "grade": 85}
]

# Sort by grade (descending), then by name (ascending) for ties
students.sort(key=lambda x: (-x["grade"], x["name"]))
print("Students sorted by grade (desc) and name (asc):")
for student in students:
    print(f"  {student['name']}: {student['grade']}")

print("=" * 50)
print("ADVANCED LIST OPERATIONS")
print("=" * 50)

print("\n1. List comprehensions:")
# Basic syntax: [expression for item in iterable if condition]

# Simple example: squares of numbers
squares = [x**2 for x in range(1, 11)]
print(f"Squares: {squares}")

# With condition: even squares only
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested list comprehension: flattening a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

# Creating a matrix with list comprehension
matrix = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
print("Generated 3x3 matrix:")
for row in matrix:
    print(f"  {row}")

print("\n2. List as a stack and queue:")
# Stack (Last-In-First-Out)
print("Stack operations:")
stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)
print(f"  Stack after pushes: {stack}")
print(f"  Popped: {stack.pop()}")  # Pop
print(f"  Stack after pop: {stack}")

# Queue (First-In-First-Out)
print("\nQueue operations:")
from collections import deque
queue = deque([])
queue.append(1)  # Enqueue
queue.append(2)
queue.append(3)
print(f"  Queue after enqueues: {queue}")
print(f"  Dequeued: {queue.popleft()}")  # Dequeue
print(f"  Queue after dequeue: {queue}")

print("\n3. List and memory management:")
# Shallow vs Deep copy
import copy

original = [1, 2, [3, 4]]
shallow = original.copy()  # or list(original) or original[:]
deep = copy.deepcopy(original)

# Modify nested list
original[2][0] = 30

print(f"Original: {original}")
print(f"Shallow copy: {shallow}")  # Nested list change is reflected
print(f"Deep copy: {deep}")  # No changes reflected

print("\n4. List performance considerations:")
# Time complexity:
# - Access by index: O(1)
# - Search (in operator): O(n)
# - Insertion/deletion at beginning/middle: O(n)
# - Insertion/deletion at end: O(1) amortized
# - Sort: O(n log n)

# Memory usage example
import sys
small_list = [1, 2, 3]
print(f"Memory used by small_list: {sys.getsizeof(small_list)} bytes")

# NOTE: Lists are dynamic arrays with over-allocation
# When a list grows beyond its current capacity, Python:
# 1. Allocates a new, larger array (typically 1.125x for small lists)
# 2. Copies all elements to the new array
# 3. Deallocates the old array

# This is why appending to a list is amortized O(1) - most appends are fast,
# but occasionally a resize operation occurs which is O(n)

print("\n5. List slicing and assignment:")
# Slicing creates a new list (shallow copy)
a = [1, 2, 3, 4, 5]
b = a[1:4]  # New list with elements at index 1, 2, 3
print(f"a: {a}")
print(f"b = a[1:4]: {b}")

# Slice assignment
a[1:4] = [20, 30]  # Replace multiple elements with new ones
print(f"After a[1:4] = [20, 30]: {a}")

# Extended slice assignment
a[::2] = [100, 300]  # Replace every other element
print(f"After a[::2] = [100, 300]: {a}")

print("=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

print("\n1. Filtering and transforming data:")
data = [10, -5, 8, -3, 0, 12, -7, 15]

# Filter positive numbers and double them
result = [x * 2 for x in data if x > 0]
print(f"Positive numbers doubled: {result}")

# Alternative using filter() and map()
positives = list(filter(lambda x: x > 0, data))
doubled = list(map(lambda x: x * 2, positives))
print(f"Same result using filter/map: {doubled}")

print("\n2. Finding unique elements while preserving order:")
# Using a dictionary to track seen items (Python 3.7+ dictionaries preserve insertion order)
def unique_ordered(items):
    return list(dict.fromkeys(items))

duplicates = [1, 5, 2, 1, 9, 1, 5, 10]
print(f"Original list: {duplicates}")
print(f"Unique ordered: {unique_ordered(duplicates)}")

print("\n3. Implementing a moving average:")
def moving_average(data, window_size):
    results = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        window_avg = sum(window) / window_size
        results.append(window_avg)
    return results

temperatures = [22, 25, 23, 24, 27, 28, 26, 29]
print(f"Temperatures: {temperatures}")
print(f"3-day moving average: {moving_average(temperatures, 3)}")

print("\n4. Implementing a simple matrix multiplication:")
def matrix_multiply(A, B):
    # Ensure dimensions are compatible
    if len(A[0]) != len(B):
        return "Incompatible dimensions"
    
    # Create result matrix filled with zeros
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    # Perform multiplication
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(f"Matrix A: {A}")
print(f"Matrix B: {B}")
print("A × B:")
for row in matrix_multiply(A, B):
    print(f"  {row}")

print("\n5. Implementing a simple priority queue:")
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    
    def push(self, item, priority):
        # Lower values = higher priority
        # Use _index to break ties and maintain FIFO order for same priority
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
    
    def pop(self):
        if self._queue:
            return heapq.heappop(self._queue)[2]
        raise IndexError("pop from an empty priority queue")
    
    def is_empty(self):
        return len(self._queue) == 0

# Example usage
pq = PriorityQueue()
pq.push("task1", 3)
pq.push("task2", 1)
pq.push("task3", 2)
pq.push("task4", 1)  # Same priority as task2, but added later

print("Items popped from priority queue in priority order:")
while not pq.is_empty():
    print(f"  {pq.pop()}")  # Should print: task2, task4, task3, task1

print("=" * 50)
print("IMPORTANT NOTES")
print("=" * 50)

print("""
1. Lists are ordered collections that can contain elements of different types.

2. Lists are mutable - you can change, add, and remove elements after creation.

3. List indices start at 0, and negative indices count from the end (-1 is the last element).

4. Slicing creates a new list (shallow copy) - the original list is not modified.

5. List methods that modify the list (sort, reverse, append, etc.) return None, not the modified list.

6. For large lists, consider using array.array or numpy.array for better performance with numeric data.

7. When frequently adding/removing from the beginning of a list, consider using collections.deque instead.

8. List comprehensions are generally faster and more readable than equivalent for loops.

9. Be careful with mutable default arguments in functions:
   def bad_idea(value, my_list=[]):  # my_list is created once when function is defined
       my_list.append(value)
       return my_list
   
   # Better approach:
   def good_idea(value, my_list=None):
       if my_list is None:
           my_list = []
       my_list.append(value)
       return my_list

10. When sorting complex objects, use the key parameter rather than cmp_to_key (which is slower).
""")

print("\nAdditional list-like collections:")

# array - more efficient for large collections of numeric data
print("\narray example:")
import array
# 'i' represents signed integer
int_array = array.array('i', [1, 2, 3, 4, 5])
print(f"Integer array: {int_array}")
print(f"First element: {int_array[0]}")
int_array.append(6)
print(f"After append: {int_array}")

# deque - efficient for adding/removing from both ends
print("\ndeque example:")
from collections import deque
d = deque([1, 2, 3])
print(f"Deque: {d}")
d.appendleft(0)  # Efficient prepend
d.append(4)      # Efficient append
print(f"After appendleft(0) and append(4): {d}")
print(f"popleft(): {d.popleft()}")  # Efficient removal from left
print(f"pop(): {d.pop()}")          # Efficient removal from right
print(f"After popleft() and pop(): {d}")

# For numerical computing, consider NumPy arrays
try:
    import numpy as np
    print("\nnumpy array example:")
    np_array = np.array([1, 2, 3, 4, 5])
    print(f"NumPy array: {np_array}")
    print(f"NumPy array + 10: {np_array + 10}")  # Vectorized operation
    print(f"NumPy array * 2: {np_array * 2}")    # Vectorized operation
    print(f"Mean: {np_array.mean()}")
except ImportError:
    print("\nNumPy is not installed. Install it with 'pip install numpy' for advanced array operations.")

print("\nThank you for learning about Python lists!")