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
    def insert(self, root, val):
        newNode = TreeNode(val)

        if not root:
            return newNode
        
        if val < root.val:
            root.left = self.insert(root.left, val)

        elif val > root.val:
            root.right = self.insert(root.right, val)
        
        return root
    


# ------------------ Visualization ------------------

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
    print(" >>> CHOOSE AN OPTION <<<  >> ")
    print("\n")
    print("\n [q] Quit.")
    print("\n [i] Insert a value.")
    print("\n [s] Search for a value.")
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