import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter.font as tkFont

class AlgorithmVisualizer: 
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the basic UI components"""
        # Control frame at the top
        self.control_frame = ttk.Frame(self.parent)
        self.control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        
        # Main content area
        self.content_frame = ttk.Frame(self.parent)
        self.content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Create a panedwindow to allow resizing between visualization and log
        self.paned_window = ttk.PanedWindow(self.content_frame, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)
        
        # Visualization area (left side)
        self.viz_frame = ttk.Frame(self.paned_window)
        
        # Log area (right side) - make it wider
        self.log_frame = ttk.Frame(self.paned_window)
        
        # Add both frames to the paned window
        self.paned_window.add(self.viz_frame, weight=2)  # Visualization gets 2/3 of space
        self.paned_window.add(self.log_frame, weight=1)  # Log gets 1/3 of space
        
        # Setup log window
        log_header_frame = ttk.Frame(self.log_frame)
        log_header_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(log_header_frame, text="Algorithm Log:", font=("Arial", 12, "bold")).pack(anchor=tk.W)
        
        # Create a custom font for the log text
        log_font = tkFont.Font(family="Courier", size=11)
        
        # Use a Frame with scrollbar for the log
        log_container = ttk.Frame(self.log_frame)
        log_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create scrollbar first
        scrollbar = ttk.Scrollbar(log_container)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Now create the text widget with the scrollbar
        self.log_widget = tk.Text(log_container, wrap=tk.WORD, width=50, height=30, 
                                font=log_font, bg="#f5f5f5", padx=8, pady=8)
        self.log_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Connect scrollbar to text widget
        self.log_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.log_widget.yview)
        
        # Add a clear log button
        ttk.Button(log_header_frame, text="Clear Log", command=self.clear_log).pack(side=tk.RIGHT)
        
        # Speed control
        speed_frame = ttk.LabelFrame(self.control_frame, text="Animation Speed")
        speed_frame.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.speed_var = tk.DoubleVar(value=1.0)
        self.speed_scale = ttk.Scale(speed_frame, from_=0.1, to=3.0, 
                                   orient=tk.HORIZONTAL, variable=self.speed_var, 
                                   length=150)
        self.speed_scale.pack(side=tk.LEFT, padx=5, pady=5)
        
        ttk.Label(speed_frame, text="Slow").pack(side=tk.LEFT, padx=(0,5))
        ttk.Label(speed_frame, text="Fast").pack(side=tk.RIGHT, padx=(5,0))
        
        # Common buttons - group them in a frame
        button_frame = ttk.Frame(self.control_frame)
        button_frame.pack(side=tk.RIGHT, padx=10)
        
        ttk.Button(button_frame, text="Reset", command=self.reset, 
                 width=10).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(button_frame, text="Start", command=self.start, 
                 width=10).pack(side=tk.LEFT, padx=5, pady=5)
    
    def setup_canvas(self):
        """Set up the matplotlib canvas for visualization"""
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.viz_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.ax.set_title(self.get_title())
        return self.fig, self.ax
    
    def log(self, message):
        """Add message to the log widget"""
        self.log_widget.insert(tk.END, message + "\n")
        self.log_widget.see(tk.END)
        self.parent.update()
    
    def clear_log(self):
        """Clear log widget"""
        self.log_widget.delete(1.0, tk.END)
    
    def get_title(self):
        """Get title for the visualization"""
        return "Algorithm Visualization"
    
    def reset(self):
        """Reset visualization"""
        self.clear_log()
        self.setup_data()
        self.update_visualization()
    
    def start(self):
        pass
    
    def setup_data(self):
        pass
    
    def update_visualization(self):
        pass