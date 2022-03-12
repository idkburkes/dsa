
def insert_shift_array(list, val):
   # handle edge cases
   if not list:
       return [val]
   elif len(list) == 1:
       list.append(val)
       return list
   # calculate midpoint and set index pointer to last element
   mid = len(list) // 2
   curIndex = len(list) - 1
  
   while curIndex >= mid:
       # shift current element right
       if curIndex == len(list) - 1:
           list.append(list[curIndex])
       else:
           list[curIndex + 1] = list[curIndex]
        # decrement current index pointer
       curIndex -= 1
    # add new value to the midpoint
   list[curIndex + 1] = val
   return list


if __name__ == "__main__":
    list = [5,8,2,9,-1]
    val = 7
    shifted_list = insert_shift_array(list, val)

    print(shifted_list)

    list2 = [1,2]
    val2 = 3
    shifted_list2 = insert_shift_array(list2, val2)
    print(shifted_list2)



