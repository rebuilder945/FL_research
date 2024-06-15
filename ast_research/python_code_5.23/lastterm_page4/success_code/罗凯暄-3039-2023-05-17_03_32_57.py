ist = eval(input())
n=max(ist)
m=min(ist)
indexn = [i for i in range(len(ist)) if ist[i] == n]
indexm = [i for i in range(len(ist)) if ist[i] == m]
newist = [ist[i] for i in range(len(ist)) if i not in indexn and i not in indexm]
print(newist)
