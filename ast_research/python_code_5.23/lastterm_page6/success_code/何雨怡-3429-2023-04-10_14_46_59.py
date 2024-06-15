n=str(input())
long=len(n)
english=0
empty=0
number=0
other=0
for i in range(long):
    num=ord(n[i])
    if 65<=num<=90:
        english+=1
    elif 97<=num<=121:
        english+=1
    elif num==0:
        empty+=1
    elif 1<=num<=47 or 58<=num<=64 or 91<=num<=96 or 123<=num<=127:
        other+=1
    elif 48<=num<=57:
        number+=1
print(english,empty,number,other)

