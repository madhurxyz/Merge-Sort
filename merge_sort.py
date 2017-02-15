from bubble_sort import bubble_sort

def divide(array):
    left = array[0:len(array)/2]
    right = array[len(array)/2 + 1: len(array)]
    if len(left) != 2 or len(left) != 3:
        divide(left)
    elif len(left) == 2 or len(left) == 3:
        bubble_sort(left)

    if len(right) != 2 or len(right) != 3:
        divide(right)
    elif len(right) == 2 or len(right) == 3:
        bubble_sort(right)


if __name__ == "__main__":
    array = [0, 6, 3, 40, 35, 86, 73, 96, 12, 5, 10]
    divide(array)
