def sushu(x):#定义素数，以便筛选
    if x ==2 or x == 3:
        return 1
    for i in range(2,x//2+1):
        if x%i==0:
            return 0
        return 1
a = eval(input())
b =[]
for i in a :
    if sushu(i) ==1:
        b.append(i)
print(b)

