# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used
import sys
import operator

def main():
    """Implement the calculator"""
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    return ops[sys.argv[2]](int(sys.argv[1]), int(sys.argv[3]))

if __name__ == "__main__":
    print(main())
