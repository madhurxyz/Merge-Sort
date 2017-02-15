def merge_sort(array):
    # splitting
    if len(array)>1:
        middle = len(array)//2
        left_array = array[:middle]
        right_array = array[middle:]

        merge_sort(left_array)
        merge_sort(right_array)

        left = 0
        right = 0
        index = 0

        # walk through array halves and copy over the smaller elements
        while left < len(left_array) and right < len(right_array):
            if left_array[left] < right_array[right]:
                array[index]=left_array[left]
                left += 1
            else:
                array[index]=right_array[right]
                right += 1
            index += 1

        # walk through array halves and copy over the remaining elements
        while left < len(left_array):
            array[index]=left_array[left]
            left += 1
            index += 1

        while right < len(right_array):
            array[index]=right_array[right]
            right += 1
            index += 1

if __name__ == "__main__":
    import random
    array = [random.randint(-1000,1000) for _ in range(100)]
    print "\nUnsorted Array: {}\n".format(array)
    merge_sort(array)
    print "\nSorted Array: {}\n".format(array)
