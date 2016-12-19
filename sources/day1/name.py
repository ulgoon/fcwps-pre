# 사용자 입력 받기 예제
name = input("What's your name? ")
print("Hi, " + name + " How are you?")

# input과 eval(input)(python2.x: raw_input과 input) 예제
#age = eval(input("How old are you? "))
age = input("How old are you? ")
print("Oh, You are " + age + " years old!!!")
print(type(age))
