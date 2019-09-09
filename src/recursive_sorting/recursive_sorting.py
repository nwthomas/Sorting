from math import floor


def merge(listA, listB):
    elements = len(listA) + len(listB)
    merged_arr = []
    for i in range(elements):
        if len(listA) == 0:
            merged_arr.append(listB[0])
            listB = listB[1:]
        elif len(listB) == 0:
            merged_arr.append(listA[0])
            listA = listA[1:]
        elif listA[0] < listB[0]:
            merged_arr.append(listA[0])
            listA = listA[1:]
        else:
            merged_arr.append(listB[0])
            listB = listB[1:]
    return merged_arr


def merge_sort(list):
    if len(list) <= 1:
        return list
    else:
        pivot_index = floor(len(list) / 2)
        left = list[:pivot_index]
        right = list[pivot_index:]
    return merge(merge_sort(left), merge_sort(right))


print(merge_sort([4, 3, 7, 2, 88, 4, 5, 2, 1, 300, 100, 200, 1000]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
