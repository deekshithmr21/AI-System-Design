def find_largest_element_sorting(arr):
    """
    Finds the largest element in a given array by sorting.

    Args:
        arr: A list of numbers.

    Returns:
        The largest element in the array.
    """
    if not arr:
        return None
    sorted_arr = sorted(arr)  
    return sorted_arr[-1]

# Example usage:
my_array = [10, 324, 45, 90, 9808]
largest = find_largest_element_sorting(my_array)
print(f"The largest element in the array (using sorting) is: {largest}")