def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(a):
    i=0
    if a>0:
        a=a/2-2
        i+=1
    else:
        print(i)
main()


