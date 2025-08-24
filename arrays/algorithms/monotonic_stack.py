def next_greater_element(arr):
    """
    Find the next greater element for each element in the array.
    Returns an array where result[i] is the next greater element for arr[i],
    or -1 if no greater element exists.
    """
    n = len(arr)
    result = [-1] * n
    stack = []  # Will store indices

    # Scan left to right for next greater
    for i in range(n):
        # Pop elements smaller than current
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)

    return result


def prev_greater_element(arr):
    """
    Find the previous greater element for each element in the array.
    Returns an array where result[i] is the previous greater element for arr[i],
    or -1 if no greater element exists.
    """
    n = len(arr)
    result = [-1] * n
    stack = []  # Will store indices

    # Scan right to left for previous greater
    for i in range(n - 1, -1, -1):
        # Pop elements smaller than current
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)

    return result


def next_smaller_element(arr):
    """
    Find the next smaller element for each element in the array.
    Returns an array where result[i] is the next smaller element for arr[i],
    or -1 if no smaller element exists.
    """
    n = len(arr)
    result = [-1] * n
    stack = []  # Will store indices

    # Scan left to right for next smaller
    for i in range(n):
        # Pop elements greater than current
        while stack and arr[stack[-1]] > arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)

    return result


def prev_smaller_element(arr):
    """
    Find the previous smaller element for each element in the array.
    Returns an array where result[i] is the previous smaller element for arr[i],
    or -1 if no smaller element exists.
    """
    n = len(arr)
    result = [-1] * n
    stack = []  # Will store indices

    # Scan right to left for previous smaller
    for i in range(n - 1, -1, -1):
        # Pop elements greater than current
        while stack and arr[stack[-1]] > arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)

    return result


def get_next_prev_indices(arr):
    """
    Returns indices of next and previous greater/smaller elements.
    Useful for problems like largest rectangle in histogram.
    """
    n = len(arr)
    next_greater_idx = [n] * n
    prev_greater_idx = [-1] * n
    next_smaller_idx = [n] * n
    prev_smaller_idx = [-1] * n

    # Next greater indices
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            next_greater_idx[stack.pop()] = i
        stack.append(i)

    # Previous greater indices
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] < arr[i]:
            prev_greater_idx[stack.pop()] = i
        stack.append(i)

    # Next smaller indices
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            next_smaller_idx[stack.pop()] = i
        stack.append(i)

    # Previous smaller indices
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            prev_smaller_idx[stack.pop()] = i
        stack.append(i)

    return {
        "next_greater": next_greater_idx,
        "prev_greater": prev_greater_idx,
        "next_smaller": next_smaller_idx,
        "prev_smaller": prev_smaller_idx,
    }


def demonstrate_monotonic_stack():
    test_cases = [
        [4, 5, 2, 10, 8],
        [3, 1, 4, 1, 5, 9, 2, 6, 5],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1],
        [],
    ]

    for arr in test_cases:
        print(f"\nArray: {arr}")
        print(f"Next Greater:  {next_greater_element(arr)}")
        print(f"Prev Greater:  {prev_greater_element(arr)}")
        print(f"Next Smaller:  {next_smaller_element(arr)}")
        print(f"Prev Smaller:  {prev_smaller_element(arr)}")

        # Get indices for all relationships
        indices = get_next_prev_indices(arr)
        print("\nIndices:")
        for key, value in indices.items():
            print(f"{key}: {value}")


# Example usage
if __name__ == "__main__":
    demonstrate_monotonic_stack()
