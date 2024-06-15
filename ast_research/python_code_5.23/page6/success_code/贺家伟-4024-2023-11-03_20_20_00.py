def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    if a<10:
        s=0
        for i in range(0,a):
            s=a*10**i+s
        d=0
        for i in range(0,a):
            d=d+s//(10**i)
    else:
        b=str(a)
        b=a*a
        c=eval(b)
        d=0
        for i in range(0,a):
            d=d+c//(100**i)
    print(d)
    
main()

