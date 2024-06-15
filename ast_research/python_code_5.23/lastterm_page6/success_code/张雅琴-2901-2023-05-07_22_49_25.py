a=0
b=0
c=0
num="1"
while num!="#":
    num=input()
    if num!="#":
        a=eval(num)
    b+=1
    c+=a
print("{}{}".format(b,c))
