def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
     s=0
    for x in range(1,n+1):
        t=1
        for y in range(1,x+1):
            t=t*y
        s+=1/t
    print('%.6f'%(s+1))
main()


