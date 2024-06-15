n=eval(input())
def F(n):
    if n<=2:
        return n
    return F(n-1)+F(n-2)
toge=0
for i in range(1,n+1):
    toge=F(i+1)/F(i)
print("%.4f"%toge)
