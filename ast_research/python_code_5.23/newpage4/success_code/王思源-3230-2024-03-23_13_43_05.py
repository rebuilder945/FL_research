list = eval(input())


list.sort()
# list.reverse()
num = 0
for i in range(len(list)):
    num = num + list[i]*(10**i)
print(num)
