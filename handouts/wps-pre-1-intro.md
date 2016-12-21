# Fastcampus 
## Web Programming SCHOOL
### Python Basic
2016.12.19

---
<!-- page_number:true -->

## Introduce

### 최우영

- Solution Architect, Back-End Developer at unknown team
- Solution Architect, Web Developer
- Skills: Python, Golang, Julia, Node.js, ...

blog: https://ulgoon.github.io
github: https://github.com/ulgoon


---
## Web Programming?
- a broad term for the work involved in developing a web site for the internet(World Wide Web) or an intranet(private network)

---
## 그 중에서도 우리는 백엔드 개발자!!
- Back-End
Data access Layer
프론트엔드의 요청에 따라 데이터에 접근하여 적절한 응답을 전달하는 Middleware

- Front-End
Presentation Layer
사용자에게 실제 보여지는 부분을 렌더링하고, 사용자의 요청을 Back-End에 전달하는 역할

---
## Back-End
Python - **Django**, Flask
java - spring
C# - asp.net
javaScript - Node.js
golang - itself
ruby - ruby on rails
PHP - Laravel

---
## Shell Basic
```
$ mkdir python - make directory python
$ cd python - change directory
$ cd .. - up to

$ ls
$ ls -al

$ touch hello.py - create hello.py
$ exit - terminate shell
$ mv hello.py /python
$ cp hello.py /python

$ python --version
$ python --help
```

---
## vim Basic
`$ vim hello.py`

Command
```
h,j,k,l - cursor
i - insert
v - visual
d - delete
y - yank
p - paste
u - undo
r - replace
$ - move end of line
^ - move start of line

:q - quit
:q! - quit(no warning)
:wq - write and quit

:{number} - move to {number}th line
```


---
## Python Basic


---
## Python Basic

### Python은? 
1989년 크리스마스 연휴를 보내던  Guido van Rossum이 만든 고급 프로그래밍 언어

### 특징
- 인터프리터
- 객체지향
- 동적타이핑
- 엄격한 문법

---
## Python Basic

Python으로 할 수 있는 것들!
- System Programming
- Web Programming
- Data Analysis
- ...

---
## Python Basic

### REPL - Read - Eval - Print Loop
코드를 입력하면 바로 결과를 확인할 수 있음!!

### We'll use python3

[difference of 2.x , 3.x](https://wiki.python.org/moin/Python2orPython3)
Short version: Python 2.x is legacy, Python 3.x is the present and future of the language

---
### version management

[pyenv setup](https://jkeun.github.io/post/python-dev-env-setting/)
[yyuu official repo](https://github.com/yyuu/pyenv)

- ubuntu
```
$ git clone https://github.com/yyuu/pyenv.git ~/.pyenv

$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

$ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

```
$ pyenv version
$ pyenv install 3.5.2
$ pyenv shell 3.5.2
$ python --version
```
---
## Hello python!

So, let's try!!

```python
print("hello python!")
```

---
## Numbers & Math

```python
print(3 + 7)
print(10 - 3)
print(15 / 7)
print(34 * 100)
```

---
## Boolean

```python
print(3 < 7)
print(10 < 3)
print(15 > 7)
print(34 == 100)

!=
>=
<=
```

---
## Variable

```python
print("hello python!")
hello = "hello"
python = "python!"
print(hello, python)
```
```python
num1 = 14
num2 = 5

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
```

---
## input
```python
name = input("What is your name? ")
print("Hi, ", name)
```

## input with evaluation
```python
input("How old are you? ")
eval(input("How old are you? "))

equals to raw_input(), input() in python 2.x
```

---
## String Formatting

```
print("I have a %s, I have an %s." % ("pen","apple"))
```

```
%s - string
%c - character
%d - Integer(decimal)
%f - floating-point
%o - 8진수(Octal)
%x - 16진수(hexadecimal)
%% - %
```

---
## String Functions
```
func.count('p')

func.find('p')

comma = ","
func = comma.join('python')

func.split(',')
python_is_easy.split()

python_is_easy.replace("python", "golang")
```


---
## List, Tuple, Dictionary
List
```
animals = ['','','']
```

Tuple

```
animals = ('','','')
```
Dictionary
```
user = {'name':'fastcampus','age':'27',city:['seoul','busan','incheon']}
```

---
## List detail
```
python_is_easy[start:end]

python_is_easy[0:5]
python_is_easy[:5]
python_is_easy[5:]
python_is_easy[37:-3]

easy_to_learn = python_is_easy[:36]
can_do_this = python_is_easy[37:]
```

---
## If
```python
if 조건:
	실행문

if 조건1 and 조건2:
	실행문

if 조건1 or 조건2:
	실행문
if not 조건:
	실행문
```

### Comparison Operators
```
x == n
x != n

x < n
x > n
x <= n
x >= n
```


---
## else
```python
if 조건:
	실행문1
else:
	실행문2
```

## else if

```python
if 조건1:
	실행문1
else:
	if 조건2:
		실행문2
	else:
		실행문3
```

---
## elif
```python
if 조건1:
	실행문1
elif 조건2:
	실행문2
elif 조건3:
	실행문3
...
else:
	실행문n
```

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