num1=list(input())
def num2(num1):
    n=len(num1)
    for x in num1[1:n+1:1]:
        a=x+5
        b=int(a)
        x=b%10
    for i in rangm(n):
        num1[i]=num1[-i]
    num2=str(num1)
    print("num2")
num2(num1)
print(num1)
