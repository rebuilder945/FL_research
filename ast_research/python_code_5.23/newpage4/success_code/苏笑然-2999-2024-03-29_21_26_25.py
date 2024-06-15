a=input()
list=a.split( )
input_str = input()
input_list = input_str.split()
n = int(input_list[0])
m = int(input_list[1])
if n>m:
    list.insert(m,list[n])
    list.insert(n+1,list[m+1])
    del list[m+1]
    del list[n+1]
else:
    list.insert(n,list[m])
    list.insert(m+1,list[n+1])
    del list[n+1]
    del list[m+1]
print(list)
