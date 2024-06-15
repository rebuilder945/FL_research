def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    stringa=str(a)
    for i in range(1,a+1):
        numberstr=stringa*i
        final=int(numberstr)
        s=s+final
    print(s)
main()

