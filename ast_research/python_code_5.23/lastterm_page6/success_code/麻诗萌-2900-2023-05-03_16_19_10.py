def stu(x):
    for y in range(2,x):
       if x%y==0 :
           return False
    else:
        return  True
def stu0(i):
    lst0=list(i)
    lst1=list(i)
    lst0.reverse()
    if lst0==lst1:
        return True
n=eval(input())
lst2=[]
while  n>0 and isinstance(n,int) :
    for i in range(n):
        if stu(i):
            if stu0(i):
                lst2.append(str(i))
    print(" ".join(lst2))
print("illegal input")

