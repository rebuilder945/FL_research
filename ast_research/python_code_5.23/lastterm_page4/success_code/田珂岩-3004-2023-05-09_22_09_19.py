import math
def sushu(n):
    if n >= 2 and type(n) == int:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    else:
        return False
list1 = eval(input())
list2 = []
for i in list1:
    if sushu(i):
        list2.append(i)    
print(list2)
