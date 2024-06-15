def sushu (x):
    for i in range (2, x //2+1):      
        if x % i ==0:
            return False 
    return True 
n = eval (input ())
sun = []
for x in n:
    if x <2 :
        None
    else:
        if sushu ( x ):
            sun.append(x)
print(sun)

