ls=eval(input())
ls1=[]
def matrix(ls):
    result={}
    for i in ls:
        result[i]=ls.count(i)
    return result
if min(matrix(ls))==1:
    for i in range(0,len(ls)):
        if ls.count(ls[i])==1:
            ls1.append(ls[i])
    ls1.sort()
    for s in ls1:
        print(s,end=",")
else:
    print("False")




