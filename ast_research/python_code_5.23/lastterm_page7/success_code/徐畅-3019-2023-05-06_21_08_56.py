name,english,python,math=map(str,input().split((" ")))
english=('%.2f'%float(english))
python=('%.2f'%float(python))
math=('%.2f'%float(math))
avg=(eval(english)+eval(python)+eval(math))/3
stu=dict(name=name,python=python,english=english,math=math,avg=avg)

s=[float(english),eval(math),eval(python)]
s.sort(reverse=True)
b=[name]+s+[avg]
print(*b,sep=' ')
