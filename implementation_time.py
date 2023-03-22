n = int(input())
5
count = 0
'''
    3이 포함?
    3, 13, 23, 33, 43, 53
    n % 10 = 3
'''


for i in range(n + 1):
    for j in range(60):
        for k in range(60):
           if '3' in str(i) + str(j) + str(k):
               count += 1
print(count)