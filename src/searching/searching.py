# STRETCH: implement Linear Search


def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(list, target):
    if len(list) == 0:
        return -1  # no items in list
    low = 0
    high = len(list) - 1
    while low <= high:
        guess = (low + high) // 2
        if list[guess] == target:
            return guess
        elif list[guess] > target:
            high = guess - 1
        else:
            low = guess + 1
    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(list, target, low, high):
    if len(list) == 0:
        return -1  # array empty
    guess = (low + high) // 2
    if list[guess] == target:
        return guess
    elif list[guess] > target:
        high = guess - 1
        return binary_search_recursive(list, target, low, high)
    else:
        low = guess + 1
        return binary_search_recursive(list, target, low, high)


if __name__ == "__main__":
    list = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
    print(linear_search(list, 0))
    print(binary_search(list, 0))
    print(binary_search_recursive(list, 0, 0, (len(list) - 1)))
