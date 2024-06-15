a=list(input())
b=list(input())
if len(b)>=2:
    for i in range(len(b)):
        for i in b:
            c=a.count(i)
else:
    c=a.count(b[0])
for i in range(c):
    if len(b)>=2:
        for i in b:
            a.remove(i)
    else:
        a.remove(i)
print("".join(a))



    



        

       



                    




