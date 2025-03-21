from math import inf
import heapq


def dijkstra(graph, node_count, start):
  optimal_costs = [inf] * (node_count + 1)
  optimal_costs[start] = 0

  queue = [(0, start)]
  while len(queue) > 0:
    through_cost, through_node = heapq.heappop(queue)

    if through_cost > optimal_costs[through_node]:
      continue

    for adj_cost, adj_node in graph[through_node]:
      renewed_cost = optimal_costs[through_node] + adj_cost
      if renewed_cost < optimal_costs[adj_node]:
        optimal_costs[adj_node] = renewed_cost
        heapq.heappush(queue, (renewed_cost, adj_node))

  return optimal_costs


def solution():
  node, edge, entry_point = map(int, input().split())
  graph = {}

  for _ in range(edge):
    start, end, cost = map(int, input().split())
    
    if start in graph:
      graph[start].append((cost, end))
    else:
      graph[start] = [(cost, end)]

  cost_table = dijkstra(graph, node, entry_point)
  valid_nodes = [cost for cost in cost_table[1:] if cost != inf]

  print(len(valid_nodes) - 1, max(valid_nodes))


if __name__ == '__main__':
  solution()
