arr = [0,1,-1,0,2,3,0]
zero_list = []
non_zero_list = []
for i in arr:
    if i==0:
        zero_list.append(0)
    else:
        non_zero_list.append(i)

print(non_zero_list + zero_list)
