# ==============================
# PYTHON LOOPS - FULL EXAMPLE
# ==============================

print("===== FOR LOOP =====")

for i in range(5):
    print("Number:", i)


print("\n===== WHILE LOOP =====")

count = 0

while count < 5:
    print("Count:", count)
    count += 1


print("\n===== BREAK STATEMENT =====")

for i in range(10):
    if i == 5:
        print("Loop stopped at", i)
        break
    print(i)


print("\n===== CONTINUE STATEMENT =====")

for i in range(5):
    if i == 2:
        continue
    print(i)


print("\n===== NESTED LOOP =====")

for i in range(3):
    for j in range(2):
        print("i =", i, "j =", j)


print("\n===== LOOP THROUGH LIST =====")

fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)


print("\n===== LOOP THROUGH STRING =====")

name = "Python"

for letter in name:
    print(letter)


print("\n===== EVEN NUMBERS =====")

for i in range(1, 11):
    if i % 2 == 0:
        print(i)


print("\n===== SUM OF NUMBERS =====")

numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total += num

print("Total Sum =", total)


print("\n===== MULTIPLICATION TABLE =====")

num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


print("\n===== SIMPLE PATTERN =====")

for i in range(1, 6):
    print("*" * i)


print("\n===== REVERSE COUNTDOWN =====")

for i in range(10, 0, -1):
    print(i)

print("Blast Off 🚀")


print("\n===== INFINITE LOOP WITH BREAK =====")

x = 1

while True:
    print("Value:", x)

    if x == 5:
        print("Stopping loop")
        break

    x += 1


print("\n===== DONE =====")