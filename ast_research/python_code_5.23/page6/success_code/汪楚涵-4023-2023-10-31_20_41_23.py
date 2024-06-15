def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    left=int((total_count/2)-2)
    i=0
    s=0
    while i<left:
        i=(i+2)*2
        s=s+2
    print(s)
main()


