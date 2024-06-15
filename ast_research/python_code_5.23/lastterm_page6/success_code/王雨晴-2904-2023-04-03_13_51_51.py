def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=0
    c=0
    d=a
    while c<a:
        b=b+d*a*10**c
        c=c+1
        d=d-1
    print(b)
main()

