s = input()
lst = []
for i in s:
    if "0"<= i <="9":
        lst.append(i)
if lst == []:
    print("No digits")
else:
    for i in s:
        if "0"<= i <="9":
            pass
        else:
            s =s.replace(i," ")
    lst1 = s.split()
    m = len(max(lst1,key=len))
    lst1.reverse()
    for i in lst1:
        if len(i) == m:
            print(i)
            break
    

