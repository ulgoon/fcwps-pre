#random module 불러오기
import random

#1~100 사이 임의의 정수를 불러와 answer에 지정
answer = random.randint(1,100)
print(answer)

# 사용자로부터 이름과 답 입력받기
username = input("What is your name? ")
guess = eval(input("Hi, " + username + " guess the number: "))

# if 조건문을 활용해 정답 판단하기
if guess == answer:
    print("Correct! Answer was " + str(answer))
else:
    print("You are wrong!!")
