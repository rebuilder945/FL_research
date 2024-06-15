srr1 = "abcdefghijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ"
srr2 = srr1[::-1]

dct = {x:y for x,y in zip(srr1,srr2)}
str = input()
print(str)
for i in range(len(str)):
    if str[i].isalpha():
        print(dct.get(str[i]),end='')
    else:
        print(str[i],end='')
