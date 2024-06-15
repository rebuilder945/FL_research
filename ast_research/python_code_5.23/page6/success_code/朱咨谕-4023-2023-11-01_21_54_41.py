def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(t):
        a=0
        while(t!=0):
            t=t-int(t/2)
            t-=2
            a+=1
        print(a)
main()


