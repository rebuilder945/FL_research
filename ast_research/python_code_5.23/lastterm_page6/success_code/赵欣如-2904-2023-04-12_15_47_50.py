def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
        b=0
        for i in range (1,a+1):
                b+=int(str(a)*i)
        print(b)
main()

