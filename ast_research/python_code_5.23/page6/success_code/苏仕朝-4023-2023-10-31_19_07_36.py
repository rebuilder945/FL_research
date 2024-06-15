def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(x):
    days=0
    if x>2:
        x=x-int(x/2)-2
        days+=1
    print(days)
main()


