def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days():
        import math
        s=total_count
        i=0
        while s>0:
            s=s-(math.floor(s/2)+2)
            i+=1
        print(i)

main()


