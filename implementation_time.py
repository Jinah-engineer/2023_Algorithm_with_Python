n = int(input())
5
count = 0
'''
    3이 포함?
    3, 13, 23, 33, 43, 53
    n % 10 = 3
'''

h = 0
m = 0
s = 0

for i in range(n):
    if i % 10 == 3:
        h += 1
    for j in range(60):
        if j % 10 == 3:
            m += 1
        for k in range(60):
            if k % 10 == 3:
                s += 1      
count = h * m * s
print(count)