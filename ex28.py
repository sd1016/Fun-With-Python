import sys

if len(sys.argv) < 4:
    print('Usage $integer1 $integer2 $integer3')
    sys.exit(1)

arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]


def max_func(a, b, c):
    if a > b and a > c:
        print("Max value is:", a)
    elif b > a and b > c:
        print("Max value is:", b)
    elif c > a and c > a:
        print("Max value is:", c)
    else:
        print("Enter 3 distinct integers to get the max value!")


if __name__ == "__main__":
    max_func(arg1, arg2, arg3)
