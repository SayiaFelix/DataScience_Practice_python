import math

seconds = input("Enter seconds: ")
seconds = int(seconds)

original_seconds = seconds  # Store the original value for output

hrs = seconds // 3600
seconds %= 3600
mins = seconds // 60
secs = seconds % 60

print(f"{original_seconds} seconds = {hrs} hrs {mins} mins {secs} secs")


def circle_calc(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    diameter = 2 * radius
    return area, circumference, diameter


if __name__ == "__main__":
    r = input("Enter a radius: ")
    r = float(r)
    area, c, d = circle_calc(r)
    print(f"area {area}, circumference {c}, diameter {d}")
