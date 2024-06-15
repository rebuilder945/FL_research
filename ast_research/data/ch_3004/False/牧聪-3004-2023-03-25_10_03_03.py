lst = eval(input())
new_lst = [n for n in lst if n !=1 or all(n % i != 0 for i in range(2, int(n**0.5)+1))]
print(new_lst)

