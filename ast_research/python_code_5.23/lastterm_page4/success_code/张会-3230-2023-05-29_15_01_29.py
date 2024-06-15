s=eval(input())
s.sort(reverse=True)
ls=[str(i) for i in s]
s1=''.join(ls)
print(int(s1))
