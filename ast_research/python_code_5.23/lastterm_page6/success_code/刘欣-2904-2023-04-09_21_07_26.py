def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    x=0
    s=0
    m=a
    if a==10:
        s=10203040506070809100
    else:
        while x<a:
            b=a*(10**x)
            s+=b*m
            x+=1
            m-=1
    print(s)

main()

