def remove_all(list, value):
    return[x for x in list if x != value ]
lst=eval(input())
a= max(lst)

b= min(lst)
result = remove_all(lst, a)
result = remove_all(result, b)
print(result)
