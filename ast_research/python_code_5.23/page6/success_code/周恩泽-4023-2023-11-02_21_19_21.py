def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
        a=[]
        while total_count>0:
            total_count=total_count-total_count//2-2
            a.append(total_count)
        b=a.index(0)
        print(b+1)
main()


