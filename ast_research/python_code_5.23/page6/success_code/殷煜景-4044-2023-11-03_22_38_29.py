n=input()
m=0
for i in range(100,int(n)+1):
    y=0
    for x in str(i):
        y=y+int(x)**3
    if y==i:
        print(i)
        m=1
if m==0:
    print("none")

