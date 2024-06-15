def main():
    total_count = int(input())
    calculate_days(total_count)
def days(a,d):
    if a>0:
        b=a//2+2
        c=a-b
        d+=1
        days(c,d)
    else:
        print()
def calculate_days(a):
    days(a,0)
            
main()


