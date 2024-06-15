def remove_duplicates(lst):  
    return list(dict.fromkeys(lst))    
lst = input()
lst = remove_duplicates(lst) 
print(lst)
