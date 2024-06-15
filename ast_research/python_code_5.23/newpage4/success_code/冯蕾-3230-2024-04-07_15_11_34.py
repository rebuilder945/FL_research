lst=eval(input())
lst.sort(reverse=True)
n='0'
for i in lst:
    n+=str(i)
print(int(n))

