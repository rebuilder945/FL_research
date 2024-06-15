list1 = input()
s = {}
for i in range(list1):
    for x in range(i):
        if x not in s:
            s[x]=1
        else:
            s[x]+=1
print(s)

