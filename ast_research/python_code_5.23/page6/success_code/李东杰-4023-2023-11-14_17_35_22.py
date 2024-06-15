def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    n=0
    while total_count>0:
        a=total_count//2+2
        total_count=total_count-a
        n+=1
   
        print(n)
main()


