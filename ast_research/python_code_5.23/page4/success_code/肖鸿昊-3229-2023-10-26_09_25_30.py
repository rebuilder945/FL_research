a=eval(input())
b=[]
for i in a: 
    c=a.count(i)
    if c==1:
        b.append(i)
if b==[]:
    print("False")
else:
    b_s=str(b)
    print(b_s)
