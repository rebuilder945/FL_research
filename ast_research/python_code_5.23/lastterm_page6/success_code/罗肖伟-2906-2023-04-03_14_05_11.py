def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(x):
    s=0
    while x>0:
        x=x*0.5-2
        s+=1
    print(s)
main()


