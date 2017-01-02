# Fastcampus 
## Web Programming SCHOOL
### Python Basic
2016.12.22

---
<!-- page_number:true -->

## Review
- Shell Basic
- Vim Basic
- install pyenv
- Python Basic
	- Numbers & Math
	- Boolean
	- Variable
	- Input
	- String Formatting
	- List, Dictionary
	- If

---
## List again!!

### [link](https://github.com/ulgoon/fcwps-pre)

---
## numguess
```python
import random


answer = random.randint(1,100)
print(answer)
```

---
## numguess
```python
username = input("Hi there, What's your name?? ")
guess = eval(input("Hi, "+ username + "guess the number: "))

if guess == answer:
	print("Correct! The answer was ", str(answer))
else:
	print("That's not what I wanted!! The answer was ", str(answer))
```

---
## numguess advanced!!

how to make it with more fun??

1. 반복문
2. 재귀호출

---
## For, while
```python
for 변수 in (리스트 or 문자열):
	실행문1
    ...
```
```python
for i in ["python", "java", "golang"]:
	print(i)
```

---
## For, while
```python
sum = 0
for i in range(1,11):
	sum += i
	print(sum)
```
### List Comprehension
```python
result = [i for i in range(1,11)]
print(result)
```

---
## For, while
```python
while 조건:
	실행문1
	...
```

```python
while name != "foo bar":
	name = input("What's your name? ")
	print("Hi, " + name + "So, where is foo bar?")
```

```python
while 1:
	print("Hello world!")
```


---
## Fizzbuzz

```python
num = eval(input("type the number: "))

for i in range(1, num + 1):
	if i % 15 == 0:
		print("fizzbuzz")
	elif i % 3 == 0:
		print("fizz")
	elif i % 5 == 0:
		print("fizz")
	else:
		print(i)
```

---
## Refactoring numguess
```python
import random


answer = random.randint(1,100)
username = input("Hi there, What's your name?? ")

while True:
	guess = eval(input("Hi, "+ username + "guess the number: "))

	if guess == answer:
		print("Correct! The answer was ", str(answer))
		break
	else:
		print("That's not what I wanted!! Try again!!")
```

---
## function
![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Function_color_example_3.svg/440px-Function_color_example_3.svg.png)
- 수학적 정의: 첫 번째 집합의 임의의 한 원소를 두 번째 집합의 오직 한 원소에 대응시키는 대응 관계
- x: 정의역 y: 공역

---
## function
![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Function_machine2.svg/440px-Function_machine2.svg.png)
- 프로그래밍에서의 함수: 입력값을 내부에서 어떤 처리를 통해 결과값을 출력하는 것

---
## function

```python
def function_name(parameter):
	실행문1
	실행문2
	...
	return y
```

---
## Leap year
4로 나뉘어 떨어지면 윤년,
100으로 나뉘어 떨어지면 평년,
400으로 나뉘어 떨어질땐 윤년

---
## Leap year(answer)
```python

leap = False
def is_leap(year):
	if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
		leap = True
	return leap
    
year = int(input("Is leap?? "))
print(is_leap(year))

```

---
## numguess with function

```python
def guesser(guess):
	while True:
		if guess == answer:
			print("Correct! The answer was ", str(answer))
			break
		else:
			print("That's not what I wanted!! Try again!!")
```

---
## Class

- 객체를 생성하기 위해 변수와 메소드를 생성하는 틀
- or **Blueprint**

```python
class Classname:
	method1
	method2
	...
```

---
## PPAP?

```python
def pen_adder(param):
	pen = pen + param
	print(pen)
```
만약 Pineapple Pen과 Apple Pen이 동시에 존재해야 한다면??

```python
ppen = pen
apen = pen

def ppen_adder(param):
	global ppen
	ppen += param
	print(ppen)

def apen_adder(param):
	global apen
	apen += param
	print(apen)
```

---
## PPAP class!!

```python
class Ppap:
	def __init__(self):
		self.result = pen

	def pen_adder(self, param):
		self.result += param
		return self.result
	def pen_adder_reverse(self, param):

pineapple_pen = Ppap()
apple_pen = Ppap()

print(pineapple_pen.pen_adder(pineapple))
print(apple_pen.pen_adder_reverse(apple))
```

---
## Object?? Instance???

- Object: 저장공간에서 할당된 공간
- Instance: Class에 의해 생성된 Object

```python
class fastcampus:
	pass

//John은 fastcampus 클래스의 인스턴스
john = fastcampus()

// sally는 input 명령의 객체
sally = input()
```

---
## Class

```python
class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_a_song(self):
		for line in self.lyrics:
			print(line)

ppap = Song(["I have a pen.", "I have an apple.", "uh!", "apple pen!"])

ppap.sing_a_song()

```