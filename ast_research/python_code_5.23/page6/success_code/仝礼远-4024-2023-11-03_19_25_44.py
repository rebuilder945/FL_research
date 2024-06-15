def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    n=0
    s=0
    for i in range(a):
        n=n+1
        s=a*(a+1-n)*10^(n-1)+s
    print(s)
        
        
main()

