def a1(n):
    w=n%2
    if w==1:
        t="red"
    else:
        t="black"
    return t
def a2(n):
    w=n%2
    if w==0:
        t="red"
    else:
        t="black"
    return t
n=int(input())
if n==0:
    print("green")
elif 0<n<=10 or 18<n<=18:
    t=a1(n)
    print(t)
elif 10<n<=18 or 28<n<=36:
    t=a2(n)
    print(t)
else:
    print("error")
