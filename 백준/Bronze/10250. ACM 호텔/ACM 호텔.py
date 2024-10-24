import math

T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    
    if N % H == 0:
        y = H
    else:
        y = N % H
    x = math.ceil(N / H)
    
    print(str(y) + format(x, '02'))