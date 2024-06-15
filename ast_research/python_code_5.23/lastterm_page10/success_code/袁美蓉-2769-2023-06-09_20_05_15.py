a = input()
for i in range(len(a)):
    if a[i].isalpha():
        str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        str2 = 'abcdefghijklmnopqrstuvwxyz'
        for j in range(len(str1)):
            if a[i]==str1[j]:
                a[i]==str1[26-j+1]
        for k in range(len(str2)):
            if a[i]==str2[k]:
                a[i]==str2[26-k+1]
    elif a[i].isdigit():
        a[i]=a[i]
print(a)
print(a[i])      
