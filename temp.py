import math

M, N = map(int,(input().split()))
num=[]

def is_psn(x):
    R = math.sqrt(x)
    if (R % 1) == 0:
        num.append(x)

for i in range(M,N+1):
    is_psn(i)
    
if num == []:
    print(-1)
else:
    print(f"{sum(num)}\n{min(num)}")