import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Algorithm Visualizer")
    root.geometry("1200x800")
    
    # Create notebook for different algorithm types
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True)
    
    # Import algorithm visualizers
    from algorithms.tree_traversal import TreeTraversalVisualizer
    from algorithms.bubble_sort import BubbleSortVisualizer
    from algorithms.insertion_sort import InsertionSortVisualizer
    
    
    # Create tabs for each algorithm type
    tree_frame = ttk.Frame(notebook)
    bubble_frame = ttk.Frame(notebook)
    insertion_frame = ttk.Frame(notebook)
 
    
    notebook.add(tree_frame, text="Tree Traversal")
    notebook.add(bubble_frame, text="Bubble Sort")
    notebook.add(insertion_frame, text="Insertion Sort")
    
    
    # Initialize visualizers in their respective tabs
    tree_vis = TreeTraversalVisualizer(tree_frame)
    bubble_vis = BubbleSortVisualizer(bubble_frame)
    insertion_vis = InsertionSortVisualizer(insertion_frame)
  
    
    root.mainloop()

if __name__ == "__main__":
    main()