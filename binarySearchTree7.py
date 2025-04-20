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
    # SEARCH
    def searchBST(self, root, target):  # worst case O(n) if unbalanced, but in general TIME: O(log n)
        if not root:
            return None
        
        if target == root.val:
            return root

        elif target < root.val:
            return self.searchBST(root.left, target)
        
        else:
            return self.searchBST(root.right, target)
        

    ## INSERT
    def insert(self, root, val):    # this is basic insertion, more advanced is "AVL" will do later. TIME: O(log n)

        newNode = TreeNode(val)

        if not root:
            return newNode
        
        if val < root.val:
            root.left = self.insert(root.left, val)

        elif val > root.val:
            root.right = self.insert(root.right, val)
        
        return root
    

    # FIND MINIMUM
    def findMin(self, root):    # TIME: O(log n)
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr
    

    # REMOVE
    def remove(self, root, val):    # TIME: O(log n + log n), 1st step findMin O(log n) and assign, 2nd step remove assigned val O(log n)
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
                minNode = self.findMin(root.right)    # find min value from right subtree
                root.val = minNode.val
                root.right, _ = self.remove(root.right, minNode.val)    # go to right subtree and delete minNode (to avoid duplication)
                return root, True  


    # ------------------ DEPTH-FIRST SEARCH (DFS) ------------------
    def inorder(self, root):        # we do something when we hit the node 2nd time (hit-> when return back to that node)
        values = []

        def inorderHelper(node):    # need helper function beacuse, values will not be updated if we call inorder() itself recursively.
            if not node:
                return 
        
            inorderHelper(node.left)
            values.append(node.val)
            inorderHelper(node.right)
        
        inorderHelper(root)
        return values


    def preorder(self, root):    # we do something when we hit the node 1st time (hit-> when return back to that node)
        values = []

        def inorderHelper(node):
            if not node:
                return 
            
            values.append(node.val)
            inorderHelper(node.left)
            inorderHelper(node.right)
        
        inorderHelper(root)
        return values
    

    def postorder(self, root):    # we do something when we hit the node 3rd time (hit-> when return back to that node)    
        values = []

        def inorderHelper(node):
            if not node:
                return 
            
            inorderHelper(node.left)
            inorderHelper(node.right)
            values.append(node.val)
        
        inorderHelper(root)
        return values


    # ------------------ BREADTH-FIRST SEARCH (DFS) ------------------
    def get_suffix(self, level):
        if 11 <= level % 100 <= 13:  # Handle special cases like 11th, 12th, 13th
            return "th"
        last_digit = level % 10
        if last_digit == 1:
            return "st"
        elif last_digit == 2:
            return "nd"
        elif last_digit == 3:
            return "rd"
        else:
            return "th"
        

    def bfs(self, root):
        from collections import deque
        queue = deque()

        if not root:
            return
        else:
            queue.append(root)
        
        level = 0
        while queue:
            level_size = len(queue)
            suffix = self.get_suffix(level + 1)  # Determine suffix for the current level
            print(f"{level + 1}{suffix} Level of the tree is:", end=' ')
            for _ in range(level_size): # _ -> variable is intentionally unused
                node = queue.popleft()
                print(node.val, end= ' ') 

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()
            level += 1


    # ------------------ BACKTRACKING ------------------
    def canReachLeaf(self, root, path):
        if not root or root.val == 0:
            return False
        
        path.append(root.val)

        if not root.left and not root.right: # base case
            return True
        
        if self.canReachLeaf(root.left, path):    # reach base case no childs
            return True
        
        if self.canReachLeaf(root.right, path):
            return True
        
        path.pop() # backtrack
        return False
    

# ------------------ VISUALIZATION ------------------
    def draw(self, filename='bst'):
        dot = Digraph()     # This creates a new directed graph (with arrows).
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

        if parent:  # Adding edges (arrows) between parent and child (parent → child)
            dot.edge(str(id(parent)), str(id(node)))

        if node.left:   # it calls itself again with updated parent so each arrow goes from parent → child

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





    
