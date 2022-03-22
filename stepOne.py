# G = 28
# if not G < 26:
#     print('its true')
# else:
#     print('its false')

# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1
#     if i == 4:
#         print('its gone to break ' * i)
#         continue

# sectionToo = ""
# while True:
#     section = input('>').lower()
#     if section == 'off':
#         break
#     if section == sectionToo:
#         print('повторение')
#         continue
#     if section == 'help':
#         print('U can tray')
#         print('start: its started the car')
#         print('stop its stoped the car')
#     elif section == 'start':
#         print('Its started')
#         sectionToo = section
#     elif section == 'stop':
#         print('Its Stoped')
#         sectionToo = section
#     else:
#         print('нет такой запроса')

# prices = [10, 10, 20]
# totoal = 0
# for prices in prices:
#     print(prices)
#     totoal += prices
# print(f"Prices:{totoal}")
# input()


# totoal = 0
# kd = [12, 36, 25, 14, 25]

# for pr in kd:
#     totoal += pr
# print('Pryes = ', totoal)

# numbers = [5, 2, 5, 2, 2]
# for i in numbers:
#     text1 = ('x' * i)
#     text2 = ('l' * i)
#     print(text1 + text2)

# numbers = [2, 5, 6, 10, 12, 15, 32]
# max = numbers[0]
# # max nuber  of list
# for chek in numbers:
#     if chek > max:
#         max = chek
# print(max)

# Numbers = [2, 2, 4, 5, 10, 10, 2]
# for i in Numbers:
#     if Numbers.count(i) > 1:
#         while Numbers.count(i) > 1:
#             Numbers.remove(i)
# print(Numbers)

# listNumbers = {
#     "0": "zero",
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "nine",
#     "9": "ten",
# }

# phone = input('Phone: ')
# NumbersText = ""
# for i in phone:
#     NumbersText += listNumbers[i] + " "
# print(NumbersText)


# def is_leap(year):
#     leap = False
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         leap = True

#     return leap


# year = int(input())
# print(is_leap(year))

# n = int(input())
# i = 1
# while(i <= n):
#     print(i)
#     i += 1


# n = int(input())
# nText = ""
# for i in range(1, n+1):
#     nText = nText + str(i)
# print(nText)

# class Psone:
#     def somePrint(self):
#         print('afh')

#     def constPrint(self):
#         print(3.6)


# porint = Psone()
# porint.somePrint()
# porint.constPrint()
# SOM = [[0,0,0],[x+1,0,0],[x+2,0,0]]

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# kords = []

# for i in range(0, x+1):
#     kords.insert(0, [i, 0, 0])

# for i in range(1, y+1):
#     kords.insert(0, [0, i, 0])

# for i in range(1, z+1):
#     kords.insert(0, [0, 0, i])
# # Y and Z
# for k in range(1, z+1):
#     for j in range(1, y+1):
#         kords.insert(0, [0, j, k])
# # X and Y
# for i in range(1, x+1):
#     for j in range(1, y+1):
#         kords.insert(0, [i, j, 0])
# # X and Z
# for i in range(1, x+1):
#     for k in range(1, z+1):
#         kords.insert(0, [i, 0, k])
# # X and  Y and Z
# for i in range(1, x+1):
#     for j in range(1, y+1):
#         for k in range(1, z+1):
#             kords.insert(0, [i, j, k])

# print(kords)

# re = []
# for ned in kords:
#     if sum(ned) != n:
#         re.append(ned)

# for i in range(0, x+1):
#     for j in range(0, y+1):
#         for k in range(0, z+1):
#             if i + j + k != n:
#                 kords.append([i, j, k])


# print(kords)


# n = int(input())
# arr = list(map(int, input().split()))
# print(set(arr))

# M = max(arr)

# C = arr.count(M)

# while C > 0:
#     arr.remove(M)
#     C -= 1

# print(max(arr))


# stu = []
# coins = []

# for i in range(int(input())):
#     name = input()
#     score = float(input())
#     stu.insert(i, [name, score])
#     if score not in coins:
#         coins.insert(i, score)

# stu.sort()

# coins.sort(reverse=True)

# coins.pop()

# M = min(coins)

# for i in stu:
#     for k in i:
#         if k == M:
#             print(i[0])

# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# n = int(input())
# student_marks = {}
# for i in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()

# mean = sum(student_marks[query_name]) / 3

# print(format(mean, ".2f"))


# N = int(input())
# L = []

# cmd = {
#     'pop': L.pop
# }

# for _ in range(N):

# for _ in range(N):
#     s = input().strip().split(" ")
#     if s[0] == 'insert':
#         L.insert(int(s[1]), int(s[2]))
#     elif s[0] == 'pop':
#         L.pop()
#     elif s[0] == 'remove':
#         L.remove(s[1])
#     elif s[0] == 'append':
#         L.append(s[1])
#     elif s[0] == 'sort':
#         L.sort()
#     elif s[0] == 'print':
#         print(L)
#     elif s[0] == 'reverse':
#         L.reverse()


# print(hash(tuple(map(int, input().split()))))


# n = int(input())
# integer_list = map(int, input().split())

# k = tuple(integer_list)
# print(k)
# print(hash(k))

# yu = 'FDfdsa'
# k = list(yu)
# ya = ''
# for el in k:
#     if el == el.lower():
#         ya = ya + str(el.upper())
#     else:
#         ya = ya + str(el.lower())


# print(ya)

# line = input()
# l = line.split()
# l = "-".join(l)
# print(l)

# firstname = 'fda'
# lastname = 'fdafda'
# print(f'Hello {firstname} {lastname}! You just delved into python.')
# str u sub_str


# def count_substring(string, sub_string):
#     c = 0
#     while string.find(sub_string) >= 0:
#         x = string.find(sub_string)
#         string = string[:x] + string[x+1:]
#         c = c + 1

#     return  c


# string = input().strip()
# sub_string = input().strip()

# count = count_substring(string, sub_string)


# ? как рабоатет any()
# ?
# st = 'FDsfds'

# print(any(el.isalnum() for el in st))
# print(any(el.isalpha() for el in st))
# print(any(el.isdigit() for el in st))
# print(any(el.islower() for el in st))
# print(any(el.isupper() for el in st))

# for el in st:
#     print(el.islower())


# ApplePI = aktiv Qanak@
# import time

# ApplePi = 0

# while True:
#     ApplePi = ApplePi + 0.00005
#     print(format(ApplePi, ".5f"))
#     time.sleep(5)

# import textwrap


# def wrap(string, max_width):
#     return textwrap.fill(string, max_width)


# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)


# n, m = map(int,input().split())
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))


# n = int(input())

# results = []

# for i in range(1, n+1):
#     decimal = str(i)
#     octal = str(oct(i)[2:])
#     hex_ = str(hex(i)[2:]).upper()
#     binary = str(bin(i)[2:])

#     results.append([decimal, octal, hex_, binary])
# print(results)

# width = len(results[-1][3])  # largest binary number

# for i in results:
#     print(*(rep.rjust(width) for rep in i))


# class Point:
#     def __init__(self, name):
#         self.name = name

#     def move(self):
#         print("move")


# point = Point('fds')
# point.name = "fk"
# print(point.name)

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi:{self.name}")


class Human(Person):
    pass


hg = Person("JOhn")
hg.talk()

gh = Human("f")
gh.talk()
