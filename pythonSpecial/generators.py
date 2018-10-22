
def cube(n):
    for i in range(n):
        yield i**3


def print_cube():
    for i in cube(4):
        print(i)


def main_gen():
    print_cube()