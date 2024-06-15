def main():
    total_count = int(input())
    calculate_days(total_count)
def  calculate_days(a):
    i=0
    while a>=0:
        i+=1
        a=a-(a//2+2)
    print(i)
main()


