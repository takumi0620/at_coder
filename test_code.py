def calc(number):
    number += 100
    calc2(number)
    return number

def calc2(number):
    number += 100

def loop_example():
    for i in range(5):
        if i == 2:
            return
        print(i)

number = 200
print(calc(number))
print(number)

loop_example()