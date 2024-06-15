def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(x):
    last=0
    while x>0:
        x=x-(x/2+2)
        last+=1
    print(last)
main()


