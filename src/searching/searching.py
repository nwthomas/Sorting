from math import floor

# STRETCH: implement Linear Search


def linear_search(arr, target):

  # TO-DO: add missing code

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(list, target):
    if len(list) == 0:
        return -1  # no items in list
    low = 0
    high = len(list) - 1
    while low <= high:
        guess = floor(low + high / 2)
        if list[guess] == target:
            return guess
        elif list[guess] > target:
            high = guess - 1
        else:
            low = guess + 1
    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls


if __name__ == "__main__":
    print(binary_search([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9], 0))
