def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    s=total_count
    i=0
    while s>0:
        s=s-(int(s/2)+2)
        i=i+1
    print(i)
main()


