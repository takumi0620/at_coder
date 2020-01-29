#Some Sums
def run():
    result = 0
    for i in range(n + 1):
        aSum = sum(i)
        if a <= aSum and aSum <= b:
            result += i
    return result

def sum(targetNum):
    result = 0
    for i in list(str(targetNum)):
        result += int(i)
    return result

n, a, b = list(map(lambda strNum: int(strNum), input().split()))
print(run())