a=input()
b=[]
for i in range (len(a)):
    b.append((int(a[i])+5)%10) 
b.reverse()       
print("".join(str(x) for x in b))
