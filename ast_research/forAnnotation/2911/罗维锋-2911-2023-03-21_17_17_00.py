def password1(x):
    x=int(x)
    x+=5
    x%=10
def password2(i):
    for m in range(int(len(i)/2)):
        c=i[m]
        i[m]=i[-m-1]
        i[-m-1]=c
a=list(input())
map(password1,a)
map(password2,a)
b="".join(map(str,a))
print(b)
