list = eval(input())
list.sort(reverse=True)
sum = ''
for x in list:
    sum = sum + str(x)
s = int(sum)
print(s)
