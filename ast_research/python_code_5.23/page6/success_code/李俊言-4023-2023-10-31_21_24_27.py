def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    b=1
    while (total_count-(total_count//2))-2>0:
        total_count=(total_count-(total_count//2))-2
        b+=1
    print(b)

main()


