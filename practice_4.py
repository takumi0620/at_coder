# Shigt only
def judge(array):
    for num in array:
        if num % 2 == 1:
            return False
    return True

def run(array):
    if judge(array):
        global result
        result += 1
        run(list(map(lambda num: num / 2, array)))
    else:
        print(result)

result = 0
count = int(input())
targetNumberArray = list(map(lambda strNum: int(strNum), input().split()))
run(targetNumberArray)