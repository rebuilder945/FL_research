ls1=eval(input())
ls1.reserve()
ls2=[]
for i in ls1:
    if i not in ls2:
        ls2.append(i)
ls2.reserve(i)
print(ls2)
