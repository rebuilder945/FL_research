def stu(i):
    if i>=2:
        for n in range(2,i):
            if i%n==0 :
                return False 
        else:
            return True
    else:
        return False
lst0=eval(input())
lst1=[]
for i in lst0:
    if stu(i):
        lst1.append(i)
print(lst1)
