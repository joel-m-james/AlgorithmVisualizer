import tkinter as tk
from tkinter import ttk
import time
import random
from visualization.visualizer import AlgorithmVisualizer

class InsertionSortVisualizer(AlgorithmVisualizer):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Add array size control
        ttk.Label(self.control_frame, text="Array Size:").pack(side=tk.LEFT, padx=5, pady=5)
        self.size_var = tk.IntVar(value=15)
        self.size_spinbox = ttk.Spinbox(self.control_frame, from_=5, to=50, 
                                        textvariable=self.size_var, width=5)
        self.size_spinbox.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Generate new data button
        ttk.Button(self.control_frame, text="New Data", 
                  command=self.setup_data).pack(side=tk.LEFT, padx=5, pady=5)
        
        # Initialize the array and visualization
        self.setup_data()
        self.fig, self.ax = self.setup_canvas()
        self.update_visualization()
    
    def get_title(self):
        return "Insertion Sort Visualization"
    
    def setup_data(self):
        # Generate random array
        size = self.size_var.get()
        self.array = [random.randint(1, 10) for _ in range(size)]
        self.colors = ['#CCCCCC'] * len(self.array)  # Default color
        self.clear_log()
        self.log(f"Generated new array: {self.array}")
        if hasattr(self, 'ax'):
            self.update_visualization()
    
    def update_visualization(self):
        self.ax.clear()
        
        # Create bar chart
        bars = self.ax.bar(range(len(self.array)), self.array, color=self.colors)
        
        # Set plot properties
        self.ax.set_title("Insertion Sort")
        self.ax.set_xlabel("Index")
        self.ax.set_ylabel("Value")
        self.ax.set_xticks(range(len(self.array)))
        self.ax.set_xticklabels(range(len(self.array)))
        self.ax.set_ylim(0, max(self.array) * 1.1)
        
        # Update the canvas
        self.canvas.draw()
    
    def start(self):
        self.insertion_sort()
    
    def insertion_sort(self):
        n = len(self.array)
        
        self.log("Starting Insertion Sort")
        
        # First element is already sorted
        self.colors[0] = '#00AA00'  # Green for sorted
        self.update_visualization()
        time.sleep(0.5 / self.speed_var.get())
        
        # Start from the second element
        for i in range(1, n):
            # Key to be inserted
            key = self.array[i]
            
            # Highlight current element being inserted
            self.colors = ['#00AA00'] * i + ['#CCCCCC'] * (n - i)
            self.colors[i] = '#FF7700'  # Orange for current key
            self.update_visualization()
            self.log(f"Inserting element {key} at position {i}")
            time.sleep(0.5 / self.speed_var.get())
            
            # Move elements of arr[0..i-1] that are greater than key 
            # to one position ahead of their current position
            j = i - 1
            while j >= 0 and self.array[j] > key:
                # Highlight comparison
                self.colors[j] = '#FF0000'  # Red for element being compared
                self.update_visualization()
                time.sleep(0.3 / self.speed_var.get())
                
                # Move the element
                self.array[j + 1] = self.array[j]
                
                # Log the swap
                self.log(f"Moving {self.array[j]} from position {j} to {j+1}")
                
                # Update visualization after move
                self.colors = ['#00AA00'] * i + ['#CCCCCC'] * (n - i)
                self.colors[j + 1] = '#FF0000'  # Red for moved element
                self.update_visualization()
                time.sleep(0.3 / self.speed_var.get())
                
                j -= 1
            
            # Place the key in its correct position
            self.array[j + 1] = key
            
            # Update sorted portion
            self.colors = ['#00AA00'] * (i + 1) + ['#CCCCCC'] * (n - i - 1)
            self.update_visualization()
            time.sleep(0.5 / self.speed_var.get())
        
        # Show sorted array with all bars in green
        self.colors = ['#00AA00'] * n  # Green for sorted
        self.update_visualization()
        self.log(f"sorted array = {self.array}")