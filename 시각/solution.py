'''
010101 -> 111
222222 -> 222222
030303 -> 333
223303 -> 22333

'''


def solution():
    N = int(input())

    three_count = 0
    for hour in range(N + 1):
        # print(hour)
        for min in range(60):
            for sec in range(60):
                time_exp = f'{hour}{min}{sec}'
                print('time_exp:', time_exp)
                if '3' in time_exp:
                    three_count += 1

    print(three_count)


if __name__ == '__main__':
    solution()
