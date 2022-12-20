import math
f = 68
k = 0
m = 0
g = 10
x = 0.018


def cos(angle):
    math.cos(math.radians(angle))


def sin(angle):
    math.sin(math.radians(angle))

def tan(angle):
    math.tan(math.radians(angle))

print(sin(30))

while True:
    for i in range(3):
        if i == 1:
            var = input("sin")
            if var == "":
                continue
            print(sin(int(var)))
        if i == 2:
            var = input("cos")
            if var == "":
                continue
            print(cos(int(var)))
        if i == 0:
            var = input("tan")
            if var == "":
                continue
            print(tan(int(var)))
