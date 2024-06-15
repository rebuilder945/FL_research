def find_unique_elements(lst):
    count_dict={}
    for i in lst:
        if i in count_dict:
             count_dict[i]+=1
        else:
            count_dict[i]=1
    unique_elements=[k for k,v in count_dict.items()if v==1]
    if not unique_elements:
        return False
    unique_elements.sort()
    return unique_elements
lst=[1,2,3,3,4,1,2,5]
result=find_unique_elements(lst)
print(result)

    

            
        

