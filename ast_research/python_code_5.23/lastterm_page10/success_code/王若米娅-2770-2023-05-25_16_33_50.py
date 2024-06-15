ls1=list(x for x in input())
ls2=list(x for x in input())
def switch(ls1,ls2):
    ls3=[]
    if len(ls2)!=len(ls1):
        return "False"
    else:
        for i in ls1:
            if i not in ls2:
                return "False"
        for i in ls2:
            if i not in ls1:
                return "False"
        return "True"
print(switch(ls1,ls2))
