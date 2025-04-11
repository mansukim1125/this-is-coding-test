import sys

input = sys.stdin.readline


def solution():
    n = int(input())

    x_occurrence, y_occurrence = {}, {}

    for _ in range(n):
        x, y = input().split()
        if x in x_occurrence:
            x_occurrence[x] += 1
        else:
            x_occurrence[x] = 1

        if y in y_occurrence:
            y_occurrence[y] += 1
        else:
            y_occurrence[y] = 1

    x_items = list(filter(lambda item: item[1] >= 2, list(dict.items(x_occurrence))))
    y_items = list(filter(lambda item: item[1] >= 2, list(dict.items(y_occurrence))))

    print(len(x_items) + len(y_items))


if __name__ == '__main__':
    solution()
