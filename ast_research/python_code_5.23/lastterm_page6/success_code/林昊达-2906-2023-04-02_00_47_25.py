def main():
    total_count = int(input())
    calculate_days(total_count)
def  calculate_days(total_count):
        days = 0
        while total_count > 0:
                a="%d" %(total_count/2)
                total_count=int(a)-2
                days += 1
        print(days)
main()


