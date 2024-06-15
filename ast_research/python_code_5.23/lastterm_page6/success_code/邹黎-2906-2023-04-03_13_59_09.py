def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    c=0        
    while total_count>0:
        a=int(total_count/2)
        total_count=total_count-a-2
        
        c=c+1
    print(c)
main()


