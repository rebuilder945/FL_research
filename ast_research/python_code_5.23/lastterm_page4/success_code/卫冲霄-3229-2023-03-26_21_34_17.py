ls=eval(input())
ls1=[]
def matrix(ls):
    result={}
    for z in ls:
        result[z]=ls.count(z)
    return result
if min(matrix(ls))==1:
    for i in range(0,len(ls)):
        if ls.count(ls[i])==1:
            ls1.append(ls[i])
    ls1.sort()
    print(*ls1,sep=",")
else:
    print("False")




