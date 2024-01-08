# check whether given number is odd or even

number = int(input("enter the number : "))

flag = True # assume given number is even

if number % 2 == 0:
    flag = True
else:
    flag = False

if flag:
    print(f"{number} is even number")
else:
    print(f"{number} is odd number")


print("hello world")