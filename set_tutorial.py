# Python Set Tutorial
# =================

# A set is an unordered collection of unique elements.
# Sets are mutable, but can only contain immutable (hashable) elements.

print("=" * 50)
print("SET BASICS")
print("=" * 50)

# Creating sets
print("\n1. Creating sets:")

# Empty set (note: {} creates an empty dictionary, not a set)
empty_set = set()
print(f"Empty set: {empty_set}")

# Set with initial values
numbers = {1, 2, 3, 4, 5}
print(f"Numbers set: {numbers}")

# Set from an iterable
fruits = set(["apple", "banana", "cherry", "apple"])  # Note: duplicates are removed
print(f"Fruits set: {fruits}")

# Set comprehension
even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares set: {even_squares}")

# NOTE: Sets can only contain hashable (immutable) elements
# This works:
valid_set = {1, 2, "hello", (1, 2)}  # Integers, strings, and tuples are hashable
print(f"Valid set: {valid_set}")

# This would cause an error:
# invalid_set = {1, 2, [3, 4]}  # Lists are mutable, so they're not hashable

print("\n2. Basic set operations:")
# Checking membership
print(f"Is 'apple' in fruits? {'apple' in fruits}")
print(f"Is 'orange' in fruits? {'orange' in fruits}")

# Length of a set
print(f"Number of fruits: {len(fruits)}")

# Adding elements
fruits.add("orange")
print(f"After adding 'orange': {fruits}")

# Adding multiple elements
fruits.update(["grape", "kiwi", "orange"])  # Note: duplicates are ignored
print(f"After update(): {fruits}")

# Removing elements
fruits.remove("banana")  # Raises KeyError if element doesn't exist
print(f"After remove('banana'): {fruits}")

# Safe removal
fruits.discard("mango")  # No error if element doesn't exist
print(f"After discard('mango'): {fruits}")

# Pop (remove and return an arbitrary element)
popped = fruits.pop()
print(f"Popped element: {popped}")
print(f"After pop(): {fruits}")

# Clear (remove all elements)
temp_set = {1, 2, 3}
temp_set.clear()
print(f"After clear(): {temp_set}")

print("=" * 50)
print("SET OPERATIONS (MATHEMATICAL)")
print("=" * 50)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(f"Set A: {A}")
print(f"Set B: {B}")

# Union (elements in either A or B)
print(f"A ∪ B (union): {A | B}")  # Using operator
print(f"A.union(B): {A.union(B)}")  # Using method

# Intersection (elements in both A and B)
print(f"A ∩ B (intersection): {A & B}")  # Using operator
print(f"A.intersection(B): {A.intersection(B)}")  # Using method

# Difference (elements in A but not in B)
print(f"A - B (difference): {A - B}")  # Using operator
print(f"A.difference(B): {A.difference(B)}")  # Using method

# Symmetric difference (elements in either A or B but not in both)
print(f"A △ B (symmetric difference): {A ^ B}")  # Using operator
print(f"A.symmetric_difference(B): {A.symmetric_difference(B)}")  # Using method

# Subset and superset
C = {1, 2, 3}
print(f"Set C: {C}")
print(f"Is C a subset of A? {C <= A}")  # Using operator
print(f"C.issubset(A): {C.issubset(A)}")  # Using method

print(f"Is A a superset of C? {A >= C}")  # Using operator
print(f"A.issuperset(C): {A.issuperset(C)}")  # Using method

# Proper subset/superset (strict subset/superset)
print(f"Is C a proper subset of A? {C < A}")  # Using operator
print(f"Is A a proper superset of C? {A > C}")  # Using operator

# Disjoint sets (no common elements)
D = {10, 11, 12}
print(f"Set D: {D}")
print(f"Are A and D disjoint? {A.isdisjoint(D)}")

print("=" * 50)
print("ADVANCED SET OPERATIONS")
print("=" * 50)

print("\n1. Set operations with multiple sets:")
E = {1, 2, 3}
F = {2, 3, 4}
G = {3, 4, 5}
print(f"Set E: {E}")
print(f"Set F: {F}")
print(f"Set G: {G}")

# Union of multiple sets
print(f"E ∪ F ∪ G: {E | F | G}")
print(f"Union of E, F, G: {set.union(E, F, G)}")

# Intersection of multiple sets
print(f"E ∩ F ∩ G: {E & F & G}")
print(f"Intersection of E, F, G: {set.intersection(E, F, G)}")

print("\n2. Updating sets in-place:")
X = {1, 2, 3, 4}
Y = {3, 4, 5, 6}
print(f"Original X: {X}")
print(f"Original Y: {Y}")

# Update (in-place union)
X_copy = X.copy()
X_copy.update(Y)  # or X_copy |= Y
print(f"X after update with Y: {X_copy}")

# Intersection update (in-place intersection)
X_copy = X.copy()
X_copy.intersection_update(Y)  # or X_copy &= Y
print(f"X after intersection_update with Y: {X_copy}")

# Difference update (in-place difference)
X_copy = X.copy()
X_copy.difference_update(Y)  # or X_copy -= Y
print(f"X after difference_update with Y: {X_copy}")

# Symmetric difference update (in-place symmetric difference)
X_copy = X.copy()
X_copy.symmetric_difference_update(Y)  # or X_copy ^= Y
print(f"X after symmetric_difference_update with Y: {X_copy}")

print("\n3. Frozen sets (immutable sets):")
# Frozen sets are immutable versions of sets
frozen = frozenset([1, 2, 3, 4])
print(f"Frozen set: {frozen}")

# Frozen sets can be used as dictionary keys or elements of another set
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Set of frozen sets: {set_of_sets}")

# Frozen sets support the same non-modifying operations as regular sets
print(f"Union of frozen sets: {frozen | {5, 6}}")
print(f"Intersection with {2, 3, 5}: {frozen & {2, 3, 5}}")

# But modifying operations will raise an error:
# frozen.add(5)  # This would raise AttributeError

print("\n4. Set performance considerations:")
# Time complexity:
# - Membership testing (x in s): O(1) average case
# - Add/remove: O(1) average case
# - Union/intersection/difference: O(len(s) + len(t)) where s and t are the sets

# Memory usage example
import sys
small_set = {1, 2, 3}
print(f"Memory used by small_set: {sys.getsizeof(small_set)} bytes")

# Sets use more memory than lists for the same elements due to the hash table,
# but provide O(1) membership testing, which is O(n) for lists

print("=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

print("\n1. Removing duplicates from a list:")
duplicates = [1, 2, 3, 1, 2, 4, 5, 4, 6]
unique = list(set(duplicates))
print(f"Original list: {duplicates}")
print(f"List with duplicates removed: {unique}")
# Note: This doesn't preserve the original order. If order matters, use:
# unique_ordered = list(dict.fromkeys(duplicates))

print("\n2. Finding common elements:")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Common elements: {common}")

print("\n3. Finding unique elements (elements in only one list):")
unique_to_list1 = set(list1) - set(list2)
unique_to_list2 = set(list2) - set(list1)
print(f"Elements unique to list 1: {unique_to_list1}")
print(f"Elements unique to list 2: {unique_to_list2}")
print(f"Elements in exactly one list: {unique_to_list1 | unique_to_list2}")  # Symmetric difference

print("\n4. Set operations for data analysis:")
# Example: Analyzing survey responses
python_users = {"Alice", "Bob", "Charlie", "David", "Eve"}
java_users = {"Bob", "Charlie", "Frank", "Grace", "Heidi"}
javascript_users = {"Alice", "Charlie", "David", "Frank", "Ivy"}

print(f"Python users: {python_users}")
print(f"Java users: {java_users}")
print(f"JavaScript users: {javascript_users}")

# Users who know all three languages
all_three = python_users & java_users & javascript_users
print(f"Users who know all three languages: {all_three}")

# Users who know at least one language
at_least_one = python_users | java_users | javascript_users
print(f"Total unique users: {at_least_one}")

# Users who know Python but not Java
python_not_java = python_users - java_users
print(f"Python users who don't know Java: {python_not_java}")

# Users who know exactly one language
only_python = python_users - (java_users | javascript_users)
only_java = java_users - (python_users | javascript_users)
only_javascript = javascript_users - (python_users | java_users)
exactly_one = only_python | only_java | only_javascript
print(f"Users who know exactly one language: {exactly_one}")

print("\n5. Using sets for graph algorithms:")
# Representing a graph using sets
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

# Finding all neighbors of a node
node = 'B'
print(f"Neighbors of {node}: {graph[node]}")

# Finding all nodes that are two steps away
two_steps = set()
for neighbor in graph[node]:
    two_steps.update(graph[neighbor])
# Remove the starting node and its direct neighbors
two_steps -= {node} | graph[node]
print(f"Nodes two steps away from {node}: {two_steps}")

print("\n6. Implementing a simple spell checker:")
dictionary = {"apple", "banana", "cherry", "date", "elderberry", "fig", "grape"}

def check_spelling(word, dictionary):
    if word in dictionary:
        return f"'{word}' is spelled correctly."
    
    # Simple suggestion algorithm: words with one character different
    suggestions = []
    for dict_word in dictionary:
        if len(word) == len(dict_word):
            # Count differences
            differences = sum(1 for a, b in zip(word, dict_word) if a != b)
            if differences == 1:
                suggestions.append(dict_word)
    
    if suggestions:
        return f"'{word}' not found. Did you mean: {', '.join(suggestions)}?"
    else:
        return f"'{word}' not found. No suggestions available."

print(check_spelling("apple", dictionary))
print(check_spelling("appla", dictionary))
print(check_spelling("orange", dictionary))

print("=" * 50)
print("IMPORTANT NOTES")
print("=" * 50)

print("""
1. Sets are unordered collections of unique elements.

2. Set elements must be hashable (immutable) - strings, numbers, tuples of immutables, frozensets.

3. Sets are mutable - you can add and remove elements after creation.

4. Sets are optimized for membership testing, removing duplicates, and mathematical set operations.

5. Set operations are generally very fast (O(1) for lookups, insertions, and deletions).

6. The empty set must be created using set(), not {} (which creates an empty dictionary).

7. Sets don't support indexing, slicing, or other sequence operations.

8. For an immutable version of a set, use frozenset.

9. Set comprehensions provide a concise way to create sets.

10. When comparing sets, == tests for equality of elements, while is tests for identity (same object).
""")

print("\nCommon set operations and their method equivalents:")
print("""
Operation          | Operator | Method                  | In-place Method
-------------------|----------|-------------------------|------------------
Union              | s | t    | s.union(t)              | s.update(t)
Intersection       | s & t    | s.intersection(t)       | s.intersection_update(t)
Difference         | s - t    | s.difference(t)         | s.difference_update(t)
Symmetric Diff     | s ^ t    | s.symmetric_difference(t)| s.symmetric_difference_update(t)
Subset             | s <= t   | s.issubset(t)           | N/A
Proper Subset      | s < t    | N/A                     | N/A
Superset           | s >= t   | s.issuperset(t)         | N/A
Proper Superset    | s > t    | N/A                     | N/A
Disjoint           | N/A      | s.isdisjoint(t)         | N/A
""")

print("\nWhen to use sets:")
print("""
1. When you need to ensure elements are unique
2. When you need fast membership testing
3. When you need to perform mathematical set operations
4. When the order of elements doesn't matter
5. When you need to eliminate duplicates from a collection
""")

print("\nWhen NOT to use sets:")
print("""
1. When you need to maintain element order (use lists or OrderedDict)
2. When you need to store mutable elements (use another data structure)
3. When you need duplicate elements (use lists)
4. When you need to access elements by index (use lists)
""")

print("\nThank you for learning about Python sets!")