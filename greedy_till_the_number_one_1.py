# 내가 푼 문제
#n, k = map(int, input().split())
n = 25
k = 3

count = 0
count += n % k

if n % k != 0:
    for i in range(n % k):
        n -= 1

while True: 
    n //= k
    count += 1
    if n == 1 :
        break

print(count)