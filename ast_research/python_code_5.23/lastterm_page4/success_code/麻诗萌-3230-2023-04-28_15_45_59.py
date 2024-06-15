lst=input()
lst0=list("".join(lst))
lst0.sort(reverse=True)
m=""
for i in lst0:
    m+=i
print(m)    
