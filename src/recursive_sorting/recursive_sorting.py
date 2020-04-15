# TO-DO: complete the help function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)

    merged_arr = [0] * elements

    # TO-DO
    i_hate = 0
    this = 0

    for i in range(0, elements):
        if i_hate >= len(arrA):
            merged_arr[i] = arrB[this]
            this += 1
        elif this >= len(arrB):
            merged_arr[i] = arrA[i_hate]
            i_hate += 1
        elif arrA[i_hate] < arrB[this]:
            merged_arr[i] = arrA[i_hate]
            i_hate += 1
        else:
            merged_arr[i] = arrB[this]
            this += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO

    if len(arr) < 2:
        return arr
    return merge(merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:]))


merge_sort([2, 0, 1, 4, 5, 9, 11, 3])

###


###


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
