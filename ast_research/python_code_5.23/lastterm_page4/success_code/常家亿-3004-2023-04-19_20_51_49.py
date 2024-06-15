def sushu(x):
    if x >= 2:
        for i in range(2,x):
            if x%i == 0:
               return False
            else:
               return True
    else :
       return False
a = input()
b = []
for x in a:
    if sushu(x):
        b.append(x)
    else:
        pass
print(b)

