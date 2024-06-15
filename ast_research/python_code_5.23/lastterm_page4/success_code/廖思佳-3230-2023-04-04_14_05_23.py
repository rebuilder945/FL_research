from audioop import reverse


list1=eval(input())
list2=list(list1)
list2.sort(reverse=True)
num=""
for i in range(len(list2)):
    num=num+str(list2[i])

k=int(num)
print(k) 
