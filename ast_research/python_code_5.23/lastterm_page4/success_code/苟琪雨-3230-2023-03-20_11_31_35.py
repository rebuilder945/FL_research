list_1=eval(input())
list_1.sort(reverse=True)
list_3=[str(i) for i in list_1]
result=int("".join(list_3))
print(result)

