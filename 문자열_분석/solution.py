import sys


input = sys.stdin.readline

def solution():
    while True:
        line = input().rstrip('\n')
        if not line:
            break

        lower_count = sum(1 for ch in line if ch.islower())
        upper_count = sum(1 for ch in line if ch.isupper())
        num_count = sum(1 for ch in line if ch.isdigit())
        space_count = sum(1 for ch in line if ch.isspace())

        print(lower_count, upper_count, num_count, space_count)


if __name__ == '__main__':
    solution()
