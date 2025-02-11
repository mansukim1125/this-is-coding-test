from typing import List


def min_currency_count(currencies: List[int], target_money: int) -> int:
  efficient_count = [10001] * (target_money + 1)
  efficient_count[0] = 0
  for currency in currencies:
    for money in range(currency, target_money + 1):
      if money - currency >= 0:
        efficient_count[money] = min(efficient_count[money], efficient_count[money - currency] + 1)

  if efficient_count[target_money] == 10001:
    return -1
  else:
    return efficient_count[target_money]


def solution():
  # min_count = min_currency_count([2, 3], 15)
  min_count = min_currency_count([3, 5, 7], 4)
  print(min_count)


if __name__ == '__main__':
  solution()
