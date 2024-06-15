def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    t=total_count
    b=0
    while t>1:
        t=t/2-2
        b+=1
    print(b)
main()


