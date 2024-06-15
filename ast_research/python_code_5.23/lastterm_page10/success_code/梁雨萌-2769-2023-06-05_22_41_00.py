srr1 = "abcdefghijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ"
srr2 = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
dct = {x:y for x,y in zip(srr1,srr2)}
str = input()
print(str)
for i in range(len(str)):
    if str[i].isalpha():
        print(dct.get(str[i]),end='')
    else:
        print(str[i],end='')
