# Card Game for Two
n = int(input())
aList = list(map(lambda strNum: int(strNum), input().split()))

alice = 0
bob = 0

for i, num in enumerate(sorted(aList, reverse=True)):
    if i % 2 == 0:
        alice += num
    else:
        bob += num

print(alice - bob)