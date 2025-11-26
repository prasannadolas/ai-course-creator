# Module 4: Stacks, Queues, and Recursion

## Introduction

In this module, we'll explore two important abstract data types (ADTs): **stacks** and **queues**, along with the powerful programming technique of **recursion**. **Stacks** and **queues** are fundamental data structures that follow specific access patterns, making them suitable for various problems. **Recursion** provides an elegant way to solve problems by breaking them down into smaller, self-similar subproblems.

## Stacks

A **stack** is an ADT that follows the **LIFO** (Last-In, First-Out) principle. Think of it like a stack of plates: the last plate you put on the stack is the first one you take off.

**Key Concepts:**

*   **LIFO (Last-In, First-Out):** The last element added to the stack is the first one removed.
*   **Operations:**
    *   **Push:** Adds an element to the top of the stack.
    *   **Pop:** Removes and returns the element from the top of the stack.
    *   **Peek (or Top):** Returns the top element without removing it.
    *   **IsEmpty:** Checks if the stack is empty.

**Implementation (using Python Lists):**

Python's built-in lists can be used to implement stacks easily. The end of the list is used as the "top" of the stack.

```python
class Stack:
    def __init__(self):
        self.items = [] # Underlying list to hold stack items.

    def is_empty(self):
        return len(self.items) == 0 # Returns true if the list is empty

    def push(self, item):
        self.items.append(item) # Adds an element to the end of the list

    def pop(self):
        if not self.is_empty():
            return self.items.pop() # Removes the last element from the list
        else:
            return None # Handle case when stack is empty

    def peek(self):
        if not self.is_empty():
            return self.items[-1] # Returns the last element in the list
        else:
            return None # Handle case when stack is empty

    def size(self):
        return len(self.items) # Returns number of elements in the stack
```

**Explanation:**

*   **`__init__(self)`:** Initializes an empty list (`self.items`) to store the stack elements.
*   **`is_empty(self)`:** Returns `True` if the underlying list is empty; otherwise, `False`.  This is **O(1)**.
*   **`push(self, item)`:** Appends an `item` to the end of the list (the "top" of the stack). This is **O(1)** (amortized).
*   **`pop(self)`:** Removes and returns the last element (the "top") from the list using `.pop()`. This is **O(1)**. Includes error handling if the stack is empty.
*   **`peek(self)`:** Returns the last element (the "top") without removing it. This is **O(1)**. Includes error handling if the stack is empty.
*   **`size(self)`:** Returns the current number of elements in the stack, which is **O(1)**.

**Use Cases for Stacks:**

*   **Function Call Stack:** When a function is called, its information (variables, return address) is pushed onto a stack. When the function finishes, it's popped off.
*   **Expression Evaluation:** Stacks are used to evaluate mathematical expressions (e.g., converting infix to postfix notation).
*   **Undo/Redo Functionality:** In text editors and other applications, stacks store the history of actions.
*   **Backtracking Algorithms:** Stacks can be used to keep track of choices in backtracking algorithms.

## Queues

A **queue** is an ADT that follows the **FIFO** (First-In, First-Out) principle. Think of it like a queue of people waiting in line: the first person in line is the first one served.

**Key Concepts:**

*   **FIFO (First-In, First-Out):** The first element added to the queue is the first one removed.
*   **Operations:**
    *   **Enqueue:** Adds an element to the rear (end) of the queue.
    *   **Dequeue:** Removes and returns the element from the front of the queue.
    *   **Peek (or Front):** Returns the element at the front without removing it.
    *   **IsEmpty:** Checks if the queue is empty.

**Implementation (using Python Lists with `deque`):**

```python
from collections import deque # Using deque for efficient queue operations

class Queue:
    def __init__(self):
        self.items = deque() # Use deque from the collections module

    def is_empty(self):
        return len(self.items) == 0 # Returns true if the queue is empty

    def enqueue(self, item):
        self.items.append(item) # Adds an element to the rear of the queue

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft() # Removes and returns the element from the front
        else:
            return None # Handle case when queue is empty

    def peek(self):
        if not self.is_empty():
            return self.items[0] # Returns the first element of the queue
        else:
            return None # Handle case when queue is empty

    def size(self):
        return len(self.items)
```

**Explanation:**

*   **`__init__(self)`:** Initializes a `deque` object from the `collections` module. `deque` is optimized for queue-like operations.
*   **`is_empty(self)`:** Returns `True` if the queue is empty; otherwise, `False` (O(1)).
*   **`enqueue(self, item)`:** Appends an `item` to the rear of the queue (O(1)).
*   **`dequeue(self)`:** Removes and returns the element from the front of the queue (O(1) with `deque`). Includes error handling.
*   **`peek(self)`:** Returns the element at the front of the queue (O(1)). Includes error handling.
*   **`size(self)`:** Returns the number of items in the queue (O(1))

**Use Cases for Queues:**

*   **Task Scheduling:** Operating systems use queues to manage processes waiting for the CPU.
*   **Breadth-First Search (BFS):** A graph traversal algorithm that uses a queue to explore nodes level by level.
*   **Printer Queues:** Managing print jobs.
*   **Simulations:** Modeling real-world scenarios where events occur in a specific order (e.g., customer service systems).

## Recursion

**Recursion** is a programming technique where a function calls itself within its own definition. It's a powerful tool for solving problems that can be broken down into smaller, self-similar subproblems.

**Key Concepts:**

*   **Base Case:** A condition that stops the recursion. Without a base case, recursion would lead to infinite loops (or stack overflow errors).
*   **Recursive Step:** The part of the function where it calls itself with a modified input, bringing it closer to the base case.

**Example: Factorial Calculation**

```python
def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.
    """
    if n == 0:  # Base case
        return 1
    else:  # Recursive step
        return n * factorial(n - 1)
```

**Explanation:**

*   **`factorial(n)`:** Calculates the factorial of `n` (n!).
*   **`if n == 0:`:** The base case. The factorial of 0 is defined as 1. If `n` is 0, the function returns 1.
*   **`else:`:** The recursive step. `factorial(n)` is defined as `n` multiplied by `factorial(n-1)`. This breaks down the problem into a smaller, self-similar subproblem. Each recursive call reduces `n` until it reaches the base case (n=0).

```python
print(factorial(5)) # Output: 120 (5 * 4 * 3 * 2 * 1)
```

**Example: Fibonacci Sequence**

```python
def fibonacci(n):
    """
    Calculates the nth Fibonacci number using recursion.
    """
    if n <= 1: # Base case
        return n
    else: # Recursive step
        return fibonacci(n-1) + fibonacci(n-2)
```

**Explanation:**

*   **`fibonacci(n)`:** Calculates the nth Fibonacci number.
*   **`if n <= 1:`:** Base case. The 0th and 1st Fibonacci numbers are 0 and 1, respectively.
*   **`else:`:** Recursive step. The nth Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers.

```python
print(fibonacci(6)) # Output: 8
```

**Advantages of Recursion:**

*   **Elegance and Readability:** Can often express solutions in a concise and elegant way, especially for problems with self-similar structures.
*   **Natural Fit for Some Problems:** Well-suited for problems like traversing tree structures or applying divide-and-conquer algorithms.

**Disadvantages of Recursion:**

*   **Overhead:** Function calls involve overhead (setting up the stack frame, etc.), making recursion potentially less efficient than iterative solutions in some cases.
*   **Stack Overflow:** Deep recursion can lead to a stack overflow error if the recursion goes too deep.
*   **Memory Usage:** Each recursive call consumes memory on the call stack.

## Common Pitfalls

*   **Stack Overflow (Recursion):** Forgetting a **base case** or having a base case that is never reached can cause the program to crash due to a stack overflow error (the call stack fills up).
*   **Inefficient Recursion:** Recursive solutions can sometimes be less efficient than iterative solutions due to function call overhead.
*   **Incorrect Stack/Queue Operations:** Using the wrong operations (e.g., trying to pop from an empty stack) or implementing the stack/queue incorrectly.
*   **Confusing Stack and Queue:** Using the wrong data structure for a given problem. Remember, **LIFO** for stacks, **FIFO** for queues.
*   **Not Choosing the Right Implementation:** For queues, using a simple Python list for both enqueueing and dequeueing is inefficient. Use `deque` from `collections` to improve performance.

## Summary

This module covered stacks, queues, and recursion. You now understand the **LIFO** (stacks) and **FIFO** (queues) access patterns and have implemented simple stack and queue data structures. You also learned the core concepts of **recursion**, including **base cases** and **recursive steps**. Stacks, queues, and recursion are fundamental tools for solving a wide variety of programming problems. Remember the trade-offs involved in using these different approaches, and practice using them through various exercises to reinforce your understanding.
