# Python Stack Tutorial
# ====================

# A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
# Elements are added and removed from the same end, called the "top" of the stack.
# Main operations: push (add), pop (remove), peek (view top without removing)

print("=" * 50)
print("STACK BASICS")
print("=" * 50)

print("\n1. Stack Concept:")
print("""
A stack is like a stack of plates:
- You can only add or remove plates from the top
- The last plate added is the first one removed (LIFO)
- You can only see the top plate without disturbing the stack

Common operations:
- push: Add an element to the top
- pop: Remove and return the top element
- peek/top: View the top element without removing it
- is_empty: Check if the stack is empty
""")

print("\n2. Implementing a stack in Python:")
print("There are multiple ways to implement a stack in Python:")

# Using a list
print("\na) Using a Python list:")
stack_list = []

# Push operation
stack_list.append(1)
stack_list.append(2)
stack_list.append(3)
print(f"Stack after pushes: {stack_list}")

# Pop operation
popped = stack_list.pop()
print(f"Popped element: {popped}")
print(f"Stack after pop: {stack_list}")

# Peek operation
if stack_list:
    print(f"Top element: {stack_list[-1]}")

# Is empty check
print(f"Is stack empty? {len(stack_list) == 0}")

# Using collections.deque
print("\nb) Using collections.deque (more efficient):")
from collections import deque

stack_deque = deque()

# Push operation
stack_deque.append(1)
stack_deque.append(2)
stack_deque.append(3)
print(f"Stack after pushes: {stack_deque}")

# Pop operation
popped = stack_deque.pop()
print(f"Popped element: {popped}")
print(f"Stack after pop: {stack_deque}")

# Peek operation
if stack_deque:
    print(f"Top element: {stack_deque[-1]}")

# Is empty check
print(f"Is stack empty? {len(stack_deque) == 0}")

print("\n3. Creating a Stack class:")

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from an empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

# Using our Stack class
stack = Stack()
print("\nUsing our Stack class:")
stack.push(10)
stack.push(20)
stack.push(30)
print(f"Stack after pushes: {stack}")
print(f"Stack size: {stack.size()}")
print(f"Top element: {stack.peek()}")
print(f"Popped element: {stack.pop()}")
print(f"Stack after pop: {stack}")
print(f"Is stack empty? {stack.is_empty()}")

print("=" * 50)
print("STACK APPLICATIONS")
print("=" * 50)

print("\n1. Reversing a string or list:")
def reverse_string(text):
    stack = Stack()
    # Push all characters onto the stack
    for char in text:
        stack.push(char)
    
    # Pop characters to get them in reverse order
    reversed_text = ""
    while not stack.is_empty():
        reversed_text += stack.pop()
    
    return reversed_text

original = "Hello, World!"
reversed_str = reverse_string(original)
print(f"Original: {original}")
print(f"Reversed: {reversed_str}")

print("\n2. Checking balanced parentheses:")
def is_balanced(expression):
    stack = Stack()
    
    # Dictionary to store pairs of opening and closing brackets
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        # If it's an opening bracket, push to stack
        if char in '({[':
            stack.push(char)
        # If it's a closing bracket
        elif char in ')}]':
            # If stack is empty or brackets don't match, it's not balanced
            if stack.is_empty() or stack.pop() != brackets[char]:
                return False
    
    # If stack is empty, all brackets were matched
    return stack.is_empty()

expressions = [
    "(a + b) * (c - d)",
    "[(a + b) * {c - d}]",
    "((a + b) * (c - d)",
    "(a + b) * c - d)",
    "{[()]}"
]

print("Checking balanced parentheses:")
for expr in expressions:
    print(f"'{expr}' is {'balanced' if is_balanced(expr) else 'not balanced'}")

print("\n3. Converting decimal to binary:")
def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"
    
    stack = Stack()
    
    # Divide by 2 and push remainders
    while decimal_num > 0:
        remainder = decimal_num % 2
        stack.push(remainder)
        decimal_num //= 2
    
    # Pop to get binary digits in correct order
    binary = ""
    while not stack.is_empty():
        binary += str(stack.pop())
    
    return binary

numbers = [0, 5, 10, 42, 255]
print("Decimal to binary conversion:")
for num in numbers:
    print(f"{num} in binary: {decimal_to_binary(num)}")

print("\n4. Implementing undo functionality:")
class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = Stack()
    
    def add_text(self, new_text):
        # Save current state for undo
        self.undo_stack.push(self.text)
        # Update text
        self.text += new_text
    
    def delete_last_char(self):
        if self.text:
            # Save current state for undo
            self.undo_stack.push(self.text)
            # Remove last character
            self.text = self.text[:-1]
    
    def undo(self):
        if not self.undo_stack.is_empty():
            # Restore previous state
            self.text = self.undo_stack.pop()
    
    def get_text(self):
        return self.text

# Demonstrate text editor with undo
editor = TextEditor()
print("Text editor with undo functionality:")
editor.add_text("Hello")
print(f"After adding 'Hello': '{editor.get_text()}'")
editor.add_text(" World")
print(f"After adding ' World': '{editor.get_text()}'")
editor.delete_last_char()
print(f"After deleting last char: '{editor.get_text()}'")
editor.undo()
print(f"After first undo: '{editor.get_text()}'")
editor.undo()
print(f"After second undo: '{editor.get_text()}'")

print("=" * 50)
print("STACK VARIATIONS")
print("=" * 50)

print("\n1. Min Stack (stack that keeps track of minimum element):")
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        
        # If min_stack is empty or val is less than or equal to current min,
        # add val to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if not self.stack:
            return None
        
        val = self.stack.pop()
        
        # If popped value is the current minimum, remove from min_stack too
        if self.min_stack and val == self.min_stack[-1]:
            self.min_stack.pop()
            
        return val
    
    def top(self):
        if self.stack:
            return self.stack[-1]
        return None
    
    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None
    
    def __str__(self):
        return f"Stack: {self.stack}, Min: {self.get_min()}"

# Demonstrate MinStack
min_stack = MinStack()
print("MinStack demonstration:")
min_stack.push(5)
print(f"After push(5): {min_stack}")
min_stack.push(2)
print(f"After push(2): {min_stack}")
min_stack.push(7)
print(f"After push(7): {min_stack}")
min_stack.push(1)
print(f"After push(1): {min_stack}")
min_stack.pop()
print(f"After pop(): {min_stack}")
min_stack.pop()
print(f"After another pop(): {min_stack}")

print("\n2. Two-Stack Queue (implementing a queue using two stacks):")
class TwoStackQueue:
    def __init__(self):
        self.stack_newest = []  # for enqueue
        self.stack_oldest = []  # for dequeue
    
    def enqueue(self, value):
        self.stack_newest.append(value)
    
    def _shift_stacks(self):
        # If stack_oldest is empty, transfer all elements from stack_newest
        if not self.stack_oldest:
            while self.stack_newest:
                self.stack_oldest.append(self.stack_newest.pop())
    
    def dequeue(self):
        self._shift_stacks()
        if not self.stack_oldest:
            raise IndexError("Dequeue from an empty queue")
        return self.stack_oldest.pop()
    
    def peek(self):
        self._shift_stacks()
        if not self.stack_oldest:
            return None
        return self.stack_oldest[-1]
    
    def is_empty(self):
        return not self.stack_newest and not self.stack_oldest
    
    def size(self):
        return len(self.stack_newest) + len(self.stack_oldest)
    
    def __str__(self):
        if self.is_empty():
            return "Queue: []"
        
        # Create a temporary copy for display purposes
        temp_oldest = self.stack_oldest.copy()
        temp_newest = self.stack_newest.copy()
        
        # Reconstruct the queue order
        queue_items = []
        
        # Add oldest items first (in reverse order)
        for _ in range(len(temp_oldest)):
            queue_items.insert(0, temp_oldest.pop())
            
        # Add newest items
        queue_items.extend(reversed(temp_newest))
        
        return f"Queue: {queue_items}"

# Demonstrate TwoStackQueue
queue = TwoStackQueue()
print("TwoStackQueue demonstration:")
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(f"After enqueues: {queue}")
print(f"Dequeued: {queue.dequeue()}")
print(f"After dequeue: {queue}")
queue.enqueue(4)
print(f"After enqueue(4): {queue}")
print(f"Dequeued: {queue.dequeue()}")
print(f"Dequeued: {queue.dequeue()}")
print(f"After two dequeues: {queue}")

print("=" * 50)
print("PERFORMANCE CONSIDERATIONS")
print("=" * 50)

print("""
1. Time Complexity:
   - Push: O(1) - Adding to the top of the stack is a constant-time operation
   - Pop: O(1) - Removing from the top of the stack is a constant-time operation
   - Peek: O(1) - Viewing the top element is a constant-time operation
   - Search: O(n) - Finding an element may require checking all elements

2. Space Complexity:
   - O(n) where n is the number of elements in the stack

3. Implementation Considerations:
   - Python list: Simple but may have performance issues for very large stacks
     due to resizing operations
   - collections.deque: More efficient for large stacks as it's optimized for
     append and pop operations from both ends
   - Custom implementation: Provides more control but requires more code

4. When to use a stack:
   - When you need LIFO (Last-In-First-Out) behavior
   - For problems involving backtracking or recursion
   - When you need to reverse things
   - For parsing expressions or syntax checking
""")

print("=" * 50)
print("IMPORTANT NOTES")
print("=" * 50)

print("""
1. Stacks are fundamental data structures used in many algorithms and systems.

2. The key characteristic of a stack is its LIFO (Last-In-First-Out) behavior.

3. In Python, you can implement stacks using:
   - Lists (append/pop)
   - collections.deque (append/pop)
   - Custom Stack class

4. Common stack operations:
   - push: Add an element to the top
   - pop: Remove and return the top element
   - peek/top: View the top element without removing it
   - is_empty: Check if the stack is empty

5. Stacks are used in:
   - Function call management (call stack)
   - Expression evaluation and syntax parsing
   - Backtracking algorithms
   - Undo mechanisms
   - Browser history

6. When implementing a stack, be careful with:
   - Popping from an empty stack (check if empty first)
   - Stack overflow (if using a fixed-size implementation)

7. For most Python applications, using collections.deque is more efficient than a list
   for implementing a stack, especially for large data sets.
""")

print("\nThank you for learning about Python stacks!")