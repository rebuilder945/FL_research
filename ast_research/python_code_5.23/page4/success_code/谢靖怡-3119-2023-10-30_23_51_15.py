ls1=eval(input())
ls1.reverse()
ls2=[]
for i in ls1:
    if i not in ls2:
        ls2.insert(0,i)
ls2.pop( )
print(ls2)
