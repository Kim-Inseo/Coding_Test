N = int(input())

for i in range(N):
    score = 0
    streak = 0
    result = input()
    
    for ox in result:
        if ox == 'O':
            streak += 1
            score += streak
        else:
            streak = 0
    
    print(score)