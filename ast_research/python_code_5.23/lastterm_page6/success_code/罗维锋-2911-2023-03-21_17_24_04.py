def password1(x):
    x=int(x)
    x=x+5
    x=x%10
def password2(i):
    for m in range(int(len(i)/2)):
        c=i[m]
        i[m]=i[-m-1]
        i[-m-1]=c
a=list(input())
map(password1,a)
b="".join(map(str,a))
print(b)
