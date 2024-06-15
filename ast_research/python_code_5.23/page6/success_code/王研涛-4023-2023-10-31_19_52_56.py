def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(x):
        i=0
        while x>0:
            x=x-(x/2+2)
            i=i+1
        print(i)
main()


