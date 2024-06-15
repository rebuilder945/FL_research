ls1=eval(input())
ls1.sort(reverse=True)
ls2=[]
for x in ls1:
    y=str(x)
    ls2.append(y)
string=''.join(ls2)
a=int(string)
print(a)
