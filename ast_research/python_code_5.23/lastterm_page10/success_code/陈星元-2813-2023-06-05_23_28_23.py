def delete(str,a):
    while a in str:
        i=str.find(a)
        str=str[:i]+str[i+len(a):]
    return str
str=input()
a=input()
s=delete(str,a)
print(s)
