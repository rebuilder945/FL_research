a=eval(input())
b=eval(input())
c_list=a.split()
d_list=b.split()
values=[]
for x in c_list :
    for y in d_list :
        values.append(x+y)
        print(values)

