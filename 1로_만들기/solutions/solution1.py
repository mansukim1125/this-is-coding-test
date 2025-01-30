def minimum_operations_to_one(number: int):
  calc_count = [0] * 30_001
  for i in range(2, 30001):
    calc_count_candidates = []
    if i % 5 == 0:
      calc_count_candidates.append(calc_count[i // 5])
    if i % 3 == 0:
      calc_count_candidates.append(calc_count[i // 3])
    if i % 2 == 0:
      calc_count_candidates.append(calc_count[i // 2])
    calc_count_candidates.append(calc_count[i - 1])
    calc_count[i] = min(calc_count_candidates) + 1
  return calc_count[number]

def solution():
  X = int(input())
  operation_count = minimum_operations_to_one(X)
  print(operation_count)


if __name__ == '__main__':
  solution()
