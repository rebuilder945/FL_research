list1=eval(input())
list1=list(list1)
a=max(list1)
b=min(list1)
m1=0
m2=0
for x in list1:
    if x==a or x==b:
        list1[m2]='#'
        m1+=1
    m2+=1
while m1>0:
    list1.remove('#')
    m1-=1
print(list1)

