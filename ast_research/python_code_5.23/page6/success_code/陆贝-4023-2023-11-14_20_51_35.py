def main():
    total_count = int(input())
    calculate_days(total_count)
def  calculate_days(n):
    t=0
    while n>0:
        mai=n*0.5+2
        n=n-mai
        t=t+1
        print(t)
        
main()


