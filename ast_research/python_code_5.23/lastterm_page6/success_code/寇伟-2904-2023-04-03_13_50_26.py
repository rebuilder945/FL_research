def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    a=str(a)
    total=0
    for i in range(1,int(a)+1):
        a=''+a*i
        total+=int(a)
    print(total)
main()

