# to visualize our tree
from graphviz import Digraph

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

class VisualBST:

    def __init__(self):
        self.root = None


    # ------------------ FUNCTIONS ------------------

    # worst case O(n) if unbalanced, but in general is O(log n)
    def searchBST(self, root, target):
        if not root:
            return None
        
        if target == root.val:
            return root

        elif target < root.val:
            return self.searchBST(root.left, target)
        
        else:
            return self.searchBST(root.right, target)
        

    ## Insert a new node and return the root of the BST.
    # this is basic insertion, more advanced is "AVL" will do later
    def insert(self, root, val): # O(logn)
        newNode = TreeNode(val)

        if not root:
            return newNode
        
        if val < root.val:
            root.left = self.insert(root.left, val)

        elif val > root.val:
            root.right = self.insert(root.right, val)
        
        return root
    
    
    # O(log n)
    def findMin(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr
    

    # O(log n + log n) - > O(logn), beacuse we traverse the tree twice, 1st time findMin and assign, 2nd time for go back and remove assigned val
    def remove(self, root, val):

        if not root:
            return None

        if val < self.root.val:
            root.left = self.remove(root.left, val)
        
        elif val > self.root.val:
            root.right = self.remove(root.right, val)
        
        else:
            if not root.left:
                return root.right
            
            elif not root.right:
                return root.left
            
            else:
                # find min val from right sub-tree
                minNode = self.findMin(root.right)
                root.val = minNode.val
                # go to the right sub-tree and delete that node (to avoid duplication)
                root.right = self.remove(root.right, minNode.val)
        
        return root   



    def inorder(self, root):
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
        values = []

        def inorderHelper(node):
            if not node:
                return 
            
            inorderHelper(node.left)
            inorderHelper(node.right)
            values.append(node.val)
        
        inorderHelper(root)
        return values
        




# ------------------ VISUALIZATION ------------------

    def draw(self, filename='bst'):
        # This creates a new directed graph (with arrows).
        dot = Digraph()
        self._add_nodes_edges(self.root, dot)
        dot.render(filename, view=True, format='png')  # opens the file automatically
        print(f"\nTree rendered and saved as '{filename}.png'")
    

    def _add_nodes_edges(self, node, dot, parent=None):
        if node is None:
            return
        
        """
        dot.node(...) tells Graphviz to create a visual circle (node) in the tree.
        id(node) gives each node a unique ID (because two nodes can have the same value, but we still want to distinguish them).
        str(node.value) is the label that shows up inside the circle (the value you inserted)."""
        dot.node(str(id(node)), str(node.val))

        # Adding edges (arrows) between parent and child (parent → child)
        if parent:
            dot.edge(str(id(parent)), str(id(node)))

        # It calls itself again with updated parent so each arrow goes from parent → child
        if node.left:
            self._add_nodes_edges(node.left, dot, node)
        if node.right:
            self._add_nodes_edges(node.right, dot, node)




# ------------------ MAIN PROGRAM ------------------
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
    print("\n")
    print(" >>> CHOOSE AN OPTION <<<  >> ")
    print("\n")
    choice = input(">>  ".lower())

    if choice == 'q':
        break

    elif choice == "i":
        try:
            val = int(input("\nEnter value to insert to BST:  >>  "))
            tree.root = tree.insert(tree.root, val)
            tree.draw("bst_tree")
        except ValueError:
            print("⚠️ Please enter a valid number.")

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
    
    elif choice == "r":
        try:
            val = int(input("\nEnter value to delete."))
            tree.root = tree.remove(tree.root, val)

            if tree.root is not None:
                print(f"✅ Value {val} is deleted succesfully from the tree.")
                tree.draw("bst_tree")
            else:
                print(f"✅ Value {val} was deleted. Tree is now empty.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

    elif choice == "1":
        print("\n")
        print(tree.inorder(tree.root))

    elif choice == "2":
        print("\n")
        print(tree.preorder(tree.root))

    elif choice == "3":
        print("\n")
        print(tree.postorder(tree.root))
    
