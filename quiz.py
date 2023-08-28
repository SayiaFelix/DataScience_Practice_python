# print('Welcome to quiz')

print("\n1\n")

result = ["heads", "tails", "tails", "heads", "tails", "heads", "heads", "tails", "tails", "tails"]

"""
Number of Heads
"""

# result_count = result.count('heads')
# print(result_count)

# for res in result:
#     res_count = res.count('heads')
#     print(res_count)

count = 0
for item in result:
    if item == "heads":
        count += 1
print("Heads count: ", count)

"""
Square of Numbers between 1 and ten
"""
print("\n2\n")

number = list(range(1, 11))
print(number)

for num in number:
    numSquere = num * num
    """
    or
    """
    numsquere = num ** 2

    # print(numSquere)
    print("Squares: ", numsquere)

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print("Square of even number:", i * i)
"""
Expense
"""

# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.
print("\n3\n")

month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
e = input("Enter expense amount: ")
e = int(e)

month = -1
for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i
        break

if month != -1:
    print(f'You spent {e} in {month_list[month]}')
else:
    print(f'You didn\'t spend {e} in any month')


# 4. Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message
print("\n4\n")

for i in range(5):
    print(f"You ran {i + 1} miles")
    # i starts with zero hence adding 1
    tired = input("Are you tired? ")
    if tired == 'yes':
        break

if i == 4:
    # 4 because the index starts from 0
    print("Hurray! You are a rock star! You just finished 5 km race!")
else:
    print(f"You didn't finish 5 km race but hey congrats anyways! You still ran {i + 1} miles")

# 5. Write a program that prints following shape
# ```
# *
# **
# ***
# ****
# *****
# ```
print("\n5\n")

for i in range(1, 6):
    s = ''
    for j in range(i):
        s += '*'
    print(s)
