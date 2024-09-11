import matplotlib.pyplot as plt

class AVLRedBlackNode:
    def __init__(self, key, color='R'):
        self.key = key #مقدار یا کلیدی که در گره ذخیره می‌شود. این مقدار می‌تواند عدد، رشته، یا هر نوع داده دیگری باشد.
        self.color = color  # 'R' for Red, 'B' for Black
        self.left = None
        self.right = None
        self.height = 1  # For AVL balance

class AVLRedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = AVLRedBlackNode(key, 'B')  # Root is always black
        else:
            self.root = self._insert(self.root, key)
            self.root.color = 'B'  # Ensure root remains black

    def _insert(self, node, key):
        if not node:
            return AVLRedBlackNode(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node  # No duplicates
        
        # Update height and balance factor
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        
        # Balance the tree
        return self._balance(node)

    def _balance(self, node):
        balance = self._get_balance(node)
        
        # Left heavy
        if balance > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            node = self._rotate_right(node)
        
        # Right heavy
        elif balance < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)
        
        # Check and fix Red-Black properties
        if node.left and node.left.color == 'R' and node.right and node.right.color == 'R':
            self._flip_colors(node)
        
        return node

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        
        # Update heights
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))
        
        return new_root

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        
        # Update heights
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))
        
        return new_root

    def _flip_colors(self, node):
        node.color = 'R' if node.color == 'B' else 'B'
        if node.left:
            node.left.color = 'R' if node.left.color == 'B' else 'B'
        if node.right:
            node.right.color = 'R' if node.right.color == 'B' else 'B'

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node or node.key == key:
            return node
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        if not self.root:
            return
        self.root = self._delete(self.root, key)
        if self.root:
            self.root.color = 'B'  # Root is always black

    def _delete(self, node, key):
        if not node:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left or not node.right:
                return node.left or node.right

            # Find successor (smallest in the right subtree)
            successor = self._get_min(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        # Update height
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        
        # Balance the tree
        return self._balance(node)

    def _get_min(self, node):
        while node.left:
            node = node.left
        return node

# Helper function to visualize the tree using matplotlib
def plot_tree(tree, filename="avl_red_black_tree.png"):
    fig, ax = plt.subplots()
    ax.set_axis_off()
    if tree.root:
        _plot_tree_helper(ax, tree.root, 0.5, 1, 0.25, tree.root.key)
    plt.savefig(filename, bbox_inches='tight')
    plt.show()

def _plot_tree_helper(ax, node, x, y, dx, key, level=0):
    if not node:
        return
    # Set the color of the circle
    circle_color = 'red' if node.color == 'R' else 'black'
    text_color = 'white' if node.color == 'R' else 'white'

    # Draw the node as a circle
    ax.text(x, y, f'{node.key}', ha='center', va='center', fontsize=12, color=text_color,
            bbox=dict(facecolor=circle_color, edgecolor='black', boxstyle='circle'))
    
    if node.left:
        ax.plot([x, x - dx], [y - 0.1, y - 0.2], color='black')
        _plot_tree_helper(ax, node.left, x - dx, y - 0.2, dx / 2, node.left.key, level + 1)
    if node.right:
        ax.plot([x, x + dx], [y - 0.1, y - 0.2], color='black')
        _plot_tree_helper(ax, node.right, x + dx, y - 0.2, dx / 2, node.right.key, level + 1)

# Main function to handle user input and output
def main():
    # Initialize the AVL-Red-Black Tree
    tree = AVLRedBlackTree()

    # Get user input for elements to insert
    elements_to_insert = input("Enter elements to insert (comma-separated): ").split(',')
    elements_to_insert = [int(e) for e in elements_to_insert]
    
    # Insert elements
    for elem in elements_to_insert:
        tree.insert(elem)
    
    # Plot and save the tree after insertions
    plot_tree(tree, "tree_after_insertion.png")
    print("Tree after insertions saved as 'tree_after_insertion.png'")

    # Get user input for elements to delete
    elements_to_delete = input("Enter elements to delete (comma-separated): ").split(',')
    elements_to_delete = [int(e) for e in elements_to_delete]
    
    # Delete elements
    for elem in elements_to_delete:
        tree.delete(elem)
    
    # Plot and save the tree after deletions
    plot_tree(tree, "tree_after_deletion.png")
    print("Tree after deletions saved as 'tree_after_deletion.png'")

if __name__ == "__main__":
    main()
