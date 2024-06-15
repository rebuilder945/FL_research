str_list = eval(input())  
count_dict = {}  
for string in str_list:  
    for char in string:  
        if char in count_dict: 
            count_dict[char] += 1  
        else:
            count_dict[char] = 1  
for key, value in count_dict.items(): 
    print(key + ',' + str(value)) 
