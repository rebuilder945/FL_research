def sushu(n):  
    if n <2:
        return False
    if n==2:
        return True
    if n>2:
        for i in range(2,n):
            if n % i==0:
                
                return False
                
            if i==n-1 and n % i != 0 :
                return True


Lsushu=[]
list1=eval(input())
for x in  range(len(list1)):
    if sushu(list1[x])==True:
        Lsushu=Lsushu+[list1[x]]

print(Lsushu)


