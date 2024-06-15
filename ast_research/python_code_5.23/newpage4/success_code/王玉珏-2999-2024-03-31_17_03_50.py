lst_str=input().split(" ")
shu=(input().split(" "))
a=eval(shu[0])
b=eval(shu[1])
lst_str[a]=lst_str[b]
lst_str[b]=lst_str[a]
print(lst_str)
