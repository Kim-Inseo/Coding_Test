import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    ps = sys.stdin.readline().rstrip()
    flag = True
    num = 0
    
    for parenthesis in ps:
        if parenthesis == '(':
            num += 1
        elif parenthesis == ')':
            num -= 1
            if num < 0:
                flag = False
                break
    
    if num != 0:
        flag = False
        
    if flag == True:
        print('YES')
    else:
        print('NO')
             