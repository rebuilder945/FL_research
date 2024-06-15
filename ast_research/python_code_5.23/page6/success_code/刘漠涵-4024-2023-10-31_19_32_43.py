def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    i=1
    lst=[]
    while i<=a:
        j=0
        k=1
        while k<=i:
            b=a*(10**(k-1))
            k+=1
            j+=b
        i+=1
        lst.append(j)
    print(sum(lst))
main()

