# Module 5: Trees and Graphs Introduction

## Introduction

In this module, we'll venture into the world of **trees** and **graphs**, two powerful and versatile non-linear data structures. We'll explore their fundamental concepts, terminology, and common applications. Understanding **trees** and **graphs** is crucial for modeling relationships, representing hierarchies, and solving complex problems in computer science and beyond.

## Trees

A **tree** is a hierarchical data structure that represents relationships between elements in a parent-child manner. It's a non-linear data structure because elements are not stored sequentially like in arrays or linked lists.

**Key Concepts and Terminology:**

*   **Node:** A fundamental unit of a **tree**, containing a value (data) and references (pointers) to its child nodes.
*   **Root:** The topmost **node** in the **tree**. It has no parent.
*   **Parent:** A **node** that has one or more child nodes.
*   **Child:** A **node** that is directly connected to a **parent node**.
*   **Leaf:** A **node** that has no children.
*   **Sibling:** Nodes that have the same parent.
*   **Edge:** The connection between two nodes (parent-child relationship).
*   **Depth (or Level):** The distance of a **node** from the **root**. The **root** has a depth of 0.
*   **Height:** The longest path from a **node** to a **leaf**. The **height** of the **tree** is the height of its **root**.
*   **Subtree:** A portion of the **tree** that is itself a **tree**.

**Types of Trees:**

*   **Binary Tree:** Each **node** has at most two children (left and right).
*   **Binary Search Tree (BST):** A **binary tree** where the value of each **node** is greater than all values in its left subtree and less than all values in its right subtree. This enables efficient searching.
*   **Balanced Tree:** A **tree** where the height of the left and right subtrees of any **node** differ by at most a constant value. AVL trees and Red-Black trees are examples of self-balancing binary search trees.
*   **N-ary Tree:** Each **node** can have up to *n* children.

**Implementation (Binary Tree in Python):**

```python
class Node:
    def __init__(self, data):
        self.data = data # Data stored in the node
        self.left = None # Reference to the left child
        self.right = None # Reference to the right child

# Example: Creating a Simple Binary Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
```

**Explanation:**

*   **`class Node:`:** Defines a class called `Node` to represent a **node** in the **binary tree**.
    *   `self.data`: Stores the data associated with the **node**.
    *   `self.left`: A pointer (reference) to the left child **node**. Initialized to `None`.
    *   `self.right`: A pointer (reference) to the right child **node**. Initialized to `None`.
*   **`root = Node(1)`:** Creates the **root node** with data value 1.
*   The subsequent lines create the left and right child nodes and connect them to the root and other nodes, building the **tree** structure.

**Tree Traversal Algorithms:**

**Traversal algorithms** are used to visit each **node** in a **tree**. Common traversal methods include:

*   **In-order Traversal:** Visit the left subtree, then the **node** itself, then the right subtree (for BSTs, this visits nodes in sorted order).

    ```python
    def inorder_traversal(node):
        if node: # Check if node is not None
            inorder_traversal(node.left)
            print(node.data, end=" ") # Visit the node
            inorder_traversal(node.right)
    ```

    **Explanation:**
    - The function recursively traverses the left subtree, prints the node's data, and then traverses the right subtree.

*   **Pre-order Traversal:** Visit the **node** itself, then the left subtree, then the right subtree.

    ```python
    def preorder_traversal(node):
        if node: # Check if node is not None
            print(node.data, end=" ") # Visit the node
            preorder_traversal(node.left)
            preorder_traversal(node.right)
    ```

    **Explanation:**
    - Prints the node's data, then recursively traverses the left and right subtrees.

*   **Post-order Traversal:** Visit the left subtree, then the right subtree, then the **node** itself.

    ```python
    def postorder_traversal(node):
        if node: # Check if node is not None
            postorder_traversal(node.left)
            postorder_traversal(node.right)
            print(node.data, end=" ") # Visit the node
    ```

    **Explanation:**
    - Recursively traverses the left and right subtrees and prints the node's data.

**Use Cases for Trees:**

*   **File Systems:** Representing the hierarchical structure of files and directories.
*   **Decision Trees:** Used in machine learning for classification and regression tasks.
*   **Database Indexing (B-trees):** Used to speed up data retrieval.
*   **Abstract Syntax Trees (AST):** Used by compilers to represent the structure of programming code.
*   **Representing Organizational Structures:** Family trees, company hierarchies.

## Graphs

A **graph** is a non-linear data structure consisting of a set of **vertices** (or **nodes**) and a set of **edges** that connect these **vertices**. **Graphs** are more general than **trees**; a **tree** is a special type of **graph**.

**Key Concepts and Terminology:**

*   **Vertex (or Node):** Represents an entity or object in the **graph**.
*   **Edge:** Represents a connection or relationship between two **vertices**.
*   **Directed Graph:** Edges have a direction (e.g., an edge from A to B, but not necessarily from B to A).
*   **Undirected Graph:** Edges have no direction (e.g., if there's an edge between A and B, there's also an edge between B and A).
*   **Weighted Graph:** Edges have associated weights (e.g., distances, costs).
*   **Path:** A sequence of **vertices** connected by **edges**.
*   **Cycle:** A **path** that starts and ends at the same **vertex**.
*   **Degree:** The number of **edges** connected to a **vertex**. In a **directed graph**, we distinguish between *in-degree* (incoming edges) and *out-degree* (outgoing edges).
*   **Connected Graph:** There is a path between every pair of **vertices**.
*   **Complete Graph:** Every **vertex** is connected to every other **vertex**.

**Representations of Graphs:**

1.  **Adjacency Matrix:** A 2D matrix where the element at `matrix[i][j]` indicates whether there's an edge from **vertex** `i` to **vertex** `j`. For weighted graphs, the element stores the edge weight.

    ```python
    # Example (Undirected, Unweighted Graph)
    # vertices: 0, 1, 2, 3
    # edges: (0, 1), (0, 2), (1, 2), (2, 3)

    adjacency_matrix = [
        [0, 1, 1, 0], # Vertex 0 is connected to 1 and 2
        [1, 0, 1, 0], # Vertex 1 is connected to 0 and 2
        [1, 1, 0, 1], # Vertex 2 is connected to 0, 1 and 3
        [0, 0, 1, 0]  # Vertex 3 is connected to 2
    ]
    ```

    **Explanation:** A 2D list (matrix) is used. A value of 1 at `adjacency_matrix[i][j]` indicates an **edge** from **vertex** `i` to **vertex** `j`. A 0 indicates no edge. Because this is an undirected graph, the matrix is symmetric.

2.  **Adjacency List:** A list of lists (or a dictionary where keys are vertices and values are lists of adjacent vertices). More space-efficient, especially for sparse graphs (graphs with relatively few edges).

    ```python
    # Example (Undirected, Unweighted Graph)
    # vertices: 0, 1, 2, 3
    # edges: (0, 1), (0, 2), (1, 2), (2, 3)

    adjacency_list = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    ```

    **Explanation:** A dictionary is used. The keys are vertex labels (0, 1, 2, 3). The values are lists of vertices that are connected to the key vertex. For example, vertex 0 is connected to vertices 1 and 2.

**Graph Traversal Algorithms:**

*   **Breadth-First Search (BFS):** Explores the **graph** layer by layer, starting from a source **vertex**. Uses a queue.

    ```python
    from collections import deque

    def bfs(graph, start_node):
        visited = set()  # Keep track of visited nodes
        queue = deque([start_node]) # Queue for BFS

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                # Enqueue all unvisited neighbors
                for neighbor in graph.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
    ```

    **Explanation:**
    - `bfs(graph, start_node)` takes a graph (represented as an adjacency list) and a starting node as input.
    - `visited`: A set to keep track of visited vertices to avoid cycles.
    - `queue`: A `deque` is used to implement a queue. Starts with the `start_node`.
    - The `while queue` loop continues as long as there are nodes in the queue.
    - In each iteration, a node (`vertex`) is dequeued.
    - If the `vertex` hasn't been visited:
        - It's printed.
        - It's added to the `visited` set.
        - All unvisited neighbors of the `vertex` are enqueued (added to the queue).

*   **Depth-First Search (DFS):** Explores as far as possible along each branch before backtracking. Uses recursion (or an explicit stack).

    ```python
    def dfs(graph, start_node, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_node)
        print(start_node, end=" ")
        for neighbor in graph.get(start_node, []):
            if neighbor not in visited:
                dfs(graph, neighbor, visited)
    ```

    **Explanation:**
    - `dfs(graph, start_node, visited)` takes a graph (adjacency list), a starting node and optionally a set of visited vertices.
    - `visited`: A set to store visited nodes. Initialized to `None` if not provided.
    - The `start_node` is added to `visited` and printed.
    - The function recursively calls itself for each unvisited neighbor of the `start_node`.

**Use Cases for Graphs:**

*   **Social Networks:** Representing users and their connections.
*   **Mapping and Navigation:** Representing roads and intersections.
*   **Computer Networks:** Representing devices and their connections.
*   **Recommendation Systems:** Representing items and user preferences.
*   **Web Crawling:** Discovering and indexing web pages.
*   **Scheduling and Resource Allocation.**

## Common Pitfalls

*   **Incorrect Tree Structure:** Creating a **tree** that violates the parent-child relationships (e.g., cycles).
*   **Incorrect Graph Representation:** Choosing an inappropriate representation (adjacency matrix vs. adjacency list) that leads to inefficiency.
*   **Infinite Loops (Graph Traversal):** Not keeping track of visited nodes during **graph** traversal, leading to infinite loops in the presence of cycles.
*   **Stack Overflow (Deep Tree Recursion):** Recursively processing very deep trees can lead to stack overflow errors.
*   **Complexity of Graph Algorithms:** Graph algorithms can have high time complexities (e.g., O(V+E) for BFS/DFS, where V is the number of vertices and E is the number of edges), and it's important to be mindful of those complexities.
*   **Confusing Tree and Graph Terminology:** Incorrectly using terms associated with trees and graphs can lead to confusion and errors.
*   **Not Considering Weighted Graphs When Appropriate:** Ignoring edge weights in problems that require them.

## Summary

This module provided an introduction to **trees** and **graphs**, two fundamental non-linear data structures. You learned about **tree** and **graph** terminology, explored different types of **trees** and **graph** representations, and reviewed the basic graph traversal algorithms. **Trees** and **graphs** are essential tools for modeling relationships and solving complex problems. Continued study of advanced tree structures (like BST, AVL, and Red-Black Trees) and graph algorithms (such as Dijkstra's, A\*, minimum spanning trees) is recommended to further strengthen your skills.
