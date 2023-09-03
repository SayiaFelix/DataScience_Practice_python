class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"Id: {self.id} \nName: {self.name}")


emp = Employee(1, 'Jay')
emp.display()

# Deleting the property of object
del emp.id
# Deleting the object itself
try:
    print(emp.id)
except AttributeError:
    print("Emp Id is not defined")

del emp
try:
    emp.display()  # it will gives error after deleting emp
except NameError:
    print("Emp is not defined")


class Animal:
    def __init__(self, habitat):
        self.habitat = habitat

    def print_habitat(self):
        print(self.habitat)

    def sound(self):
        print("Some Animal Sound")


class Dog(Animal):
    def __init__(self):
        super().__init__("Kennel")

    def sound(self):
        print("Woof woof!")


x = Dog()
x.print_habitat()
x.sound()


class Teacher:
    def teachers_action(self):
        print("I can teach")


class Engineer:
    def Engineers_action(self):
        print("I can code")


class Youtuber:
    def youtubers_action(self):
        print("I can code and teach")


class Person(Teacher, Engineer, Youtuber):
    pass


coder = Person()
coder.teachers_action()
coder.Engineers_action()
coder.youtubers_action()


class AdultException(Exception):
    pass


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def minor(self):
        if int(self.age) >= 18:
            print("You Can Go Out(Major)")
            raise AdultException
        else:
            print("Minor")
            return self.age

    def display(self):
        try:
            print(f"Age =====> {self.minor()}")
        except AdultException:
            print(f"Person is Adult: Age===>{self.age}")
        finally:
            print(f"name =====> {self.name}")


Person('Tina', 17).display()
# AdultException is raised
Person('Jay', 25).display()


# Fibonacci
class Fibonacci:
    def __init__(self, limit):
        self.prev = 0
        self.curr = 1
        self.n = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.limit:
            result = self.prev + self.curr
            self.prev = self.curr
            self.curr = result
            self.n += 1
            return result
        else:
            raise StopIteration


fib_iterator = iter(Fibonacci(10))
while True:
    # Print the Value
    try:
        print(next(fib_iterator))
    except StopIteration:
        break


#  Create Generator method such that every time it will returns a next square number

def next_square():
    i = 1
    while True:
        yield i * i
        i += 1
        # print(i)


for n in next_square():
    if n > 100:
        break
    print(n)

# Find average marks for the three subjects using command line input of marks.

import argparse as arg

if __name__ == "__main__":
    parser = arg.ArgumentParser()
    parser.add_argument("--physics", help="physics marks")
    parser.add_argument("--chemistry", help="chemistry marks")
    parser.add_argument("--maths", help="maths marks")

    args = parser.parse_args()

    print(args.physics)
    print(args.chemistry)
    print(args.maths)

    # print("Result:", (
    #         int(args.physics) + int(args.chemistry) + int(args.maths)
    # ) / 3)

    # python3 cmd.py --physics 60 --chemistry 70 --maths 90


# Create a decorator function to check that the argument passed to the function factorial is a non-negative integer:
# Create a factorial function which finds the factorial of a number.
# Use the decorator to decorate the factorial function to only allow factorial of non-negative integers.
def check(f):
    def helper(t):
        if type(t) == int and t > 0:
            return f(t)
        else:
            raise Exception("Argument is not a non-negative integer")

    return helper


@check
def factorial(p):
    if p == 1:
        return 1
    else:
        return p * factorial(p - 1)


for i in range(1, 10):
    print(i, factorial(i))

try:
    print(factorial(-1))
except Exception as e:
    e.print_exception()

try:
    print(factorial(1.354))
except Exception as e:
    e.print_exception()

# Create a Dictionary which contains the Binary values mapping with numbers found in the below integer and binary and save it in binary_dict.
# Dictionary
integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]

z = zip(integer, binary)
binary_dict = {integer: binary for integer, binary in z}

print(binary_dict)

# Create a List which contains additive inverse of a given integer list. An additive inverse a for an integer i is a number such that:
integer = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [-1 * i for i in integer]
print(additive_inverse)

# Create a set which only contains unique sqaures from a given a integer list.
integer = [1, -1, 2, -2, 3, -3]
sq_set = {i * i for i in integer}
print(sq_set)

# create any set anf try to use frozenset(setname)
# Find the elements in a given set that are not in another set
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Original sets:")
print(set1)
print(set2)
print("Difference of set1 and set2 using difference():")
print(set1.difference(set2))
print("Difference of set2 and set1 using difference():")
print(set2.difference(set1))
print("Difference of set1 and set2 using - operator:")
print(set1 - set2)
print("Difference of set2 and set1 using - operator:")
print(set2 - set1)
