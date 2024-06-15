def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    i=0
    x=0
    a=total_count
    while x<=total_count:
        a=a//2+2
        x=x+a
        i=i+1
    print(i)
    
    
main()


