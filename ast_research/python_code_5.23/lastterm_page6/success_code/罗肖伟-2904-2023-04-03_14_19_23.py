def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=a
    for i in range(a-1):
        a1=str(a)
        a2=a1+"a"
        a3=int(a2)
        s+=a3
    print(s)    
main()

