



def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1



if __name__ == '__main__':
    list = [-131, -82, 0, 27, 42, 68, 179]
    
    test_one = binary_search(list, 42)
    test_two = binary_search(list, -131)
    test_three = binary_search(list, 179)

    print(test_one, test_two, test_three)