# check whether given number is prime number or not

number = int(input("enter the number : "))

flag = True

if number <= 1:
    print(f"{number} is not prime number")
elif number > 1:
    # lets check for factors
    for i in range(2, number):
        if number % i ==0:
            flag = False
            break
if flag:
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")