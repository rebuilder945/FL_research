list = eval(input())

max_num = max(list)
min_num = min(list)

while(1):
    if(list.count(max_num) != 0):
        list.remove(max_num)
    elif(list.count(min_num) != 0):
        list.remove(min_num)
    else: break

print(list)
