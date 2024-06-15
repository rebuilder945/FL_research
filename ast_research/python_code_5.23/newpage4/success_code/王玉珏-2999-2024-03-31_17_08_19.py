lst_str=input().split(" ")
shu=(input().split(" "))
a=eval(shu[0]) 
b=eval(shu[1])
new_list=[]
new_list=[x for x in lst_str]
new_list[a]=lst_str[b]
new_list[b]=lst_str[a]
print(new_list)
