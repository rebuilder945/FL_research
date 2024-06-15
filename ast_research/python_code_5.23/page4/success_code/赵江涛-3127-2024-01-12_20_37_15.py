n = eval(input())
list = list(range(1,n+1))
a  =  list[0]
list.remove(a)
list.append(a)
print(list)
