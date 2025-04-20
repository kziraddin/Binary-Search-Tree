# 🌳 Visual Binary Search Tree (BST) in Python

This project implements a **Binary Search Tree (BST)** in Python with both **console-based tree visualization**
and **graphical rendering using Graphviz**. It includes fundamental tree traversal techniques and additional features like pathfinding.

---

## 🚀 Features
### 🧠 Binary Search Tree (BST) implementation with basic operations:
- Insert
- Search
- Remove
#### 🎨 Visual rendering of the tree structure using Graphviz
#### 🔍 Comprehensive traversal options:
- Depth-First Search (DFS): Inorder, Preorder, Postorder traversals
- Breadth-First Search (BFS): Level order traversal with labeled levels
#### 🛤 Pathfinding to check for a valid root-to-leaf path
#### 🎮 Interactive CLI for real-time interactions with the tree

## 📸 Preview
After modifying the tree (e.g., inserting or removing nodes), an updated visual is automatically generated as a PNG file (bst_tree.png)

## 🧩 Requirements
- Python 3.x
- `graphviz` system package (for rendering)
- `graphviz` Python module

#### Install system Graphviz:
**macOS** (Homebrew):
```bash
brew install graphviz
```
#### Ubuntu/Debian:
```bash
sudo apt-get install graphviz
```
**Windows**
Download from: https://graphviz.org/download/

### Install Python package:
```bash
pip3 install graphviz
```
### 💻 How to Run
```bash
python3 binarySearchTree.py
```

#### Then follow the CLI prompts to:
- Insert values into the tree
- Search for specific values
- Delete nodes from the tree
- Perform tree traversals (DFS, BFS)
- Check if a path exists from the root to a leaf node

### 📚 Files
- binarySearchTree.py — Main script containing all the logic
- bst_tree.png — Auto-generated visual representation of the BST (updated dynamically)

### 🧠 Concepts Used
#### Binary Search Tree:
-Insert, Search, Remove operations
#### Tree Traversals:
- Depth-First Search (Inorder, Preorder, Postorder)
- Breadth-First Search with level-specific suffixes (1st, 2nd, etc.)
#### Backtracking:
- Pathfinding from root to leaf
#### Recursion:
- Core logic for tree operations
#### Graphical Visualization:
- Using Graphviz to render the tree

## 🎮 Interactive Menu
#### The interactive CLI offers the following options:
- [i] Insert a value: Add a new node to the tree.
- [s] Search for a value: Check if a value exists in the tree.
- [r] Remove a value: Delete a specific value from the tree.
- [1] Inorder Traversal: Print nodes in sorted order (DFS).=
- [2] Preorder Traversal: Print nodes in root-left-right order (DFS).
- [3] Postorder Traversal: Print nodes in left-right-root order (DFS).
- [4] Level Order Traversal: Print nodes level by level (BFS).
- [5] Pathfinding: Check if a path exists from root to a leaf node.
- [q] Quit: Exit the program.

## 🙌 Future Improvements
- ⚙️ Implement AVL Tree for self-balancing
- ➕ Add support for duplicate value handling
- 🔍 Enhance visual rendering (e.g., with colors or labels)
- 📈 Optimize traversal algorithms for larger datasets

### 👨‍💻 Author

Built by [Ziraddin (Z)] — feel free to fork, improve, or reach out!

### 📝 License

This project is open source and available under the MIT License.


## Demo Video

https://github.com/user-attachments/assets/fb46a314-1778-45e8-ae56-68ad0a39a695



