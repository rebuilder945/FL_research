list_1 =list(eval(input()))
list_2 =[]
for i in list_1:
    if list_1.count(i) ==1:
        list_2.append(i)
if len(list_2)==0:
    print("False")
else:
    list_2.sort()
    for i in list_2[:-1]:
        print(i,end=",")
    print(list_2[-1])
    
