def solution():
    coordinate = input()

    init_x = ord(coordinate[0]) - ord('a')
    init_y = ord(coordinate[1]) - ord('1')

    ds = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, -2), (-1, -2), (1, 2), (-1, 2)]
    valid_count = 0
    for d in ds:
        x_is_valid = 0 <= init_x + d[0] <= 7
        y_is_valid = 0 <= init_y + d[1] <= 7
        valid_count += int(x_is_valid and y_is_valid)

    print(valid_count)


if __name__ == '__main__':
    solution()
