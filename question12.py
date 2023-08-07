"""
Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each
digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
li = []
bi = []
for i in range(1000, 3000 + 1):
    li.append(i)
print(li)


def calculate(i):
    flag = False
    no = i
    while i > 0:
        n = i % 10
        i = i // 10
        if n % 2 != 0:
            flag = True
            break
    if not flag:
        bi.append(no)


for i in li:
    calculate(i)

print(bi)
