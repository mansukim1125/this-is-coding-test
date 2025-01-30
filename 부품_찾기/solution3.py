"""
작성자: 김준석
작성일: 2024-12-21
프로그램명: 부품 찾기 (집합 버전)
설명: 가게의 부품 재고 여부를 집합을 이용하여 확인하는 프로그램
입력: 
   - N: 가게가 가지고 있는 부품의 개수
   - N개의 부품 번호
   - M: 손님이 요청한 부품의 개수
   - M개의 부품 번호
출력: 각 부품이 있으면 yes, 없으면 no를 공백으로 구분하여 출력
"""

def solution():
  N = int(input())
  parts = set(map(int, input().split()))
  M = int(input())
  requested_parts = list(map(int, input().split()))

  for part in requested_parts: # M
    print('yes' if part in parts else 'no', end=' ')


if __name__ == '__main__':
  solution()
