num1 = int(input(""))
num2 = int(input(""))
num3 = int(input(""))
mode = int(input(""))
if mode == 1:
    max = max(num1, num2, num3)
    print(max)
if mode == 2:
    min = min(num1, num2, num3)
    print(min)
if mode == 3:
    num4 = (num1 + num2 + num3)/3
    print(num4)