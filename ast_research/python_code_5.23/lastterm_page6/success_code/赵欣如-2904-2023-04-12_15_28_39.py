def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
        c=0
        for i in range (a+1):
                b=0
                d=i-1
                while d>=0:
                        b+=10**d
                        d=d-1
                c+=a*b
print(c)
main()

