list = input().split()
n, m = map(int, input().split())
temp = list[m]
list[m] = list[n]
list[n] = temp
ptint(list)
