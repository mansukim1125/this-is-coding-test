from typing import Dict, List
import math


def get_closest_node(distance: List[int], visited: List[int]) -> int:
  min_dist = math.inf
  min_index = None
  for index, zipped in enumerate(zip(distance, visited)):
    d, v = zipped
    print(v, d)
    if v is False and d < min_dist:
      min_dist = d
      min_index = index

  return min_index


def dijkstra(graph: Dict[int, List[List[int]]], start: int) -> List[int]:
  distance = [math.inf] * (len(graph.keys()) + 1)
  visited = [False] * (len(graph.keys()) + 1)
  distance[start] = 0

  for _ in graph.keys(): # V
    closest_node = get_closest_node(distance, visited) # V
    
    visited[closest_node] = True

    for node, cost in graph[closest_node]: # E
      if visited[node]: pass
      else:
        distance[node] = min(distance[node], distance[closest_node] + cost)

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
  for min_cost in min_costs:
    print(min_cost)
