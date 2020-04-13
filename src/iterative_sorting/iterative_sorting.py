# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for item in arr:
            if item > arr[cur_index]:
                smallest_index = arr.index(item)
                arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # pass_count = 0
    # while pass_count < 35:
    #     for i in range(0, len(arr) - 1):
    #         cur_index = i
    #         next_index = i + 1
    #         if arr[cur_index] > arr[next_index]:
    #             arr[cur_index], arr[next_index] = arr[next_index], arr[cur_index]
    #         else:
    #             pass_count += 1
    #             print(pass_count)
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


test_arr = [5, 8, 1, 2, 6, 9, 0, 10, 3]
bubble_sort(test_arr)
print(test_arr)


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
