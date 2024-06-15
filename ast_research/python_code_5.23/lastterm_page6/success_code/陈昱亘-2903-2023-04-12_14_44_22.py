def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    lst=[]
    m=1
    for i in range(n):
        m*=(i+1)
        n=1/m
        lst.append(n)
    e=1+sum(lst)
    print('%.6f'%(e))
main()


