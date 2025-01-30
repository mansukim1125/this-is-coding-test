def get_diff_height(iter, sub):
  lst = [0] * len(iter)
  for x in list(iter):
    lst.append(max(x - sub, 0))
  return lst

def solution():
  N, M = map(int, input().split())
  garaetteok_heights = list(map(int, input().split()))

  max_height = max(garaetteok_heights)

  optimal_max_height = 0

  for upperbound in range(max_height, -1, -1):
    sum_of_remain = sum(get_diff_height(garaetteok_heights, upperbound))
    if sum_of_remain >= M:
      optimal_max_height = upperbound
      break

  return optimal_max_height

if __name__ == '__main__':
  print(solution())
