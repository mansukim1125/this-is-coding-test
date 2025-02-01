def count_tiling_ways(width: int) -> int:
  number_of_ways = [0] * 1001 # width + 1 이렇게 할 수도 있지만 아래 쪽에서 예외 처리가 복잡해진다.. (if 문으로 width 가 1 이하인 경우 || width 로 만들면 for 안 쪽에서 - 인덱스가 된다.)

  number_of_ways[1] = 1
  number_of_ways[2] = 3

  for i in range(3, width + 1):
    number_of_ways[i] = number_of_ways[i - 1] + number_of_ways[i - 2] * 2

  return number_of_ways[width]

def solution():
  N = int(input())
  number_of_ways = count_tiling_ways(N)
  print(number_of_ways % 796796)
  

if __name__ == '__main__':
  solution()
