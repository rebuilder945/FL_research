ls=eval(input())
for i in ls[::]:
    a=ls.count(i)
    if a>1:
        for b in range(a-1):
            ls.remove(i)
print(ls)

        
        


