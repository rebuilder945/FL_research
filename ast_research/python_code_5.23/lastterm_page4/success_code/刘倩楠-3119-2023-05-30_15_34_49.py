nums=eval(input())
ls=[]
for x in nums[::-1]:
    if x not in ls:
        ls.append(x)
ls.reverse()
print(ls)
