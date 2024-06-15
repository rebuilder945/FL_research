list1=eval(input())
list2=list1.reverse()
numbers=[]
for i in list2:
    if i not in numbers:
        numbers.append(i)
listul=numbers.reverse()
print(listul)
