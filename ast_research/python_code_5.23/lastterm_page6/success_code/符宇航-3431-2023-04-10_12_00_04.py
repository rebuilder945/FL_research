n = eval(input())
if n<=10:
    if n%2==0:
        cl="black"
    else:
        cl='red'
if n>10 and n<=18:
    if n%2==0:
        cl="red"
    else:
        cl='black'
if n>18 and n<=28:
    if n%2==0:
        cl="black"
    else:
        cl='red'
if n>28 and n<=36:
    if n%2==0:
        cl="red"
    else:
        cl='black'
if n == 0:
    cl = 'green'
print(cl)

