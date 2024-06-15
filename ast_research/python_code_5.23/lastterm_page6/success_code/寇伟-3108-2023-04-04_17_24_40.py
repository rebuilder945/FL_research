ls = eval(input())
def output(ls):
    x=''
    z=''
    for i in ls:
        x+=i
    y=''
    y=x[:]
    y_set=set(y)
    y_list=list(y_set)
    y_list.sort()
    dic={}
    for i in y_list:
        z=z+i+','+str(x.count(i))
        print(z)
output(ls)

