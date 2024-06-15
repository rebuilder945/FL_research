def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    for i in range(a):
        s=s+10**i*a*(a-i)
    print(s)
        
main()

