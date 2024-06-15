a=eval(input())
s=[]
for i in a:
        for j in range (2,i):
            if i%j==0:
                break
        else:
            s.append(i)



print(s)        


