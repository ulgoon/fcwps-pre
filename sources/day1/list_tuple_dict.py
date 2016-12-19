print("=" * 40)
# 빈 list를 선언합니다. 선언과 동시에 값을 채워넣을 수 있습니다.
# lang = ["python", "c", "java", "golang"]
lang = []

# list에 요소를 추가합니다.
lang.append("python")
lang.append("java")
lang.append("golang")
print(lang)

# 혹은 특정한 위치에 원하는 값을 추가할 수 있습니다.
lang.insert(1, "c")
print(lang)

# 특정 요소를 삭제할 수도 있습니다.
lang.remove("golang")
print(lang)

# 혹은 리스트에 있던 값을 빼낼 수도 있습니다.
java = lang.pop(2)
print(lang)
print(java)

print("=" * 40)
# 리스트를 정렬하는 법을 알아봅니다.
numbers = [2, 1, 4, 3]
print(numbers)

numbers.sort()
print(numbers)

# 리스트를 역순으로 출력하고 싶을땐 이렇게 한답니다.
numbers = [2, 1, 4, 3]
numbers.reverse()
print(numbers)

# 특정 값의 위치를  출력할땐 이렇게 합니다.
index_of_two = numbers.index(2)
print(index_of_two)

# 리스트끼리 더할 땐 extend를 활용합니다.
numbers += [5, 6]
print(numbers)
numbers.extend([7, 8])
print(numbers)

# Tuple
print("=" * 40)

# Tuple은 괄호를 이용해 선언할 수 있습니다.
tuple1 = (1, 2, 3, 4)

# tuple은 삭제나 추가가 불가능합니다.
# del tuple[1]
# tuple1[1] = 'c'

# tuple끼리 더하거나 반복하는 것은 가능합니다.
tuple2 = (5, 6)
print(tuple1 + tuple2)

print(tuple1 * 3)

print("=" * 40)
# dictionary의 선언
dict1 = {}
print(dict1)

# dictionary는 key와 value로 이루어져 있으며, 추가하는 법은 다음과 같습니다.
dict1 = {'name': 'foo bar'}
print(dict1)

dict1 = {'korean': 95, 'math': 100, 'science': [80, 70, 90, 60]}
print(dict1)

dict1['english'] = "pass"
print(dict1)

# 요소 삭제는 del을 활용합니다.
del dict1['math']
print(dict1)

# key를 활용해 value를 출력하는 법을 알아봅시다.
print(dict1['korean'])

# key만 출력하는 법을 알아봅시다.
print(dict1.keys())

# value만 출력할땐 이렇게 합니다.
print(dict1.values())

# key와 value를 함께 출력합니다.
print(dict1.items())
