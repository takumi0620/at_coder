# Product
a, b = list(map(lambda strNum: int(strNum), input().split()))

def judge(a, b):
    return a * b % 2 == 0

if judge(a, b):
    print("Even")
else:
    print("Odd")