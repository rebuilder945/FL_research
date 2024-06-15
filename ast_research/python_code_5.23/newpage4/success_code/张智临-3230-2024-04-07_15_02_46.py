lst = eval(input())
lst.sort(reverse=ture)
sum = ''
for i in range(len(lst)):
  sum+=str(lst[i])
print(int(sum))
