M=input().split()
L=input().split()
S1,S2=eval(",".join(L))
import copy
MC=copy.deepcopy(M)
MC[S1]=M[S2]
MC[S2]=M[S1]
print(MC)
