def main():
    total_count = int(input())
    calculate_days(total_count)
def caculate_days(total_count):
    N = len(total_count)
    i = 0
    if N>0:
        N = N-(N/2+2)
        i = i+1
        return N 
    print(i)
main()


