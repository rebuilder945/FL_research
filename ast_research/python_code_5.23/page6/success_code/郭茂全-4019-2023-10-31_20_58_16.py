a=input()
new=''
m=0
new1=''
for x in a:
    b=int(x)
    c=str((b+5)%10)
    new+=c
for i in new:
    m-=1
    new1+=new[m]
print(new1)
