def translate(a):
    for i in range(len(a)):
        if a[i].isalpha():
            str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            str2 = 'abcdefghijklmnopqrstuvwxyz'
            for j in range(len(str1)):
                if a[i]==str1[j]:
                    result = str1[25-j]
                    return result
            for k in range(len(str2)):
                if a[i]==str2[k]:
                    result = str2[25-k]
                    return result
        elif a[i].isdigit():
            return a[i]
s = input()
print(s)
print(translate(s))  
