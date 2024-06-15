def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=a
    c=0
    s=0
    if a<10:
        while c<a:
            s += b*a*10**c
            b -= 1
            c += 1
    else:
        while c<2*a:
            s += b*a*10**c
            b -= 1
            c += 2
    print(s)
main()

