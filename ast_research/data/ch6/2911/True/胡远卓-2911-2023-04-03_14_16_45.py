num=eval(input())
x=""
while num>0:
    x+=chr(ord('0')+(num%10+5)%10)
    num//=10
print(x)
