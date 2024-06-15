a=input()
list1=[]
for i in a:         
    for x in range(2,i):
        if i%x==0:
            break
        list1.append(i)
        print(list1)
        break

