import sys


input = sys.stdin.readline

def eval(equation: str) -> int:
    for i, char in enumerate(equation):
        if char in '01':
            n = int(char)
            prefix = equation[:i]
            suffix = equation[i+1:]
            break
    
    # 팩토리얼(!) 연산
    if len(suffix):
        n = 1  # 0!와 1! 모두 1이므로..
    
    return n ^ (len(prefix) % 2)


def solution():
    n = int(input())
    for _ in range(n):
        print(eval(input().rstrip('\n')))

if __name__ == '__main__':
    solution()
