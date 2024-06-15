def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    n=1
    m=a
    while n<=a:
        s+=m
        m+=a*10**n
        n+=1
    print(s)
main()

