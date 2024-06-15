def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    s=1 n=1
    for i in range(1,1+num):
        for a in range(1,1+i):
            n=n*a
        s=s+1/n
    print(s)
        
        
main()


