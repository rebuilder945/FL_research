lst=eval(input())
lst.sort(reverse=True)
num=""
for i in lst:
    num+=str(i)
print(int(num))

