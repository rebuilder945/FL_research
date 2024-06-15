def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(a):
    i=1
    lst=[]
    while i<=a:
        j=1
        b=1
        while j<=i:
            k=1/j
            b*=k
            j+=1
        lst.append(b)
        i+=1
    e=sum(lst)+1
    print('%.6f'%e)
main()


