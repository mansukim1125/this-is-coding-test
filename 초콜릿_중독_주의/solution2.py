import sys


input = sys.stdin.readline

def eval(equation: str) -> int:
    operand = int(equation[-1] == '!')

    right = len(equation) - 1
    while equation[right] == '!':
        right -= 1

    operand = int(equation[right]) | operand

    reversal_count = max(right, 0)

    return operand ^ reversal_count % 2



def solution():
    n = int(input())
    for _ in range(n):
        print(eval(input()[:-1]))


if __name__ == '__main__':
    solution()
