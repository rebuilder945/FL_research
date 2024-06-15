def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
    s=0
    m=0
    n=x
    while m<x:
        s+=n*x*10**m
        m+=1
        n-=1
    print(s)
main()

