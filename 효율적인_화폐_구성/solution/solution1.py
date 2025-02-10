from typing import List


def min_currency_count(currencies: List[int], target_money: int) -> int:
  min_coins = [0] * (10000 + 1)

  for currency in currencies:
    min_coins[currency] = 1

  for money in range(1, target_money + 1):
    candidate = []
    for currency in currencies:
      if money - currency >= 0 and min_coins[money - currency] != -1:
        candidate.append(min_coins[money - currency] + 1)

    if len(candidate) <= 0:
      min_coins[money] = -1
    else:
      min_coins[money] = min(candidate)

  return min_coins[target_money]

def solution():
  # min_count = min_currency_count([2, 3], 15)
  min_count = min_currency_count([3, 5, 7], 4)
  print(min_count)


if __name__ == '__main__':
  solution()
