n=eval(input())
s=n
max_num=max(n)
min_num=min(n)
for num in n:
    if num==max_num or num==min_num:
        s.remove(num)
print(s)

