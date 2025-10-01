def allPathsSourceTarget(graph):
    target = len(graph) - 1
    output = []
    path = [0]
    dfs(path, 0, graph, target, output)

    return output


def dfs(path, node, g, t, out):
    if node == t:
        out.append(path.copy())
        return

    for next_node in g[node]:
        path.append(next_node)
        dfs(path, next_node, g, t, out)
        path.pop()


if __name__ == '__main__':
    g = [[1,2],[3],[3],[]]
    result = allPathsSourceTarget(g)
    print(result)