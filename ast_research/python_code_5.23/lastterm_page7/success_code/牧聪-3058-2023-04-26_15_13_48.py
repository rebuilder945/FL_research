strs={}
while True:  
    str = input()  
    if str == "q":  
        break  
    if str in strs:
        strs[str]=strs[str]+1
    else:
        strs[str]=1
print(strs)
    

