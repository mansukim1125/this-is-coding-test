from typing import Dict, List
from math import inf
import heapq


def dijkstra(graph: Dict[int, List[List[int]]], start: int) -> List[int]:
  distance = [inf] * (len(dict.keys(graph)) + 1)
  distance[start] = 0

  queue = [(0, start)]

  while len(queue) > 0:
    cost, node = heapq.heappop(queue)
    for adj_cost, adj_node in graph[node]:
      if distance[adj_node] > distance[node] + adj_cost:
        distance[adj_node] = distance[node] + adj_cost
        heapq.heappush(queue, distance[adj_node])
  
  return distance


def solution():
  N, M = map(int, input().split())
  
  graph = {}
  for i in range(1, M + 1):
    graph[i]
    pass

if __name__ == '__main__':
  pass