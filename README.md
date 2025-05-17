# Algorithm Visualizer

## Overview

Algorithm Visualizer is a Python-based educational tool designed to help developers understand and learn algorithms through visualization. This project allows you to see algorithms in action, making it easier to grasp complex concepts by visualizing each step of the process.

The motivation behind this project was my personal need to improve my understanding of algorithms. By seeing algorithms work in real-time with visual feedback, I found I could grasp concepts more intuitively than by just reading code or pseudocode.

## Features

- **Visualizations** of various algorithms
- **Step-by-step execution** to follow algorithm progress
- **Detailed logging** of algorithm operations
- **Adjustable animation speed** for better understanding

## Algorithms Implemented

### Sorting Algorithms (for now, more to be added!)
- **Bubble Sort**: Repeatedly steps through the list, compares adjacent elements, and swaps them if they're in the wrong order.
- **Insertion Sort**: Builds the sorted array one item at a time by taking elements from the unsorted part and inserting them into their correct position.

### Data Structure Operations
- **Binary Tree Traversal**:
  - In-Order Traversal (left, root, right)
  - Pre-Order Traversal (root, left, right)
  - Post-Order Traversal (left, right, root)

## Getting Started

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually comes with Python)
- Matplotlib
- NumPy

### Installation

1. Clone this repository
```bash
git clone https://github.com/joel-m-james/AlgorithmVisualizer.git
cd AlgorithmVisualizer
```

2. Install the required dependencies
```bash
pip install matplotlib numpy
```

3. Run the application
```bash
python main.py
```

## Usage

1. **Select an algorithm** from the tabs at the top
2. **Configure parameters** like array size if applicable
3. **Click "Start"** to begin the visualization
4. Use the **speed slider** to adjust how fast the visualization runs
5. Watch the **visualization** and follow the **log** to understand each step

## Project Structure

```
algorithm_visualizer/
│
├── main.py                # Main application entry point
├── visualization/         # Core visualization components
│   ├── __init__.py
│   ├── visualizer.py      # Base visualizer class
│   └── ui_components.py   # Common UI elements
│
├── algorithms/            # Algorithm implementations
│   ├── __init__.py
│   ├── tree_traversal.py  # Binary tree traversal algorithms
│   ├── bubble_sort.py     # Bubble sort implementation
│   └── insertion_sort.py  # Insertion sort implementation
│
└── utils/                 # Utility functions
    ├── __init__.py
    └── data_generator.py  # Functions to generate test data
```

## Learning Outcomes

This project has helped me:

1. **Understand algorithm behavior** more intuitively by watching them execute
2. **Identify performance characteristics** by observing how algorithms handle different inputs
3. **Debug complex algorithms** by stepping through the visualization
4. **Compare different approaches** to solving the same problem

## Future Improvements

- Add more sorting algorithms (Quick Sort, Merge Sort, Selection Sort)
- Implement graph algorithms (DFS, BFS, Dijkstra's)
- Add complexity analysis information
- Create a code view to show the current line being executed
- Add the ability to input custom datasets

## Contributing

Contributions are welcome! If you'd like to add a new algorithm or improve the existing visualizations:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-algorithm`)
3. Commit your changes (`git commit -m 'Add amazing algorithm'`)
4. Push to the branch (`git push origin feature/amazing-algorithm`)
5. Open a Pull Request


## Acknowledgments

- Inspired by various algorithm visualization websites and tools
- Thanks to all the computer science educators who emphasize the importance of visualization in learning algorithms

---

*This project was created as a tool for learning and understanding algorithms better. If you find it helpful for your own learning journey, please star the repository and share it with others who might benefit from it!*