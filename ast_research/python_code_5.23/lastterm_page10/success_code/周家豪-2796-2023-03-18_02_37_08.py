dummy=input()
string=''
lst=[]
for i in dummy:
    if i.isdigit():
        string+=i
    else:
        if string!='':
            lst.append(string)
        string=''
if string!='':
    lst.append(string)

if lst!=[]:
    maximum=max(len(x) for x in lst)                     
    lstreversed=lst[::-1]
    for x in lstreversed:
        if len(x)==maximum:
            print(x)
            break
else:
    print("No digits")
