"""
Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of
comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,9,25,49,81
"""


li = list(input().split(","))

ans = [int(i)*int(i) for i in li if int(i) % 2 != 0]
print(ans)
