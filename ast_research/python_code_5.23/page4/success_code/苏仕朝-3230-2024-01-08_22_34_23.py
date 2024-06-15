list1=eval(input())
list1.sort(reverse=True)
mi=len(list1)
eva=0
for x in list1:
    if mi >1:
        eva=eva+x*10**(mi-1)
        mi-=1
    elif mi==0:
        break
print(eva)
