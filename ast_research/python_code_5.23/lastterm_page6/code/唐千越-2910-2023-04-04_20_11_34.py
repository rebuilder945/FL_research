def d():
    h,N=int(input())
    s(h,N)
def s(h,N):
    if N=1:
        s=h
    if N>1:
        while h > 0:
            g=h
            h *= 0.5
            s=g+2*h
        print(s)
d()
