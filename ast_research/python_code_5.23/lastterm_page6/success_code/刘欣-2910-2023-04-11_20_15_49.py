gaodu=int(input())
cishu=int(input())
juli=gaodu
for i in range(cishu-1):
    gaodu=gaodu/2
    juli+=gaodu*2
print("%.2f"%juli)
