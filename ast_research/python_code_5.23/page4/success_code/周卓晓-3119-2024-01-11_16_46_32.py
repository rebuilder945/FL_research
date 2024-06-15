ls=eval(input())
lst=[]
for x in ls[::-1]:
    if x not in lst:
        lst.append(x)
print(lst[::-1])



