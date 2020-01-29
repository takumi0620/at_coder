# Coins
result = 0
COIN_50 = 50
COIN_100 = 100
COIN_500 = 500

def isFinish(currentMoney):
    return currentMoney == money

def calculate(currentMoney, num, coin):
    global result
    for i in range(num + 1):
        tmp = currentMoney + i * coin
        if isFinish(tmp):
            result += 1
            return

        if coin == COIN_500:
            calculate(tmp, num100, COIN_100)
        elif coin == COIN_100:
            calculate(tmp, num50, COIN_50)

num500 = int(input())
num100 = int(input())
num50 = int(input())
money = int(input())
calculate(0, num500, COIN_500)

print(result)