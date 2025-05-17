import tkinter as tk
from tkinter import ttk
import time
import random
from visualization.visualizer import AlgorithmVisualizer

class BubbleSortVisualizer(AlgorithmVisualizer):
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
        return "Bubble Sort Visualization"
    
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
        self.ax.set_title("Bubble Sort")
        self.ax.set_xlabel("Index")
        self.ax.set_ylabel("Value")
        self.ax.set_xticks(range(len(self.array)))
        self.ax.set_xticklabels(range(len(self.array)))
        self.ax.set_ylim(0, max(self.array) * 1.1)
        
        # Update the canvas
        self.canvas.draw()
    
    def start(self):
        self.bubble_sort()
    
    def bubble_sort(self):
        n = len(self.array)
        swapped = True
        
        self.log("Starting Bubble Sort")
        
        # Initialize all bars to default color
        self.colors = ['#CCCCCC'] * n
        self.update_visualization()
        
        # Outer loop for passes
        for i in range(n):
            swapped = False
            
            # Inner loop for comparisons and swaps
            for j in range(0, n - i - 1):
                # Highlight bars being compared
                self.colors = ['#CCCCCC'] * n
                self.colors[j] = '#FF7700'     # Current element (orange)
                self.colors[j + 1] = '#00AAFF'  # Next element (blue)
                self.update_visualization()
                
                # Delay for visualization
                time.sleep(0.5 / self.speed_var.get())
                
                # Compare adjacent elements
                if self.array[j] > self.array[j + 1]:
                    # Swap the elements
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    swapped = True
                    
                    # Highlight swapped bars
                    self.colors[j] = '#FF0000'      # Red for swapped
                    self.colors[j + 1] = '#FF0000'
                    self.update_visualization()
                    
                    self.log(f"swap {j} and {j+1}")
                    
                    # Delay after swap
                    time.sleep(0.5 / self.speed_var.get())
            
            # If no swapping occurred in this pass, array is sorted
            if not swapped:
                break
                
        # Show sorted array with all bars in green
        self.colors = ['#00AA00'] * n  # Green for sorted
        self.update_visualization()
        self.log(f"sorted array = {self.array}")