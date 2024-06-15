def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(a):
    b=[]
    i=0
    while a>0:
        a=a/2-2
        i+=1
        b.append(i)
    print(int(b[-1]))
main()


