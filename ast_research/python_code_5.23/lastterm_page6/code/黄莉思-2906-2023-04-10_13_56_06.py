def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(n):
    days=0
    while n>0:
         days+=1
         n=n-n//2-2
     print(days)
main()


