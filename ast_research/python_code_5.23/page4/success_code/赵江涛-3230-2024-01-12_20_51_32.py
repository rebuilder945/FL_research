list = eval(input())
list.sort(reversed=True)
sum = ''
for x in list:
    sum = sum + str(x)
s = int(sum)
print(s)
