# the graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# the costs table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# the parents table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Пройти через каждый узел.
    for node in costs:
        cost = costs[node]
        # Если это самая низкая стоимость на данный момент и она еще не обработана...
        if cost < lowest_cost and node not in processed:
            # ... установить его как новый узел с наименьшей стоимостью.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Найдите самый дешевый узел, который вы еще не обработали.
node = find_lowest_cost_node(costs)
# Если вы обработали все узлы, этот цикл while выполнен.
while node is not None:
    cost = costs[node]
    # Пройдитесь по всем соседям этого узла.
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # Если дешевле добраться до этого соседа, пройдя через этот узел...
        if costs[n] > new_cost:
            # ... обновить стоимость для этого узла.
            costs[n] = new_cost
            # Этот узел становится новым родителем для этого соседа.
            parents[n] = node
    # Отметьте узел как обработанный.
    processed.append(node)
    # Найдите следующий узел для обработки и выполните цикл.
    node = find_lowest_cost_node(costs)

print("Cost from the start to each node:")
print(costs)