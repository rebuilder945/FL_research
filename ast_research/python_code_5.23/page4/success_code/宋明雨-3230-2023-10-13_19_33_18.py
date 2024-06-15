List = eval(input())
List.sort(reverse=True)
a = 1
Max= 0
for i in List:
    Nums = i * (10**(len(List)-a))
    a += 1
    Max += Nums 
print(Max)
