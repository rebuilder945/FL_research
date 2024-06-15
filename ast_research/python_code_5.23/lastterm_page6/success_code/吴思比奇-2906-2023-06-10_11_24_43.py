def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    i=0
    x=0
    while x<total_count:
        a=total_count//2+2
        x=x+a
        i=i+1
    print(i)
    
    
main()


