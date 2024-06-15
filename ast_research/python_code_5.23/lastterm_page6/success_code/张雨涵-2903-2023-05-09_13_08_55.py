def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
        d = [1/i for i in range(1,num+1)]
        t=[]
        for a in range(num+1):
                s=1
                
                for x in d[:a]:
                      s*=x
                      t.append(s)
        e = sum(t)+1
        print("%.6f"%e)
main()


