def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    N=total_count
    D=0
    while N>0:
        if N%2==0:
            N=(N/2)-2
            D+=1
        elif N%2==1:
            N=(N+1/2)-2
            D+=1
print(D)

main()


