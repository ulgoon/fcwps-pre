# 문자열을 이용한 다양한 함수 활용
python = "Hi, there. I'm python. Python is very easy."

# H의 갯수를 세어주는 count함수와 p의 위치를 출력하는 find
print(python.count("H"))
print(python.find("p"))

# python이라는 문자열에 comma를 끼워넣기
comma = ","
print(comma.join(python))
print(comma.join("python"))
print(comma.join(["p","y","t","h","o","n"]))

# 문자열 혹은 리스트를 괄호안의 기준을 활용하여 분할하기
print(python.split())
print(python.split("."))

# python이라는 문자열을 golang으로 바꾸기
print(python.replace("python","golang"))
