def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(a):
        n=0
        while a>=0:
            if a%2==0:
                a-=(a%2+2)
                n+=1
            else:
                a-=(a//2+2)
                n+=1
        print(n)           
main()


