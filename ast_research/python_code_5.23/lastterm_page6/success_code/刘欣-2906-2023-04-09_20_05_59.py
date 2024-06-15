def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(a):
    day=0
    while a>0:
        maichu=(a//2)+2
        shengyu=a-maichu
        day+=1
    print(day)
main()


