# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # starting at the beginning of `a` and `b`
    # compare the next value of each
    # add smallest to `merged_arr`
    merged_arr = []

    # this loop will run as long as both arrays have content
    while len(arrA) > 0 and len(arrB) > 0:
        # smallest will contain the value we determine is smaller
        smallest = 0

        # if A is smaller, pop it off and assign it to smallest; 
        # otherwise assign B
        if arrA[0] < arrB[0]:
            smallest = arrA.pop(0)
        else:
            smallest = arrB.pop(0)

        # once we've determined which is smaller append that to our merged list
        merged_arr.append(smallest)

    # when we get out of the while loop and one array has run out of length
    # we want to extend the contents of the remaining array onto the end of merged
    if len(arrA) > 0:
        merged_arr.extend(arrA)
    else:
        merged_arr.extend(arrB)

    #finally return the re-merged array
    print(merged_arr)
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # check if the list is less than 2; 
    # if it is, it's sorted
    if len(arr) < 2:
        return arr
    # if it's unsorted:
    else:
        # determine the midpoint, 
        # and set our left and right arrays using that point
        midpoint = len(arr) // 2
        left = arr[0:midpoint]
        right = arr[midpoint:]
        # our finished array will be the result of a merge
        # between the recursive calls of merge sort which will return arrays when sorted
        arr = merge(merge_sort(left), merge_sort(right))
    return arr



# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

