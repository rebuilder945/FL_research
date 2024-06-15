def sushu(n):
    count = 0
    if n == 1:
        return True
    for i in range(2,n):
        if n % i == 0:
            count = count + 1
    if count != 0:
        return False
    else:
        return True
 
 
 
a = input()
 
b = []
 
a = a.split(',')
 
for i in a:
    if(sushu(eval(i))):
        b.append(eval(i))
 
print(b)

