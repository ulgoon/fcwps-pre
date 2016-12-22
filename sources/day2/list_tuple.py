lang = []

lang.append("python")
lang.append("java")
lang.append("golang")
lang.append("julia")
lang.append("golang")

lang.insert(1, "c")

lang.remove("golang")

java = lang.pop(2)

# =========================
# sorting
# =========================
numbers = [2, 1, 4, 3]
print(numbers)

# numbers.sort()
# numbers.reverse()

print(numbers.index(2))

numbers = numbers + [5, 6]
print(numbers)

numbers.extend([7, 8])
print(numbers)



