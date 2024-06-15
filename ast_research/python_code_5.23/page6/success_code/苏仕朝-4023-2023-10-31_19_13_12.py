def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(x):
    days=0
    if x>0:
        days+=1
        x=x-x//2-2
    print(days)
main()


