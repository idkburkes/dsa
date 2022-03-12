

def reverseArray(list):
    if(list is None or len(list) <= 1):
        return list

    left = 0
    right = len(list) - 1
    while(left <= right):
        swap(list, left, right)
        left += 1
        right -= 1
    return list


def swap(list, left, right):
    temp = list[left]
    list[left] = list[right]
    list[right] = temp
    return list


if __name__ == '__main__':
    list = [5,4,1,5,7,54,2,89,2]
    
    print(f'initial list: {list}')
    print(f'reversed list: {reverseArray(list)}')