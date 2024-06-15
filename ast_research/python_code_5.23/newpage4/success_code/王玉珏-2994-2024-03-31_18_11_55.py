lst=(input().split(","))
numlst=input().split(",")
n=eval(numlst[0])
m=eval(numlst[1])
if n>len(lst) or n<-len(lst):
    print("error")
else:
    new_list1=[x for x in lst]
    del new_list1[n]
    new_list2=[lst[n]]
    new_list3=new_list1+new_list2*m
    new_list4=[]
    for num in new_list3:
        new_list4.append(int(num))

    print(new_list4)

