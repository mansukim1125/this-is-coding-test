from math import inf


def initialize_zero(graph):
  for row_idx in range(1, len(graph)):
    for col_idx in range(1, len(graph[row_idx])):
      if row_idx == col_idx:
        graph[row_idx][col_idx] = 0


def floyd_warshall(graph):
  for through_node in range(1, len(graph)):
    for start_idx in range(1, len(graph)):
      for end_idx in range(1, len(graph[start_idx])):
        graph[start_idx][end_idx] = min(graph[start_idx][end_idx], graph[start_idx][through_node] + graph[through_node][end_idx])


def solution():
  nodes, edges = map(int, input().split())

  graph = [[inf] * (nodes + 1) for _ in range(nodes + 1)]
  for _ in range(edges):
    row, col = map(int, input().split())
    graph[row][col] = 1
    graph[col][row] = 1

  X, K = map(int, input().split())

  initialize_zero(graph)
  floyd_warshall(graph)

  print(graph[1][K] + graph[K][X])


if __name__ == '__main__':
  solution()
