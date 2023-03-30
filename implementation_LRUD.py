n = int(input())
a, b = 1, 1
plans = input().split()

# (i , j)
di = [0, 0, -1, 1] # left side
dj = [-1, 1, 0, 0] # right side

move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    # plan은 이동계획
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = a + di[i]
            ny = b + dj[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x, y = nx, ny

print(x, y)