list=eval(input())
list.reverse
a=[str(x) for x in list]
for i in a:
    i+=i
print(i)
