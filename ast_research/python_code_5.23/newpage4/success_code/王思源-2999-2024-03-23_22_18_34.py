list = list(input().split(" "))
n,m = eval(input())


for i in range(len(list)):
    temp = list[n]
    list[n] = list[m]
    list[m] = temp
print(list)
