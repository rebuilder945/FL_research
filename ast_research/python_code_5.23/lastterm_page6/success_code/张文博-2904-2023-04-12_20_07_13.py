def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
    s=0
    for x in range(a):
        i=10**x
        s=s+(a-x)*i*a
    print(s)   
main()

