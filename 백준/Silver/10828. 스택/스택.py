from collections import deque
import sys

queue = deque()

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    order = sys.stdin.readline().rstrip()
    
    if order[:2] == 'pu':
        push, num = order.split()
        queue.append(num)
    elif order == 'pop':
        try:
            num = queue.pop()
            print(num)
        except:
            print(-1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order == 'top':
        try:
            num = queue[-1]
            print(num)
        except:
            print(-1)