n = int(input())  
lst = list(range(1, n+1))     
lst.append(lst.pop(0))    
print(lst)
