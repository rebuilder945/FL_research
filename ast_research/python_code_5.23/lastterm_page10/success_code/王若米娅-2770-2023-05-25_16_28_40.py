ls1=list(x for x in input())
ls2=list(x for x in input())
def switch(ls1,ls2):
    ls3=[]
    if len(ls2)!=len(ls1):
        return "False"
    else:
        for i in ls1:
            if i in ls2:
                ls3.append(i)
        for j in ls2:
            if j not in ls3:
                return "False"
            else:
                return "True"
print(switch(ls1,ls2))
