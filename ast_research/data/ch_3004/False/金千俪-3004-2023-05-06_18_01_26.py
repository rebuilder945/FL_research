lst=eval(input())
for i in lst[:]:
    if i >=2 and type(i)==int:
        for x in range(2,int(i+1)):
            if i % x == 0:
                lst.remove(i)
                break
    else:
        lst.remove(i)
print(lst)
#int(i**0.5)+1
        

