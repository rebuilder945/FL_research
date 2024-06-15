lst=eval(input())
lst.sort(reverse=True)

s=""
for i in lst:
    s+=str(i)
print(int(s))
