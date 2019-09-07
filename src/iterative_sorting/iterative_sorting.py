# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(1, len(arr)):
        cur_index = i
        while cur_index > 0 and arr[cur_index] < arr[cur_index - 1]:
            arr[cur_index], arr[cur_index - 1] = arr[cur_index - 1], arr[cur_index]
            cur_index -= 1
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
