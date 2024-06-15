def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(b):
        c=0
        s=str(b)
        for i in range(1,b+1):
                c+=int(s*i)
        print(c)
main()

