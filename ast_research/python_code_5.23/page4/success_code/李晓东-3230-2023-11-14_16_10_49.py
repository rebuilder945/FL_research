list1 = eval(input())
a = ""
list1.sort(reverse=True)
for i in list1:
    a = a+str(i)
b = int(a)
print(b)

