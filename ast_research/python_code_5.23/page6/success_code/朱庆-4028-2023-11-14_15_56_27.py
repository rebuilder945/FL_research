def sushu(x):
    return x !=1 and all(x%l !=0 for l in range(2,x))

def huiwenshu(x):
    return str(x)==str(x)[::-1]
def huiwensushu(x):
    return huiwenshu(x) and sushu(x)

n = input()
if type(n)!= int or int(n)<0:
    print("illegal input")
else:
    n = int(n)
    print(*filter(huiwensushu,range(1,n+1)))
   

