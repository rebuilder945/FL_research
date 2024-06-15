def translate(a):
    for i in range(len(a)):
        if a[i].isalpha():
            str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            str2 = 'abcdefghijklmnopqrstuvwxyz'
            for j in range(len(str1)):
                if a[i]==str1[j]:
                    return str1[26-j+1]
            for k in range(len(str2)):
                if a[i]==str2[k]:
                    return str2[26-k+1]
        elif a[i].isdigit():
            return a[i]
s = input()
print(s)
print(translate(s))  
