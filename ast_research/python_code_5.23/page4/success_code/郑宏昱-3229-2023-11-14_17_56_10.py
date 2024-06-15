a = eval(input())        
b = []        
count_dict = {}      
for x in a:        
    count_dict[x] = count_dict.get(x, 0) + 1  # 记录每个元素的出现次数      
for x in a:      
    if count_dict[x] == 1:  # 只添加出现一次的元素到b中      
        b.append(x)      
b.sort()       
result = str(b).replace(" ", "").replace("[", "").replace("]", "")  
print(result) if result else print(False)


