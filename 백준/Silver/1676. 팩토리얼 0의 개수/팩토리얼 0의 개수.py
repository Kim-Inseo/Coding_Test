import sys

N = int(sys.stdin.readline().rstrip())
answer = 0

while True:
    tmp = N // 5
    
    if tmp == 0:
        break
    else:
        answer += tmp
        N //= 5
        
print(answer)