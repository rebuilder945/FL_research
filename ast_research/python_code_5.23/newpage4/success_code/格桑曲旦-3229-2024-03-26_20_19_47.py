def find_unique_elements(lst):
    unique_elements=[x for x in set(lst) if lst.count(x)==1]
    return sorted(unique_elements)
lst=[1,2,3,3]
result=find_unique_elements(lst)
print(result)
