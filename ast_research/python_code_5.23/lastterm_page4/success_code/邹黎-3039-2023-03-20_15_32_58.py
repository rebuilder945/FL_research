lst=list(eval(input()))
zuida=max(lst)
zuixiao=min(lst)
for x in lst:
    if x==zuida or x==zuixiao:
        lst.remove(x)
print(lst)
    
