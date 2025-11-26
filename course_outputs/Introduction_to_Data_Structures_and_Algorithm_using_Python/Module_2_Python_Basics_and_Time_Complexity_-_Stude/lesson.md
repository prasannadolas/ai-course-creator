# Module 2: Python Basics and Time Complexity

## Introduction

In this module, we'll solidify your understanding of Python fundamentals, as a solid grasp of these is essential for working with data structures and algorithms. We will then transition to a critical concept: **time complexity**, specifically focusing on **Big O notation**. This is how we analyze the efficiency of our algorithms.

## Python Refresher

Let's quickly recap some key Python concepts that you'll need.

**1. Data Types**

Python supports various data types, including:

*   **Integers:** Whole numbers (e.g., `10`, `-5`, `0`).
*   **Floats:** Numbers with decimal points (e.g., `3.14`, `-2.5`).
*   **Strings:** Sequences of characters (e.g., `"hello"`, `"Python"`).
*   **Booleans:** `True` or `False`.
*   **Lists:** Ordered, mutable sequences of items (e.g., `[1, 2, 3]`, `["a", "b", "c"]`).
*   **Tuples:** Ordered, immutable sequences of items (e.g., `(1, 2, 3)`).
*   **Dictionaries:** Key-value pairs (e.g., `{"name": "Alice", "age": 30}`).

**2. Control Flow**

*   **`if`, `elif`, `else`:** Conditional statements for decision-making.

```python
age = 20
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

**Explanation:**
This code checks the value of the variable `age`. If `age` is greater or equal to 18, it prints "You are an adult". Otherwise, it prints "You are a minor."

*   **`for` loops:** Iterate over sequences (lists, strings, etc.).

```python
for i in range(5):
    print(i)
```

**Explanation:**
This loop iterates five times. The `range(5)` function creates a sequence of numbers from 0 to 4. In each iteration, the value of `i` is printed.

*   **`while` loops:** Repeat a block of code as long as a condition is true.

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

**Explanation:**
This `while` loop continues as long as `count` is less than 3. Inside the loop, the current value of `count` is printed, and then `count` is incremented.

**3. Functions**

Functions are reusable blocks of code.

```python
def greet(name):
    """This function greets the person passed in as a parameter."""
    print("Hello, " + name + "!")

greet("Alice") # Calling the function
```

**Explanation:**
This code defines a function called `greet` that takes a `name` as input, and prints a greeting message. It's then called with the argument "Alice".

## Introduction to Time Complexity

**Time complexity** is a way to analyze how the runtime of an algorithm grows as the input size increases. It's not about measuring the *exact* time in seconds or milliseconds, but rather about understanding the *trend* of how the execution time changes. We use **Big O notation** to express this.

**Big O Notation**

**Big O notation** describes the *upper bound* of an algorithm's growth rate. It provides a simplified way to compare the efficiency of different algorithms.

*   **O(1) - Constant Time:** The algorithm takes the same amount of time regardless of the input size.

```python
def get_first_element(data):
    return data[0] # Accessing the first element of a list
```

**Explanation:**
This function accesses the first element of a list. The time taken for this operation is constant, regardless of how long the list is.

*   **O(n) - Linear Time:** The runtime grows linearly with the input size (n).

```python
def search_for_value(data, target):
    for item in data:
        if item == target:
            return True # Found target
    return False # Target not found
```

**Explanation:**
This function searches for a target value within a list. In the worst-case scenario (target not in list, or target is the last element), the function has to look through every element in the `data` list. Therefore, the runtime grows linearly with the size of `data`.

*   **O(log n) - Logarithmic Time:** The runtime increases logarithmically with the input size. This is very efficient. Typically found in algorithms that repeatedly divide the problem into smaller parts. Think of binary search.

*   **O(n^2) - Quadratic Time:** The runtime grows proportionally to the square of the input size. Often seen in nested loops.

```python
def find_pairs(data):
    for i in range(len(data)):
        for j in range(len(data)):
            print(data[i], data[j]) # Perform an operation on each pair
```

**Explanation:**
This function has two nested loops. The outer loop iterates `n` times (where `n` is the length of `data`), and the inner loop also iterates `n` times. The total number of operations is approximately `n * n`, which results in quadratic time complexity (O(n^2)).

*   **O(2^n) - Exponential Time:** The runtime doubles with each addition to the input size. These algorithms are typically very slow for even moderately sized inputs.

## Analyzing Time Complexity

1.  **Identify the Basic Operations:** Determine the fundamental operations performed by your algorithm (e.g., comparisons, assignments, arithmetic operations).
2.  **Count the Operations:** Analyze how the number of operations grows as the input size (n) increases.
3.  **Determine the Dominant Term:** Focus on the term that grows the fastest as n increases. This term determines the Big O notation. For example, O(n^2 + n) is simplified to O(n^2) because n^2 grows much faster than n.
4.  **Simplify and Express in Big O:** Drop constant factors and lower-order terms.

**Example: Analyzing a Simple Loop**

```python
def print_elements(data):
    for item in data:
        print(item)
```

**Analysis:**

1.  **Basic Operations:** The primary operation is the `print()` function within the loop.
2.  **Counting Operations:** The loop iterates `n` times, where `n` is the length of the `data` list. The `print()` function is executed once in each iteration.
3.  **Dominant Term:** The dominant term is `n` (the number of loop iterations).
4.  **Big O Notation:** The time complexity is **O(n)** - Linear Time.

## Practical Code Examples (with Time Complexity Analysis)

```python
# O(1) - Constant Time
def get_element_by_index(data, index):
    return data[index]
```

**Explanation:** Accessing an element by its index in a list takes constant time. The operation's duration doesn't change based on the list's size.

```python
# O(n) - Linear Time
def sum_list(data):
    total = 0
    for item in data:
        total += item
    return total
```

**Explanation:** This function iterates through the entire list once. If the list has `n` elements, the loop runs `n` times. Therefore, the time complexity is linear, **O(n)**.

```python
# O(n^2) - Quadratic Time
def find_duplicates(data):
    duplicates = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)): # Starts from i+1 to avoid comparing the same element twice
            if data[i] == data[j]:
                if data[i] not in duplicates: # Avoid adding the same duplicate multiple times.
                    duplicates.append(data[i])
    return duplicates
```

**Explanation:** This function uses nested loops. The outer loop runs `n` times, and the inner loop runs approximately `n` times in the worst case (when there are no duplicates). Therefore, the time complexity is **O(n^2)** - Quadratic Time.

## Common Pitfalls

*   **Confusing Time and Space Complexity:** **Time complexity** analyzes the runtime, whereas **space complexity** assesses the amount of memory (space) used by the algorithm. Both are important.
*   **Focusing on Micro-optimizations:** Prematurely optimizing small sections of code can distract you from the larger picture of overall algorithm efficiency.
*   **Ignoring the Worst-Case Scenario:** **Big O notation** usually focuses on the worst-case scenario. Be aware that the *average* and *best-case* scenarios may differ, but worst-case analysis guarantees a performance upper bound.
*   **Incorrectly Identifying the Dominant Operation:** Carefully analyze your code to determine which operations dominate the runtime. Sometimes it's not immediately obvious.
*   **Over-reliance on Benchmarking:** While benchmarking can provide real-world performance measurements, it doesn't replace the need for **Big O analysis**. Benchmarking results can be specific to the hardware and input data.

## Summary

This module provided a Python refresher and introduced the critical concept of **time complexity**, including **Big O notation**. We covered how to analyze the efficiency of algorithms and expressed their growth rates. Understanding **time complexity** is crucial for making informed decisions about which algorithms to use and for writing efficient and scalable code. In the upcoming modules, we'll apply these concepts as we analyze the time and space complexity of various data structures and algorithms. Remember to practice analyzing the time complexity of the code you write; this is a crucial skill.
