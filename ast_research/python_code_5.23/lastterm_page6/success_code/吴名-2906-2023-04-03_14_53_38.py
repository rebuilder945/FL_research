def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(q):
    i=0
    if q <=4:
        print("1")
    else:
        while q >=5:
            if q//2==0:
                q=q/2-2
                i+=1
            else:
                q=(q+1)/2-2
                i+=1
        if q<=4:
                print(i+1)
main()


