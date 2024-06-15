t=eval(input())

for x in t:
    if x>3:
        pass
    else:
        for i in range(4,x):
            if x%i==0:
                t.remove(i)
                break
print(t)    

     
