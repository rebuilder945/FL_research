list=eval(input())
list1=[]
def sushu(n):
    for n in list:
        if n>=2 and type(n)==int:
            for i in range(2,n//2+1):
                if n%i==0:
                    break
                else:
                    list1.append(x)
print(list1)
