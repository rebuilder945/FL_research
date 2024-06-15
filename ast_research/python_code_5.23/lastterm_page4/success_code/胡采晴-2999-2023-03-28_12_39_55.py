def beginOrend(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]
    return arr

arr = input()
pos1 = int(input())
pos2 = int(input())
print(beginOrend(arr, pos1, pos2))
