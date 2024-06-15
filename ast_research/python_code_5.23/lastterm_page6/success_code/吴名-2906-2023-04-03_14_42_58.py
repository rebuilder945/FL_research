def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(q):
    i=0
    while q >=4:
        q=q/2-2
        i+=1
        if q<=3:
            print(i+1)
main()


