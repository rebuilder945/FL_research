n=input()
y=0
m=0
for i in range(100,int(n)):
    for x in str(i):
        y+=int(x)**3
    if y==i:
        print(i)
        m=1
if m==0:
    print("none")

