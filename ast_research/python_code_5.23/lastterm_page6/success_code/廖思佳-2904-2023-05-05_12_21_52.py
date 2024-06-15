def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    n=0
    m=a
    for n in range(a):
        s+=m*a*10**n
        m-=1
    print(s)
main()

