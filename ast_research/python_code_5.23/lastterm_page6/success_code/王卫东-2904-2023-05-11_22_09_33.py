def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
    s=0
    for x in range(1,a+1):
        for y in range (0,x):
            if a>=10:
                s=s+a*(10**(2*y))
            else:    
                s=s+a*(10**y)
    print(s)
main()

