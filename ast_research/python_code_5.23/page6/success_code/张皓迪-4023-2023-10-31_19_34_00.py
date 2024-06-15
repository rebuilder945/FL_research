def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(a):
    a=a-(a/2)-2
    a=int(a)
    i=1
    if a>0:
        a=a/2-2
        i+=1
    else:
        print(i)
main()


