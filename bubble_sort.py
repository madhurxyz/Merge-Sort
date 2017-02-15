#Best Case: O(n)
#Worst Case: O(n^2)
def bubble_sort(array):
    is_sorted = True
    while is_sorted:
        is_sorted = False
        for i in range(len(array)-1):
            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                is_sorted = True
    return array

if __name__ == "__main__":
    import random
    array = [random.randint(-1000,1000) for _ in range(100)]
    print "\nUnsorted Array: {}\n".format(array)
    bubble_sort(array)
    print "\nSorted Array: {}\n".format(array)
