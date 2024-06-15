h=int(input())
n=int(input())
h1=0
for i in range(1,n+1):
    if i ==1:
        h1+=h
    if i >1:
        h1+=2*h
    h=h/2
print("%.2f"%h1)  

