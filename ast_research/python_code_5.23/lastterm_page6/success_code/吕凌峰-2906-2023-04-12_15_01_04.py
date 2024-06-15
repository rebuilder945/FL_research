def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    while total_count>1:
        a=total_count/2+2
        b=total_count-a
        total_count=b
        day+=1
    print(day)
main()


