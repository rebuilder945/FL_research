lit=eval(input())
lit.sort(reverse=True)
s=''
for i in range(len(lit)):
    s+=str(lit[i])
print(s)


