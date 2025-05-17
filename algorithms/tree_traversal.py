import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import time
from visualization.visualizer import AlgorithmVisualizer

class TreeTraversalVisualizer(AlgorithmVisualizer):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Add algorithm selection
        ttk.Label(self.control_frame, text="Traversal:").pack(side=tk.LEFT, padx=5, pady=5)
        self.algorithm_var = tk.StringVar()
        self.algorithm_combo = ttk.Combobox(self.control_frame, textvariable=self.algorithm_var)
        self.algorithm_combo['values'] = ('In-Order', 'Pre-Order', 'Post-Order')
        self.algorithm_combo.current(0)
        self.algorithm_combo.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Initialize the binary tree and visualization
        self.setup_data()
        self.fig, self.ax = self.setup_canvas()
        self.update_visualization()
    
    def get_title(self):
        return "Binary Tree Traversal"
    
    def setup_data(self):
        # Binary tree structure similar to the screenshot
        # Format: [left_child, right_child]
        self.tree = {
            5: [3, 8],
            3: [1, 4],
            8: [6, 10],
            1: [0, 2],
            4: [-1, -1],  # -1 means no child
            6: [-1, 7],
            10: [9, -1],
            0: [-1, -1],
            2: [-1, -1],
            7: [-1, -1],
            9: [-1, -1]
        }
        
        # Node positions (manually defined for tree layout)
        self.node_positions = {
            5: (0.5, 0.9),    # Root level
            3: (0.3, 0.7),    # Level 1
            8: (0.7, 0.7),    # Level 1
            1: (0.2, 0.5),    # Level 2
            4: (0.4, 0.5),    # Level 2
            6: (0.6, 0.5),    # Level 2
            10: (0.8, 0.5),   # Level 2
            0: (0.1, 0.3),    # Level 3
            2: (0.3, 0.3),    # Level 3
            7: (0.7, 0.3),    # Level 3
            9: (0.9, 0.3),    # Level 3
        }
        
        # Initialize node colors (gray by default)
        self.node_colors = {node: '#CCCCCC' for node in self.tree.keys()}
        self.edge_colors = {}
        
        # Initialize edges
        for parent, children in self.tree.items():
            for i, child in enumerate(children):
                if child != -1:
                    self.edge_colors[(parent, child)] = '#CCCCCC'
        
        # Current traversal path
        self.current_path = []
        self.visited_nodes = set()
    
    def update_visualization(self):
        self.ax.clear()
        
        # Draw edges first (so they're behind nodes)
        for (u, v), color in self.edge_colors.items():
            # Get positions
            pos_u = self.node_positions[u]
            pos_v = self.node_positions[v]
            
            # Draw the edge as an arrow
            self.ax.annotate("", xy=pos_v, xytext=pos_u,
                          arrowprops=dict(arrowstyle="->", color=color, lw=2))
        
        # Draw nodes
        for node, pos in self.node_positions.items():
            color = self.node_colors[node]
            circle = plt.Circle(pos, 0.05, color=color, ec='black', zorder=2)
            self.ax.add_patch(circle)
            
            # Add node label
            self.ax.text(pos[0], pos[1], str(node), ha='center', va='center', 
                     fontweight='bold', color='black', zorder=3)
        
        # Set plot limits and turn off axes
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.set_title(f"{self.algorithm_var.get()} Traversal")
        self.ax.axis('off')
        
        # Update the canvas
        self.canvas.draw()
    
    def start(self):
        self.reset()
        algorithm = self.algorithm_var.get()
        
        root_node = 5  # Root node from the tree structure
        
        if algorithm == 'In-Order':
            self.traverse_inorder(root_node)
        elif algorithm == 'Pre-Order':
            self.traverse_preorder(root_node)
        elif algorithm == 'Post-Order':
            self.traverse_postorder(root_node)
    
    def update_node(self, node, message=None):
        # Update node color (highlight current node in red/pink)
        self.node_colors[node] = '#FF5C8A'  # Pink color from screenshot
        
        # Update edge colors for the path
        if len(self.current_path) > 1:
            for i in range(len(self.current_path) - 1):
                u, v = self.current_path[i], self.current_path[i+1]
                if (u, v) in self.edge_colors:
                    self.edge_colors[(u, v)] = '#FF5C8A'
        
        # Log the action
        if message:
            self.log(message)
        
        # Update the visualization
        self.update_visualization()
        
        # Control animation speed
        delay = 1.0 / self.speed_var.get()
        time.sleep(delay)
    
    def traverse_inorder(self, node, depth=0):
        if node == -1:
            return
        
        # Keep track of path
        self.current_path.append(node)
        
        # Process left subtree
        left_child = self.tree[node][0]
        if left_child != -1:
            self.log(f"Going left from {node}")
            self.update_node(node, f"Going left from {node}")
            self.traverse_inorder(left_child, depth + 1)
        else:
            self.log(f"No more nodes. Backtracking.")
            
        # Process current node
        if node not in self.visited_nodes:
            self.visited_nodes.add(node)
            self.log(f"Printing {node}")
            self.update_node(node, f"Printing {node}")
        
        # Process right subtree
        right_child = self.tree[node][1]
        if right_child != -1:
            self.log(f"Going right from {node}")
            self.update_node(node, f"Going right from {node}")
            self.traverse_inorder(right_child, depth + 1)
        else:
            self.log(f"No more nodes. Backtracking.")
        
        # Remove from current path when backtracking
        self.current_path.pop()
    
    def traverse_preorder(self, node):
        if node == -1:
            return
        
        # Keep track of path
        self.current_path.append(node)
        
        # Process current node first
        if node not in self.visited_nodes:
            self.visited_nodes.add(node)
            self.log(f"Printing {node}")
            self.update_node(node, f"Printing {node}")
        
        # Then process left subtree
        left_child = self.tree[node][0]
        if left_child != -1:
            self.log(f"Going left from {node}")
            self.update_node(node, f"Going left from {node}")
            self.traverse_preorder(left_child)
        else:
            self.log(f"No left child for {node}")
        
        # Then process right subtree
        right_child = self.tree[node][1]
        if right_child != -1:
            self.log(f"Going right from {node}")
            self.update_node(node, f"Going right from {node}")
            self.traverse_preorder(right_child)
        else:
            self.log(f"No right child for {node}")
        
        # Remove from current path when backtracking
        self.current_path.pop()
    
    def traverse_postorder(self, node):
        if node == -1:
            return
        
        # Keep track of path
        self.current_path.append(node)
        
        # Process left subtree first
        left_child = self.tree[node][0]
        if left_child != -1:
            self.log(f"Going left from {node}")
            self.update_node(node, f"Going left from {node}")
            self.traverse_postorder(left_child)
        else:
            self.log(f"No left child for {node}")
        
        # Then process right subtree
        right_child = self.tree[node][1]
        if right_child != -1:
            self.log(f"Going right from {node}")
            self.update_node(node, f"Going right from {node}")
            self.traverse_postorder(right_child)
        else:
            self.log(f"No right child for {node}")
        
        # Process current node last
        if node not in self.visited_nodes:
            self.visited_nodes.add(node)
            self.log(f"Printing {node}")
            self.update_node(node, f"Printing {node}")
        
        # Remove from current path when backtracking
        self.current_path.pop()