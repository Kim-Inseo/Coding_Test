T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    
    new_S = ''
    
    for letter in S:
        new_S += letter * R
        
    print(new_S)
    