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
