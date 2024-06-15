str1 = input()
a = 0
b =0
c =0
d =0
for i in str1[0:len(str1)]:
    if 0<=ord(i)<=127:
        if i ==' ':
            b += 1
        elif ord('A')<=ord(i) <=ord('z') or 1<=ord(i)<=32:#ord()中数据类型为字符串
            a += 1
        elif ord('0') <=ord(i)<=ord('9'):
            c += 1
        else:
            d +=1
    else:
        False 
print(a,b,c,d)

