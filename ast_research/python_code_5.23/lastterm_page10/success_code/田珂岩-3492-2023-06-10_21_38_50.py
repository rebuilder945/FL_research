s = input()
ls = list(s)
lst = []
for i in ls:
    if ls.count(i) == 1:
        lst.append(i)
if lst != []:        
    print(lst[0])        
else:
    print("None")    
