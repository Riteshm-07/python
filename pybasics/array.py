# =============================
# PYTHON ARRAYS / LISTS FULL EXAMPLE
# =============================

# In Python, arrays are usually created using LISTS

# -----------------------------
# CREATE ARRAY
# -----------------------------
numbers = [10, 20, 30, 40, 50]

print("Original Array:")
print(numbers)

# -----------------------------
# ACCESS ELEMENTS
# -----------------------------
print("\nFirst Element:", numbers[0])
print("Last Element:", numbers[-1])

# -----------------------------
# CHANGE VALUE
# -----------------------------
numbers[1] = 200

print("\nAfter Changing Second Element:")
print(numbers)

# -----------------------------
# ADD ELEMENTS
# -----------------------------

# Add at end
numbers.append(60)

# Add at specific position
numbers.insert(2, 999)

print("\nAfter Adding Elements:")
print(numbers)

# -----------------------------
# REMOVE ELEMENTS
# -----------------------------

# Remove by value
numbers.remove(40)

# Remove last element
numbers.pop()

print("\nAfter Removing Elements:")
print(numbers)

# -----------------------------
# ARRAY LENGTH
# -----------------------------
print("\nTotal Elements:", len(numbers))

# -----------------------------
# LOOP THROUGH ARRAY
# -----------------------------
print("\nLoop Using For Loop:")

for item in numbers:
    print(item)

# -----------------------------
# LOOP WITH INDEX
# -----------------------------
print("\nLoop With Index:")

for i in range(len(numbers)):
    print("Index", i, "=", numbers[i])

# -----------------------------
# CHECK ELEMENT EXISTS
# -----------------------------
print("\nCheck Value Exists:")

if 30 in numbers:
    print("30 Found")
else:
    print("30 Not Found")

# -----------------------------
# SORT ARRAY
# -----------------------------
numbers.sort()

print("\nSorted Array:")
print(numbers)

# -----------------------------
# REVERSE ARRAY
# -----------------------------
numbers.reverse()

print("\nReversed Array:")
print(numbers)

# -----------------------------
# SUM OF ARRAY
# -----------------------------
total = sum(numbers)

print("\nSum of Array:", total)

# -----------------------------
# MAX AND MIN
# -----------------------------
print("Maximum Value:", max(numbers))
print("Minimum Value:", min(numbers))

# -----------------------------
# COPY ARRAY
# -----------------------------
copy_array = numbers.copy()

print("\nCopied Array:")
print(copy_array)

# -----------------------------
# 2D ARRAY
# -----------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\n2D Array:")

for row in matrix:
    print(row)

# -----------------------------
# USER INPUT ARRAY
# -----------------------------
print("\nCreate Your Own Array")

arr = []

size = int(input("How many elements: "))

for i in range(size):
    value = int(input("Enter Number: "))
    arr.append(value)

print("Your Array:", arr)

# -----------------------------
# FIND EVEN AND ODD
# -----------------------------
print("\nEven Numbers:")

for num in arr:
    if num % 2 == 0:
        print(num)

print("\nOdd Numbers:")

for num in arr:
    if num % 2 != 0:
        print(num)

# -----------------------------
# SEARCH ELEMENT
# -----------------------------
search = int(input("\nEnter Number To Search: "))

if search in arr:
    print(search, "Found in Array")
else:
    print(search, "Not Found")

# -----------------------------
# END
# -----------------------------
print("\nProgram Finished")