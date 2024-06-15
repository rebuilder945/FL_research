def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=a
    s=0
    le=len(str(a))
    for x in range(b):
        s+=a
        a=a*(10**le)+b       
    print(s)
main()

