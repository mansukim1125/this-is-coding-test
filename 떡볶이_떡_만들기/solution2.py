def calculate_diff_with_upper(heights, upperbound):
    diff_arr = [0] * len(heights)
    for i in range(len(heights)):
        diff_arr[i] = max(heights[i] - upperbound, 0)

    return diff_arr


def determine_upperbound(heights, target):
    start = 0
    end = max(heights)
    optimal_upperbound = 0

    while (start <= end):
        upperbound = (start + end) // 2
        diff = sum(calculate_diff_with_upper(heights, upperbound))
        if (diff < target):
            end = upperbound - 1
        elif (diff > target):
            start = upperbound + 1
        else:
            optimal_upperbound = upperbound
            break

    return optimal_upperbound


def solution():
    N, M = map(int, input().split())
    heights = list(map(int, input().split()))

    upperbound = determine_upperbound(heights, M)

    return upperbound


if __name__ == '__main__':
    print(solution())
