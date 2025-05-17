import random

def generate_random_array(size, min_val=1, max_val=10):
    """Generate a random array of integers
    
    Args:
        size (integer): Array size
        min_val (integer): Min value (inclusive)
        max_val (integer): Max value (inclusive)
    
    Returns:
        list: Random array of integers
    """
    return [random.randint(min_val, max_val) for _ in range(size)]

def generate_nearly_sorted_array(size, swaps=None):
    """Generate a nearly sorted array by starting with a sorted array
    and performing a few random swaps
    
    Args:
        size (int): Size of the array
        swaps (int): Number of swaps to perform. If None, uses sqrt(size).
    
    Returns:
        list: Nearly sorted array
    """
    if swaps is None:
        swaps = int(size ** 0.5)
    
    # Create sorted array
    arr = list(range(1, size + 1))
    
    # Perform random swaps
    for _ in range(swaps):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr

def generate_reversed_array(size):
    """Generate a reversed (sorted in descending order) array
    
    Args:
        size (int): Size of the array
    
    Returns:
        list: Reversed array
    """
    return list(range(size, 0, -1))

def generate_few_unique_array(size, unique_vals=3):
    """Generate an array with few unique values
    
    Args:
        size (int): Size of the array
        unique_vals (int): Number of unique values
    
    Returns:
        list: Array with few unique values
    """
    values = list(range(1, unique_vals + 1))
    return [random.choice(values) for _ in range(size)]