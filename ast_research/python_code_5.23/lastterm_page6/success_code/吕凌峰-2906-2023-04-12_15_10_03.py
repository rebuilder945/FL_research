def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    d=0
    while total_count>=1:
        a=total_count/2+2
        b=total_count-a
        total_count=b
        d+=1
    print(d)
main()


