import sys


input = sys.stdin.readline

def eval(equation: str) -> int:
    exclamation_occured = 0
    if equation[-1] == '!':
        exclamation_occured = 1
    
    operand = 0
    reversal_count = 0
    for ch in equation:
        if ch.isdigit():
            if exclamation_occured:
                operand = 1
            else:
                operand = int(ch)
            break
        reversal_count += 1
    
    if reversal_count % 2 == 0:
        return operand
    else:
        return int(not operand)


def solution():
    n = int(input())
    for _ in range(n):
        print(eval(input()[:-1]))


if __name__ == '__main__':
    solution()
