def finish(i, j, k):
    if (i * 10000 + j * 5000 + k * 1000) == y and (i + j + k) == n:
        print("{} {} {}".format(i, j, k,))
        exit()

n, y = list(map(lambda strNum: int(strNum), input().split()))
for i in range(n + 1):
    finish(i, 0, 0)
    for j in range(n + 1 - i):
        finish(i, j, 0)
        finish(i, j, n - i - j)
print("-1 -1 -1")