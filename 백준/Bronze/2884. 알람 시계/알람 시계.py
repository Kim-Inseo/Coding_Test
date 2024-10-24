hour, minute = map(int, input().split())

minutes = hour * 60 + minute

if minutes < 45:
    minutes += (24 * 60 - 45)
else:
    minutes -= 45
    
new_h = minutes // 60
new_m = minutes % 60

print(new_h, new_m)