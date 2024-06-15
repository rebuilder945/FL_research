def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    ls=[]
    s=0
    for i in range(a):
        s=s+a*10**i*(a-i)
    print(s)
    
main()

