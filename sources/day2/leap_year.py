def is_leap(year):
    leap = "평년입니다"
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = "윤년입니다"
    return leap

year = int(input("Enter the year: "))
print(is_leap(year))
