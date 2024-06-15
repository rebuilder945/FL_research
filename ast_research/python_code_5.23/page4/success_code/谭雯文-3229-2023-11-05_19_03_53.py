n1=eval(input())
n1.sort()
i=0
while i <len(n1):
    if n1.count(n1[i])>=2:
        for x in range(n1.count(n1[i])):
            del n1[i]
    else:
        i+=1

if n1==[] :
    print("False")
else:
    print(",".join(str(i) for i in n1))

    


    

