a=eval(input( ))
a.sort(reverse=True)
if a.count(0)==len(a):
    print("0")
if a.count(0)!=len(a):
    b=" ".join(str(x)for x in a)
    c=b.split()
    d="".join(c)
    print(d)
