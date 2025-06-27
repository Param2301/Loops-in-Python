#Task 1: Countdown Timer with while Loop
start = int(input("Enter the starting number: "))

countdown = start

print("Starting countdown:", end=" ")
while countdown >= 1:
    print(countdown, end=" ")
    countdown -= 1
    
print("Yeahhhhhh! 🚀")

#Task 2: Multiplication Table with for Loop
number = int(input("Enter a number: "))

print(f"\nMultiplication table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

#Task3: Factorial Calculator with for Loop
number = int(input("Enter a number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i 

print(f"The factorial of {number} is {factorial}.")

if number <= 5:  
    calculation = " × ".join(str(i) for i in range(1, number + 1))
    print(f"Calculation: {calculation} = {factorial}")
