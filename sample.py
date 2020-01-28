# インプット例
# 1
# 2 3
# 文字列
a = int(input())
b, c = list(map(lambda num: int(num), input().split()))
str = input()

print("{} {}".format(a + b + c, str))