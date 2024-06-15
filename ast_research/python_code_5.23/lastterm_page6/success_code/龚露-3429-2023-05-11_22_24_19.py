ls = list(input())
str = ''.join(ls)
num1=[]
num2=[]
num3=[]
num4=[]
for i in range(0,len(ls)):
    if str[i]==" ":
        num2.append(i)
    elif ord('0')<=ord((str[i]))<=ord('9'):
        num3.append(i)
    elif ord("a")<=ord(str[i])<=ord("z") or ord("A")<=ord(str[i])<=ord("Z"):
        num1.append(i)
    else:
        num4.append(i)
e=len(num1)
f=len(num2)
g=len(num3)
h=len(num4)
print(e,f,g,h)
