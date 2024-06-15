def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    start=1
    jiecheng=1
    for i in range(1,num+1):
        jiecheng=jiecheng*i
        daoshu=1/jiecheng
        start=start+daoshu
    print("%.6f"%(start))
main()


