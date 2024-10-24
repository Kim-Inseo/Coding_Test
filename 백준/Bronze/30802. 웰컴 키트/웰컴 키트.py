import sys
import math

N = int(sys.stdin.readline().rstrip())
shirts = list(map(int, sys.stdin.readline().rstrip().split()))
T, P = map(int, sys.stdin.readline().rstrip().split())

shirt_num = []

for shirt in shirts:
    shirt_num.append(math.ceil(shirt / T))
    
print(sum(shirt_num))
print(N // P, N % P)