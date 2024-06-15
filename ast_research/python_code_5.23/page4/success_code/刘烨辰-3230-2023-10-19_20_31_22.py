list1 = eval(input())
list1.sort(reverse=True)
b = 1
a = str(b)
for i in range(0,len(list1)):
    a = a + str(list1[i])
print(int(a[1:]))
