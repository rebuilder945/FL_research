

def BinSearch(array, key, low, high):

    mid = int((low+high)/2)

    if key == int(array[mid][0]):  # 若找到

        return array[mid]

    if low > high:

        return False



    if key < int(array[mid][0]):

        return BinSearch(array, key, low, mid-1)  #递归

    if key > int(array[mid][0]):

        return BinSearch(array, key, mid+1, high)







if __name__ == "__main__":

    array = []

    for i in range(1,21):

        array.append([str(i),'学生'+str(i)])



    ret = BinSearch(array, 20, 0, len(array)-1)  # 通过折半查找，找到65

    print(ret)

