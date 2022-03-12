
def insertion_sort(arr):

    for i in range(1, len(arr)):
        j = i - 1
        temp = arr[i]

        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = temp

def sort_and_display(array):
    print('Initial: ', array)
    insertion_sort(array)
    print('After sort: ', array, '\n')


if __name__ == '__main__':
    array = [8,4,23,42,16,15]
    sort_and_display(array)
  
    reverse_sorted = [20,18,12,8,5,-2]
    sort_and_display(reverse_sorted)

    few_uniques = [5,12,7,5,5,7]
    sort_and_display(few_uniques)

    nearly_sorted = [2,3,5,7,13,11]
    sort_and_display(nearly_sorted)