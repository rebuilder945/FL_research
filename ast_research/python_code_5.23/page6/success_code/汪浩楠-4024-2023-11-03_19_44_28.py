def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    n=0
    m=1
    while n<=a:
        s+=a*m*10**n
        n+=1
        m+=1
    print(s)
main()

