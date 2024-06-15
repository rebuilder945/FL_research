ls=eval(input())
for i in ls:
    if ls.count(i)>1:
        while i in ls:
            ls.remove(i)
if ls==[]:
    print("False")
else:
    ls=','.join(str(i) for i in ls)
    print(ls)
