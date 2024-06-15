n1=eval(input())
i=0
while i<len(n1):
    if n1.count(n1[i])>=2:
        del n1[i]
    else:
        i+=1
print(n1)

        

