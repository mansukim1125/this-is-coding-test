from typing import Dict, List
import math
import heapq


def get_closest_node(heap, visited: List[int]) -> int:
  item = None
  while True:
    item = heapq.heappop(heap)
    if visited[item[1]]:
      continue
    else:
      break

  return item


def dijkstra(graph: Dict[int, List[List[int]]], start: int) -> List[int]:
  distance = [math.inf] * (len(graph.keys()) + 1)

  heap = [(0, 1)]

  distance[start] = 0

  for _ in graph.keys(): # V
    _, closest_node = heapq.heappop(heap) # V

    for node, cost in graph[closest_node]: # E
      if distance[node] > distance[closest_node] + cost:
        distance[node] = distance[closest_node] + cost
        heapq.heappush(heap, (distance[node], node))

  return distance


if __name__ == '__main__':
  # vertex: v, edge: e
  graph: Dict[int, List[List[int]]] = {
    1: [[2, 2], [3, 5], [4, 1]],
    2: [[3, 3], [4, 2]],
    3: [[2, 3], [6, 5]],
    4: [[3, 3], [5, 1]],
    5: [[3, 1], [6, 2]],
    6: [],
  }

  min_costs = dijkstra(graph, start=1)
  for index, min_cost in enumerate(min_costs):
    if index > 0:
      print(min_cost)
