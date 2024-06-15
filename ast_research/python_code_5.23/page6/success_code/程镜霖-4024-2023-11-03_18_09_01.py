def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    n=0
    m=0
    s=a
    while m<a:
        n=s*a*10**s
        m+=1
        s-=1
    print(n)

main()

