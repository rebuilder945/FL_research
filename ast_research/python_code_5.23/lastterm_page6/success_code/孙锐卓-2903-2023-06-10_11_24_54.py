def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
    e=[1]
    k=1
    n=x
    
    for i in range(n):
        k=(i+1)*k
           
        p=1/k
        e.append(p)
        
        
    print('%.6f'%(sum(e)))
main()


