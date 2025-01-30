"""
작성자: 김준석
작성일: 2024-12-20
프로그램명: 부품 찾기 (이진 탐색 버전)
설명: 가게의 부품 재고 여부를 이진 탐색으로 확인하는 프로그램
입력: 
   - N: 가게가 가지고 있는 부품의 개수
   - N개의 부품 번호
   - M: 손님이 요청한 부품의 개수
   - M개의 부품 번호
출력: 각 부품이 있으면 yes, 없으면 no를 공백으로 구분하여 출력
"""

def binary_search(key, iterable):
  sorted_list = sorted(iterable)
  start = 0
  end = len(iterable) - 1

  while start <= end:
    mid = (start + end) // 2
    if key < iterable[mid]:
      end = mid - 1
    elif iterable[mid] < key:
      start = mid + 1
    else:
      return iterable[mid]
    
  return None


def solution():
  N = int(input())
  parts = list(map(int, input().split()))
  M = int(input())
  requested_parts = list(map(int, input().split()))

  for part in requested_parts:
    result = binary_search(part, parts)
    print('no' if result is None else 'yes', end=' ')


if __name__ == '__main__':
  solution()
