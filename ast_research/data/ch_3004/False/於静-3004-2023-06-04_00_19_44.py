#定义一个函数寻找素数
def sushu(n):
    if n>=2:
        for i in range(2,n):
            if n%i != 0:
                return True
        else:
                return False
    else:
        return False
a=eval(input())
lst=[]
for i in a:
    if sushu(i):
        lst.append(i)
print(lst)

