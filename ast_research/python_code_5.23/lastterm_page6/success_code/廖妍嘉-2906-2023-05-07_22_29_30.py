def main():
    total_count = int(input())
    calculate_days(total_count)
def  calculate_days(n):
    i = 0
    while n>0:
        n=n-n//2-2
        i +=1
        print(i)
main()


