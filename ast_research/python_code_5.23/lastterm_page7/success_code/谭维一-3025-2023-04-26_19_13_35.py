s=input()
s=s.split("#")[0]
dict={'d':0,'l':0}
out=''
for i in s:
    if i.isdigit():
        dict['d']+=1
    elif i.isalpha():
        dict['l']+=1
        out += i
output=','.join([str(dict['d']), str(dict['l'])])
print(output)
print(out)
