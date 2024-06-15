lst =eval(input())
lst.sort(reverse=True)
b = ''
for i in range(len(lst)):
    b+=str(lst[i])
print(int(b))
