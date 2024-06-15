a = input()
star = 0
list1=[]
list2=[]
list3=[]
list4=[]
if len(a)>=8:
    star=star+1
for x in a:
    if x.isdigit():
        list1.append(x)
    elif x.isalpha():
        list2.append(x)
        list3.append(x)
    elif x in '~!@#$%^&*()_=-/,.?<>;:[]{}|\\':
        list4.append(x)
c = [list1,list2,list3,list4]
for y in c:
    if y!=[]:
        star+=1
print(star)
