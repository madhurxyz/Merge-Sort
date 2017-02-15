from bubble_sort import bubble_sort

# def divide(array):
#     left = array[0:len(array)/2]
#     right = array[len(array)/2 + 1: len(array)]
#
#     if len(left) != 2 or len(left) != 3:
#         divide(left)
#     elif len(left) == 2 or len(left) == 3:
#         bubble_sort(left)
#
#     if len(right) != 2 or len(right) != 3:
#         divide(right)
#     elif len(right) == 2 or len(right) == 3:
#         bubble_sort(right)
temp = []
def merge_sort(array):
    divide(array, temp, 0, len(array)-1)

def divide(array, temp, leftStart, rightEnd):
    if leftStart >= rightEnd:
        return

    middle = (leftStart + rightEnd)/2

    divide(array, temp, leftStart, middle)
    divide(array, temp, middle + 1, rightEnd)
    merge(array, temp, leftStart, rightEnd)

def merge(array, temp, leftStart, rightEnd):
    leftEnd = (rightEnd + leftStart)/2
    rightStart = leftEnd + 1
    size = rightEnd - leftStart + 1

    left = leftStart
    right = rightStart
    index = leftStart

    while left <= leftEnd and right <= rightEnd:
        if array[left] <= array[right]:
            temp[index] =  array[left]
            left += 1
        else:
            temp[index] = array[right]
            right += 1
        index += 1

    


if __name__ == "__main__":
    array = [0, 6, 3, 40, 35, 86, 73, 96, 12, 5, 10]
    merge_sort(array)
