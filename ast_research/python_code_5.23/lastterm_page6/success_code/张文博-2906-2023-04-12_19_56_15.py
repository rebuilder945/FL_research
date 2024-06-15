def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(i):
    j=0
    for x in range(100):
        if i<0 or i==0:
            break
        i=i/2-2
        j+=1
main()


