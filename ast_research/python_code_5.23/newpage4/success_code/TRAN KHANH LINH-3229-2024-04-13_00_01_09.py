num_list = eval(input())
num_one=[]
for num in num_list:
    if (num_list.count(num)==1):
        num_one.append(num)
num_one.sort()
if(len(num_one)==0):
    print("False")
else:
    for i in range(0,len(num_one)):
        if(i==len(num_one)-1):
            print(num_one[i])
        else:
            print(str(num_one[i])+",",end="")
