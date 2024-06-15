def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(n):
        i=0
        while n>=0:
            i = i+1
            n = n//2-2
        print (i)
main()


