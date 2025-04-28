from graphviz import Digraph

class TreeNode:
    """Class representing a node in the binary search tree."""
    def __init__(self, val):
        """
        Initialize a new TreeNode.

        Args:
            val (int): Value to store in the node.
        """
        self.val = val
        self.left = None
        self.right = None


class VisualBST:
    """Class for a Binary Search Tree with visualization and traversal support."""
    def __init__(self):
        """Initialize the VisualBST with an empty root."""
        self.root = None

    def searchBST(self, root, target):
        """
        Recursively search for a value in the BST.

        Args:
            root (TreeNode): The root node of the BST.
            target (int): The value to search for.

        Returns:
            TreeNode: Node containing the value, or None if not found.
        """
        if not root:
            return None
        
        if target == root.val:
            return root
        elif target < root.val:
            return self.searchBST(root.left, target)
        else:
            return self.searchBST(root.right, target)

    def insert(self, root, val):
        """
        Insert a value into the BST.

        Args:
            root (TreeNode): Root node of the tree.
            val (int): Value to insert.

        Returns:
            TreeNode: New root after insertion.
        """
        newNode = TreeNode(val)
        if not root:
            return newNode
        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

    def findMin(self, root):
        """
        Find the node with the minimum value in a BST.

        Args:
            root (TreeNode): Root node of the tree/subtree.

        Returns:
            TreeNode: Node with the minimum value.
        """
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def remove(self, root, val):
        """
        Remove a node with the given value from the BST.

        Args:
            root (TreeNode): Root of the tree/subtree.
            val (int): Value to remove.

        Returns:
            tuple: (Updated root TreeNode, Boolean indicating if node was removed)
        """
        if not root:
            return None, False

        if val < root.val:
            root.left, removed = self.remove(root.left, val)
            return root, removed
        elif val > root.val:
            root.right, removed = self.remove(root.right, val)
            return root, removed
        else:
            if not root.left:
                return root.right, True
            elif not root.right:
                return root.left, True
            else:
                minNode = self.findMin(root.right)
                root.val = minNode.val
                root.right, _ = self.remove(root.right, minNode.val)
                return root, True

    def inorder(self, root):
        """
        Perform in-order traversal of the BST.

        Args:
            root (TreeNode): Root of the tree.

        Returns:
            list: Values in in-order sequence.
        """
        values = []
        def inorderHelper(node):
            if not node:
                return 
            inorderHelper(node.left)
            values.append(node.val)
            inorderHelper(node.right)
        inorderHelper(root)
        return values

    def preorder(self, root):
        """
        Perform pre-order traversal of the BST.

        Args:
            root (TreeNode): Root of the tree.

        Returns:
            list: Values in pre-order sequence.
        """
        values = []
        def inorderHelper(node):
            if not node:
                return 
            values.append(node.val)
            inorderHelper(node.left)
            inorderHelper(node.right)
        inorderHelper(root)
        return values

    def postorder(self, root):
        """
        Perform post-order traversal of the BST.

        Args:
            root (TreeNode): Root of the tree.

        Returns:
            list: Values in post-order sequence.
        """
        values = []
        def inorderHelper(node):
            if not node:
                return 
            inorderHelper(node.left)
            inorderHelper(node.right)
            values.append(node.val)
        inorderHelper(root)
        return values

    def get_suffix(self, level):
        """
        Return the correct suffix for a given number (st, nd, rd, th).

        Args:
            level (int): The number to find a suffix for.

        Returns:
            str: The appropriate suffix string.
        """
        if 11 <= level % 100 <= 13:
            return "th"
        last_digit = level % 10
        return {1: "st", 2: "nd", 3: "rd"}.get(last_digit, "th")

    def bfs(self, root):
        """
        Perform level-order traversal (Breadth-First Search) of the BST.

        Args:
            root (TreeNode): Root of the tree.
        """
        from collections import deque
        queue = deque()

        if not root:
            return
        queue.append(root)
        level = 0
        while queue:
            level_size = len(queue)
            suffix = self.get_suffix(level + 1)
            print(f"{level + 1}{suffix} Level of the tree is:", end=' ')
            for _ in range(level_size):
                node = queue.popleft()
                print(node.val, end=' ')
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()
            level += 1

    def canReachLeaf(self, root, path):
        """
        Determine if there's a path from root to any leaf node.

        Args:
            root (TreeNode): The root of the tree.
            path (list): List to track the path.

        Returns:
            bool: True if a path exists, otherwise False.
        """
        if not root or root.val == 0:
            return False
        path.append(root.val)
        if not root.left and not root.right:
            return True
        if self.canReachLeaf(root.left, path) or self.canReachLeaf(root.right, path):
            return True
        path.pop()
        return False

    def draw(self, filename='bst'):
        """
        Generate a visual PNG of the current BST using Graphviz.

        Args:
            filename (str): Name of the output file (default is 'bst').
        """
        dot = Digraph()
        self._add_nodes_edges(self.root, dot)
        dot.render(filename, view=True, format='png')
        print(f"\nTree rendered and saved as '{filename}.png'")

    def _add_nodes_edges(self, node, dot, parent=None):
        """
        Recursive helper for creating Graphviz nodes and edges.

        Args:
            node (TreeNode): Current node to draw.
            dot (Digraph): Graphviz Digraph object.
            parent (TreeNode, optional): Parent node for connecting edges.
        """
        if node is None:
            return
        dot.node(str(id(node)), str(node.val))
        if parent:
            dot.edge(str(id(parent)), str(id(node)))
        if node.left:
            self._add_nodes_edges(node.left, dot, node)
        if node.right:
            self._add_nodes_edges(node.right, dot, node)



# ------------------ MAIN PROGRAM ------------------
def main():
    """
    Interactive Binary Search Tree (BST) visualizer and manipulator.

    This program allows users to:
    - Insert, search, and remove values from the BST
    - Display the tree using Inorder, Preorder, Postorder, and BFS traversals
    - Check if a path exists from root to leaf
    - Visualize the BST using Graphviz (if installed)

    Usage:
    Run the script and follow the on-screen menu options.
    """
    tree = VisualBST()

    while True:
        print("\n")
        print("\n [q] Quit.")
        print("\n [i] Insert a value.")
        print("\n [s] Search for a value.")
        print("\n [r] Remove a value. ")
        print("\n Press 1 to print values in INORDER TRAVERSAL.")
        print("\n Press 2 to print values in PREORDER TRAVERSAL.")
        print("\n Press 3 to print values in POSTORDER TRAVERSAL.")
        print("\n Press 4 to perform LEVEL ORDER TRAVERSAL.")
        print("\n Press 5 to check if path exists from root to leaf node.")
        print("\n")
        print(" >>> CHOOSE AN OPTION <<<  >> ")
        print("\n")
        
        choice = input(">>  ").lower()

        # QUIT
        if choice == 'q':
            break
        
        # INSERT
        elif choice == "i":
            try:
                val = int(input("\nEnter value to insert to BST:  >>  "))
                tree.root = tree.insert(tree.root, val)
                tree.draw("bst_tree")

            except ValueError:
                print("⚠️ Please enter a valid number.")

        # SEARCH
        elif choice == "s":
            try:
                val = int(input("\nEnter value to search:  >>  "))
                result = tree.searchBST(tree.root, val)

                if result:
                    print("\n")
                    print(f'Value {val} is FOUND in the tree.')
                
                else:
                    print("\n")
                    print(f'Value {val} is NOT FOUND in the tree.')

            except ValueError:
                print("⚠️ Please enter a valid number.")

        # REMOVE
        elif choice == "r":
            try:
                val = int(input("\nEnter value to delete.  >>  "))
                tree.root, removed = tree.remove(tree.root, val)
                tree.draw("bst_tree")

                if removed:
                    print(f"Value {val} is deleted succesfully from the tree ✅.")

                else:
                    print(f'Value {val} is NOT FOUND in the tree ❌.')

            except ValueError:
                print("⚠️ Please enter a valid number.")

        # DFS
        # inorder traversal
        elif choice == "1":
            print("\n")
            print(tree.inorder(tree.root))

        # preorder traversal
        elif choice == "2":
            print("\n")
            print(tree.preorder(tree.root))

        # post order traversal
        elif choice == "3":
            print("\n")
            print(tree.postorder(tree.root))

        # BFS
        elif choice == "4":
            print("\n")
            tree.bfs(tree.root)



        # Check if path exists to leaf node
        elif choice == "5":
            values = []
            print("\n")
            result = tree.canReachLeaf(tree.root, values)

            if result:
                print("\nThere is a path from root to leaf node:", values)
            else:
                print("\nThe is no way to get to leaf node.")


if __name__ == "__main__":
    main()



