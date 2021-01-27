'''
In computer science, binary search, also known as half-interval search, logarithmic search, 
or binary chop, is a search algorithm that finds the position of a target value within a 
sorted array. Binary search compares the target value to the middle element of the array.

Write a binary search using recursion.
'''

# Method * 1

def binary_search(data, target):

    low = 0
    high = len(data) - 1
    mid = (low + high) // 2 + 1

    if mid > high:
        if data[mid - 1] != target:
            return False
        else:
            return True

    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data[:mid], target)
    else:
        return binary_search(data[mid:], target)
    
 
# Method * 2

# def binary_search(data, target, low, high):
#
#     if low > high:
#         return False
#     else:
#         mid = (low + high) // 2
#         if target == data[mid]:
#             return True
#         elif target < data[mid]:
#             return binary_search(data, target, low, mid - 1)
#         else:
#             return binary_search(data, target, mid + 1, high)
        
