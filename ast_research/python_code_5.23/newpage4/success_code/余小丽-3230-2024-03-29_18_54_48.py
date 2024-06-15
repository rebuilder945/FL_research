lst=eval(input())
lst.sort(reverse=True)
print(lst)
num=""
for i in lst:
    num+=str(i)
print(int(num))

