def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(N):
    x=0
    while N>0:
        N=N/2-2
        x=x+1
    print(x)    
main()


