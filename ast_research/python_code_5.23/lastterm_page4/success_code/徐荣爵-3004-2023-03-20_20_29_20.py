lst = eval(input())
for x in lst:
    if x > 2:
        for i in range(2,x):
            if x%i == 0:
                lst.pop(0)
                break
            else:
                pass
    elif x < 2:
        lst.pop(0)
    else:
        pass
print(lst)
        
