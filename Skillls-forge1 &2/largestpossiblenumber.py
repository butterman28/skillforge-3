from functools import cmp_to_key
def compare(a, b):
    # Compare two strings by concatenating them in different orders
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

def printLargest(arr):
    # Sort the array using the custom comparison function
    arr.sort(key=cmp_to_key(compare))
    
    # Concatenate the sorted strings and return the result
    return ''.join(arr)

# Example usage:
arr1 = ["3", "30", "34", "5", "9"]
arr2 = ["54", "546", "548", "60"]
print(printLargest(arr1))  # Output: "9534330"
print(printLargest(arr2))  # Output: "6054854654"
