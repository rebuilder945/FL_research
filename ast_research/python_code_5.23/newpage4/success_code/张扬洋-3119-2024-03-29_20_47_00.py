lst = eval(input())
count=[]
lst_count=lst_num=len(lst)
while(lst_count>0):
    if(lst[lst_count-1] not in count):
        count.append(lst[lst_count-1])
    lst_count-=1
count.reverse()
print(count)
