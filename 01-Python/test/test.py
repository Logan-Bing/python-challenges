def solution(n):
    roman_numbers = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    for key, value in roman_numbers.items():
        if value == n:
            print(key)
        elif value > n:
            x = value - n
            x *



solution(4)

roman_number = [[]]
