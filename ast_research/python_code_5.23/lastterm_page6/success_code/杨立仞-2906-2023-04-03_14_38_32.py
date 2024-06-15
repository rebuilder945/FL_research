def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(m):
    i=0
    while m>0:
        m=m-(m//2)-2
        i+=1
    print(i)    
main()


