def insert_sort(somelist):
    for i in range(1, len(somelist)):
        key = somelist[i]
        j = i - 1
        while i > 0 and somelist[j] > key:
            somelist[j + 1] = somelist[j]
            j = j - 1
        somelist[j + 1] = key
    return somelist


# Python program for implementation of MergeSort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list
def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.data = None
if __name__ == '__main__':
    local_list = [0, 1, 5, 5, 2, 8, 3, 6, 4]
    print(local_list)
    print(insert_sort(local_list))

    arr = [12, 11, 13,13, 5]
    print("Given array is:", end="\n")
    print_list(arr)
    merge_sort(arr)
    print("Sorted array is: ", end="\n")
    print_list(arr)
    root = Node(2)
    root.left = Node(3)
    root.right = Node(5)
    