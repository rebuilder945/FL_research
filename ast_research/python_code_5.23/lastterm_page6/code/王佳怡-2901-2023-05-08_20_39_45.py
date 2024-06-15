a=input()
if a!=#:
    a=int(a)
    l=[]
    l.append(a)
    a=eval(input())
print(len(l),end=" ")
print(sum(l))
