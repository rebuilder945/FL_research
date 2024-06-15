def main():
    total_count = int(input())
    calculate_days(total_count)
def   calculate_days(total_count):
        n=total_count
        a=0
        while n >0:
                n=n-(int(n/2)+2)
                a=a+1
        print(a)
main()


