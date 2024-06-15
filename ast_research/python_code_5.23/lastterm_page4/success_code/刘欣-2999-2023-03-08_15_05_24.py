str_list=input().split(' ')
n,m=map(int,input.split(' '))
_=str_list[n]
str_list[n]=str_list[m]
str_list[m]=_
print(str_list)
