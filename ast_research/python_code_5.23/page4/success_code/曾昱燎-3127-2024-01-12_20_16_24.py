n = int(input())  
lst = list(range(1, n+1))    
for i in range(len(lst)):  
    lst.append(lst.pop(0))    
print(lst)
