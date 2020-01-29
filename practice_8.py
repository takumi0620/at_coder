# Kagami Mochi
max = int(input())
inputList = []
while True:
    inputList.append(int(input()))
    if max == len(inputList):
        break

print(len(set(inputList)))