ls1=eval(input())
ls1.reverse()
ls2=[]
for i in ls1:
    if i not in ls2 and type(i) is not bool:
        ls2.insert(0,i)
    elif i not in ls2 and type(i) is bool:
        ls2.insert(0,i)
ls2.pop( )
print(ls2)
