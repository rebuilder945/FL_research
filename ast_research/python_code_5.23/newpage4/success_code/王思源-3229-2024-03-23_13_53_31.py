list = eval(input())

num_count = 0
num_sort = []
for i in range(len(list)):
    if(list.count(list[i]) == 1):
        num_count = num_count + 1
        num_sort.append(list[i])
        
num_sort.sort()

if num_count == 0: 
    print("False")
else:
    for i in range(len(num_sort)-1):
        print(num_sort[i], end=",")
    print(num_sort[-1])
