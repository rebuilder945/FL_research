boy = eval(input())
girl = eval(input())
all = boy + girl
a = boy / all
b = girl / all
c = '{:.2%}'.format(a)
d = '{:.2%}'.format(b)
print("The male students ratio is",str(c)+",the female students ratio is",d)
