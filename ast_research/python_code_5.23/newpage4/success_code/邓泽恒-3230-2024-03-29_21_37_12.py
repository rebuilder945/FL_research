def k(x):
    if x <= 1:
        return False  
    for i in range(1, x):
        if x % i == 0:
            return False 
        else:
            return True 
num=eval(input())
b=[]
for x in num:
    if k(x):
        b.append(x)
print(b)
