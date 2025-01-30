"""
작성자: 김준석
작성일: 2024-12-20
프로그램명: 부품 찾기
설명: 가게의 부품 재고 여부를 확인하는 프로그램
입력: 
    - N: 가게가 가지고 있는 부품의 개수
    - N개의 부품 번호
    - M: 손님이 요청한 부품의 개수
    - M개의 부품 번호
출력: 각 부품이 있으면 yes, 없으면 no를 공백으로 구분하여 출력
"""

def solution():
  N = int(input())
  parts_input = map(int, input().split())
  parts = [0] * 1000001 # 해시 테이블 방식

  for part in parts_input:
    parts[part] = 1

  M = int(input())
  requested_parts_input = map(int, input().split())

  for requested_part in requested_parts_input:
    print('yes' if parts[requested_part] == 1 else 'no', end=' ')


if __name__ == '__main__':
  solution()