from collections import deque
from graphviz import Digraph

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BalancedBST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self.root = self._insert(self.root, key)
        self.root = self.balance(self.root)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.val:
            node.left = self._insert(node.left, key)
        elif key > node.val:
            node.right = self._insert(node.right, key)
        return node

    def remove(self, key):
        if self.root:
            self.root = self._remove(self.root, key)
            self.root = self.balance(self.root)

    def _remove(self, node, key):
        if node is None:
            return node
        if key < node.val:
            node.left = self._remove(node.left, key)
        elif key > node.val:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self.findMin(node.right)
            node.val = temp.val
            node.right = self._remove(node.right, temp.val)
        return node

    def findMin(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def balance(self, node):
        if node is None:
            return node
        balance_factor = self.getBalance(node)
        if balance_factor > 1:
            if self.getBalance(node.left) < 0:
                node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)
        if balance_factor < -1:
            if self.getBalance(node.right) > 0:
                node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)
        return node

    def getBalance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def rotateLeft(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        return y

    def rotateRight(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        return y

    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.val)
                _inorder(node.right)
        _inorder(self.root)
        return result

    def preorder(self):
        result = []
        def _preorder(node):
            if node:
                result.append(node.val)
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)
        return result

    def postorder(self):
        result = []
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.val)
        _postorder(self.root)
        return result

    def level_order(self):
        if not self.root:
            return []
        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def draw(self, filename='balanced_bst'):
        """
        Generate a visual PNG of the current BST using Graphviz.

        Args:
            filename (str): Name of the output file (default is 'balanced_bst').
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
    Interactive Balanced Binary Search Tree (AVL) visualizer and manipulator.
    """
    tree = BalancedBST()

    while True:
        print("\n")
        print("[q] Quit.")
        print("[i] Insert a value.")
        print("[s] Search for a value.")
        print("[r] Remove a value.")
        print("1: Print values in INORDER TRAVERSAL.")
        print("2: Print values in PREORDER TRAVERSAL.")
        print("3: Print values in POSTORDER TRAVERSAL.")
        print("4: Print values in LEVEL ORDER TRAVERSAL.")
        print("5: Visualize the tree (Graphviz).")
        print(">>> CHOOSE AN OPTION <<<")
        choice = input(">>  ").lower()

        # QUIT
        if choice == 'q':
            break

        # INSERT
        elif choice == "i":
            try:
                val = int(input("Enter value to insert to BST:  >>  "))
                tree.insert(val)
                tree.draw("bst_tree")
            except ValueError:
                print("⚠️ Please enter a valid number.")

        # SEARCH
        elif choice == "s":
            try:
                val = int(input("Enter value to search:  >>  "))
                result = tree.search(val)
                if result:
                    print(f'Value {val} is FOUND in the tree.')
                else:
                    print(f'Value {val} is NOT FOUND in the tree.')
            except ValueError:
                print("⚠️ Please enter a valid number.")

        # REMOVE
        elif choice == "r":
            try:
                val = int(input("Enter value to delete.  >>  "))
                found = tree.search(val)
                if found:
                    tree.remove(val)
                    tree.draw("bst_tree")
                    print(f"Value {val} is deleted successfully from the tree ✅.")
                else:
                    print(f'Value {val} is NOT FOUND in the tree ❌.')
            except ValueError:
                print("⚠️ Please enter a valid number.")

        # INORDER
        elif choice == "1":
            print("INORDER:", tree.inorder())

        # PREORDER
        elif choice == "2":
            print("PREORDER:", tree.preorder())

        # POSTORDER
        elif choice == "3":
            print("POSTORDER:", tree.postorder())

        # LEVEL ORDER
        elif choice == "4":
            print("LEVEL ORDER:", tree.level_order())

        # DRAW
        elif choice == "5":
            tree.draw("bst_tree")

if __name__ == "__main__":
    main()