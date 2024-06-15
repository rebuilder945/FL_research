n_str = input()
n_list = eval(n_str)
for x in n_list:
    if n_list.count(x)>1:
        n_list.remove(x)
print(n_list)
