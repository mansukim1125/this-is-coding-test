from typing import List


def calculate_maximum_stolen_value(ingredients: List[int]) -> int:
  max_ingredients = [0] * 100

  max_ingredients[0] = ingredients[0]
  max_ingredients[1] = max(ingredients[1], max_ingredients[0])

  for i in range(2, len(ingredients)):
    max_ingredients[i] = max(ingredients[i] + max_ingredients[i - 2], max_ingredients[i - 1])

  return max_ingredients[len(ingredients) - 1]

def solution():
  input() # 사용하지 않는 값
  ingredients = list(map(int, input().split()))
  max_stolen_value = calculate_maximum_stolen_value(ingredients)
  print(max_stolen_value)


if __name__ == '__main__':
  solution()
