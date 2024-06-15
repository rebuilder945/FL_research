import math
def sushu(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
list1 = eval(input())
list2 = []
for i in list1:
    if sushu(i) and i != 1:
        list2.append(i)    
print(list2)        



