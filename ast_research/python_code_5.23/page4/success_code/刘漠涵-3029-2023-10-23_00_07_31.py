students=input().split(',')
scores=eval(input())
list1=[]
for n in range(len(students)):
        list2=[students[n],scores[n]]
        list1.append(list2)
print(list1)


