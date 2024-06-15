lst=list(eval(input()))
zuida=max(lst)
zuixiao=min(lst)
lst0=[]
for x in lst:
    if x !=zuida and x !=zuixiao:
        lst0.append(x)
        

print(lst0)
    
