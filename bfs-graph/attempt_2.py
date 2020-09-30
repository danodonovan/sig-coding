import queue


def componentsInGraph(n, m, gb, index):
    # print(f'n = {n}')
    # print(f'm = {m}')

    graph = {
        node + 1: set()
        for node in range(n)
    }

    for head, tail in gb:
        graph[head].add(tail)
        graph[tail].add(head)

    distances = [
        bfs_distance(graph, start_node=index, final_node=node)
        for node in range(1, n + 1)
        if index != node
    ]

    def _mult_dist(distance):
        if distance == 0:
            return -1
        else:
            return distance * 6

    return [
        _mult_dist(distance) for distance in distances
    ]


def bfs_distance(graph, start_node, final_node):
    # bfs
    q = queue.SimpleQueue()
    discovered = set()
    level = {}

    discovered.add(start_node)
    level[start_node] = 0
    q.put(start_node)

    while not q.empty():
        v = q.get()
        if v is final_node:
            return level[v]

        for next_node in graph[v]:
            if not next_node in discovered:
                discovered.add(next_node)
                level[next_node] = level[v] + 1
                q.put(next_node)

    return 0


if __name__ == "__main__":

    q = int(input())

    for _ in range(q):
        n, m = map(int, input().split())
        gb = [
            list(map(int, input().split()))
            for _ in range(m)
        ]
        index = int(input())

        result = componentsInGraph(n, m, gb, index)

        print(*result, sep=' ')
