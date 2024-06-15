n=input()
sums=0
def fibonacci(s):
    a=0
    b=1
    i=1
    while i<s:
        a,b=b,a+b
        i+=1
    return b
for i in range(2,int(n)+2):
    mid=(fibonacci(i+1))/(fibonacci(i))
    sums+=mid
print(sums)
