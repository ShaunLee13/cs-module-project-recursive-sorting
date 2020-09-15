# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # base case; this determines that the search area has length
    if end >= start:
        # next assign midpoint and check it against target
        # if equivalent, return index of midpoint and escape function
        midpoint = (end + start) // 2
        if arr[midpoint] == target:
            return midpoint
        # otherwise we'll compare whether < or > than midpoint
        # to determine where to set our sub-array
        elif arr[midpoint] > target:
            # if greater, target is in lower half
            # and so our search area will end at the index before midpoint
            return binary_search(arr, target, start, midpoint-1)
        else:
            # otherwise target is in upper half so our new start will 
            # be the next index after midpoint
            return binary_search(arr, target, midpoint+1, end)
    # if we have no more search area, or if array is empty, return -1
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

