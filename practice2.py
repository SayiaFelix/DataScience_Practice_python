# print("practice2")
print("\n1\n")


def calculate_area1(b, h):
    Tarea = 1 / 2 * b * h
    print("Area of triangle base,", b, "and height,", h, "is:", Tarea, sep=' ')

    Rarea = b * h
    print("Area of Rectangle base,", b, "and height,", h, "is:", Rarea, sep=' ')

    # return area


x = 2
y = 20
while x <= 10:
    calculate_area1(x, y)
    print(" ")
    x = x + 1

# areaTriangle = calculate_area(10, 20)
# print("Area is:", areaTriangle)

print("\n2\n")


def print_pattern(n=5):
    """
    :param n: Integer number representing number of lines
    to be printed in a pattern. If n=3 it will print,
      *
      **
      ***
    If n=4, it will print,
      *
      **
      ***
      ****
    Default value for n is 5. So if function caller doesn't
    supply the input number then it will assume it to be 5
    :return: None
    """
    # we need to run two for loops. Outer loop prints patterns line by line
    # where as inner loop print the content of that specific lines

    for i in range(n):
        p = ''
        for j in range(i + 1):
            p = p + '*'
        print(p)


# 3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if
# input number is 3, ``` * ** *** ``` if input is 4 then it should print ``` * ** *** **** ``` Basically number of
# lines it prints is equal to that number. (Hint: you need to use two for loops)

print("Print pattern with input=3")
print_pattern(3)
print("Print pattern with input=4")
print_pattern(4)
print("Print pattern with no input number")
print_pattern()  # Not supplying any input will use default argument which is 5

print("\n3\n")


def calculate_area(dimension1, dimension2, shape="triangle"):
    """
    :param dimension1: In case of triangle it is "base". For rectangle, it is "length".
    :param dimension2: In case of triangle it is "height". For rectangle, it is "width".
    :param shape: Either "triangle" or "rectangle"
    :return: Area of a shape
    """
    if shape == "triangle":
        area1 = 1 / 2 * (dimension1 * dimension2)
        # Triangle area is : 1/2(Base*Height)
    elif shape == "rectangle":
        area1 = dimension1 * dimension2
        # Rectangle area is: Length*Width
    else:
        print("Error: Input shape is neither triangle nor rectangle.")
        area1 = None
        # If user didn't supply "triangle" or "rectangle" as shape then return None
    return area1


# 1. Write a function called calculate_area that takes base and height as an input and returns and area of a
# triangle. Equation of an area of a triangle is, ``` area = (1/2)*base*height ```
# 2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on
# shape type it will calculate area. Equation of rectangle's area is, ``` rectangle area=length*width ``` If no shape
# is supplied then it should take triangle as a default shape

# Calculate area of triangle whose base is 10 and height is 5
base = 10
height = 5
triangle_area = calculate_area(base, height, "triangle")
print("Area of triangle is:", triangle_area)

# Calculate area of a rectangle whose length is 20 and width is 30
length = 20
width = 30
rectangle_area = calculate_area(length, width, "rectangle")
print("Area of rectangle is:", rectangle_area)

# Calculate area of a triangle without supplying shape argument in a function call
triangle_area = calculate_area(base, height)  # Here third argument is missing
print("Area of triangle with no shape supplied: ", triangle_area)

print("\n4\n")

# Write a program that asks user to enter a city name and it should tell which country the city belongs to

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
Kenya = ["Nairobi", "Mombasa", "Nakuru", "Kisumu"]
Uganda = ["Kampala", "Tororo", "Jinja"]
Tanzania = ["Dar Es Salaam", "Dodoma", "Arusha"]

city = input("Enter city name: ")

if city in india:
    print(f"{city} is in india")
elif city in pakistan:
    print(f"{city} is in pakistan")
elif city in bangladesh:
    print(f"{city} is in bangladesh")
elif city in Kenya:
    print(f"{city} is in Kenya")
elif city in Tanzania:
    print(f"{city} is in Tanzania")
elif city in Uganda:
    print(f"{city} is in Uganda")
else:
    print(f"I won't be able to tell you which country {city} is in! Sorry!")

print("\n5\n")

#     1. Ask user to enter his fasting sugar level
#     2. If it is below 80 to 100 range then print that sugar is low
#     3. If it is above 100 then print that it is high otherwise print that it is normal

sugar = input("Please enter your fasting sugar level:")
sugar = float(sugar)
if sugar < 80:
    print("Your sugar is low, go eat some jalebi :)")
elif sugar > 100:
    print("Your sugar is high, stop eating all mithais..!")
else:
    print("Your sugar is normal, relax and enjoy your life!")

print("\n6\n")

# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

exp = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print("In feb this much extra was spent compared to jan:", exp[1] - exp[0])  # 150

# 2. Find out your total expense in first quarter (first three months) of the year
print("Expense for first quarter:", exp[0] + exp[1] + exp[2])  # 7150

# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spent 2000$ in any month? ", 2000 in exp)  # False

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print("Expenses at the end of June:", exp)  # [2200, 2350, 2600, 2130, 2190, 1980]

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
exp[3] = exp[3] - 200
print("Expenses after 200$ return in April:", exp)  # [2200, 2350, 2600, 1930, 2190, 1980]

# 2. You have a list of your favourite marvel super heros
# =['Spider-Man','thor','hulk','iron man','captain america']
# Using this list

heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
# 1. Length of the list
print(len(heros))
# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)
# 3. You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3, 'black panther')
print(heros)
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3] = ['doctor strange']
print(heros)
# 5. Sort the list in alphabetical order
heros.sort()
print(heros)

print("\n7\n")

# 1. Create 3 variables to store street, city and country, now create address variable to
# store entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
# Now Print the address in such a way that the street, city and country prints in a separate line
street = "13 patli gali"
city = "New Delhi"
country = "India"
address = street + '\n' + city + '\n' + country
print("Address using + operator:", address)
address = f'{street}\n{city}\n{country}'
print("Address using f-string:", address)

# 2. Create a variable to store the string "Earth revolves around the sun"
#     1. Print "revolves" using slice operator
#     2. Print "sun" using negative index
s = 'Earth revolves around the sun'
print(s[6:14])
print(s[-3:])

# 3. Create two variables to store how many fruits and vegetables you eat in a day.
# Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat every day.
# Use python f string for this.
num_fruits = 10
num_veggies = 5
print(f"I eat {num_veggies} veggies and {num_fruits} daily")

# 4. I have a string variable called s='maine 200 banana khaye'. This of course is a
# wrong statement, the correct statement is 'maine 10 samosa khaye'.
# Replace incorrect words in original strong with new ones and print the new string.
# Also try to do this in one line.
s = 'maine 200 banana khaye'
s = s.replace('banana', 'samosa')
s = s.replace('200', '10')
print("Using two line replace:", s)

s = 'maine 200 banana khaye'
s = s.replace('banana', 'samosa').replace('200', '10')
print("Using single line:", s)

print("\n8\n")

# 1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total
#    area using python and print it
length = 92
width = 48.8
area = length * width
print("area of football field:", area)  # Ans: 4489.599999999999

# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar,
#    and you gave shopkeeper 20 dollar.
#    Find out using python, how many dollars is the shopkeeper going to give you back?
num_packets = 9
cost_per_packet = 1.49
total_cost = num_packets * cost_per_packet
money_paid = 20
cash_back = money_paid - total_cost
print("Cash back:", cash_back)  # Ans: 6.59

# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet
#    is its length. If tiles cost 500 rs per square feet, how much will be the total
#    cost to replace all tiles. Calculate and print the cost using python
#    Hint: Use power operator (**) to find area of a square
length = 5.5
area = length ** 2  # area of square is length power 2
cost = area * 500
print("total cost for bathroom tiles replacement:", cost)  # Ans: 15125.0

# 4. Print binary representation of number 17
num = 17
print('Binary of number 17 is:', format(num, 'b'))  # Ans: 10001
