def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
    I=0
    J=0
    K=a 
    while J<a:
        I+=K*a*10**J
        K-=1
        J+=1
        
    print(I)
main()

