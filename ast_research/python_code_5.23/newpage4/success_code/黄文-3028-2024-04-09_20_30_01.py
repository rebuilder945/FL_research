n, m, l = eval(input())
result_list = [n]
for _ in range(m):
      a = n + l
      result_list.insert(0, a)
print(reversed(result_list))
       
