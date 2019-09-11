# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Boolean flag to check if current iteration has swapped anything
    swapped = False
    for i in range(0, len(arr)):
        # Loops over every time every time
        for j in range(0, len(arr) - 1):
            # Swap elements if j is lesser than j + 1
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Indicate via boolean flag that change has occured
                swapped = True
        # End all loops if not swaps have happend on current iteration
        if not swapped:
            break
        # Else reset boolean flag
        else:
            swapped = False
    return arr


# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
