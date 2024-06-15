lst = eval(input())
for x in lst[:]:
    for x in lst[:]:
        if x > 2:
            for i in range(2,x):
                if x%i == 0:
                    lst.remove(x)
                    break
                else:
                    pass
        elif x < 2:
            lst.remove(x)
        else:
            pass
print(lst)
 
