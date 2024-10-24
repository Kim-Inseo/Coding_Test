import sys

N = int(sys.stdin.readline().rstrip())

people_list = []
age_list = [[] for _ in range(201)]

for i in range(N):
    people_list.append(sys.stdin.readline().rstrip())

for person in people_list:
    age, name = person.split()
    age_list[int(age)].append(name)
    
for i in range(len(age_list)):
    if len(age_list[i]) == 0:
        continue
    for name in age_list[i]:
        print(i, name)