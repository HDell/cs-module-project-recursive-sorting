# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # base case
    if len(arr) == 1:
        if arr[0] == target:
            return 0
        else:
            return -1
    elif len(arr) == 0:
        return -1

    if arr[end//2] == target:
        return (end//2)
    # recursive cases
    elif target > arr[len(arr)//2]:
        return binary_search(arr[(len(arr)//2)+1:], target, 0, len(arr[(len(arr)//2)+1:])-1)
    else: # target < arr[len(arr)//2]
        return binary_search(arr[0:len(arr)//2], target, 0, len(arr[0:len(arr)//2])-1)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

