ls1=eval(input())
ls2=[]
for x in ls1[::-1]:#
    if x not in ls2:
        ls2.append(x)  #
ls2.reverse()#
print(ls2)
