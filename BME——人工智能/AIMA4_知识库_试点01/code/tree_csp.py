"""无环二元约束图的两遍求解。输入是无重复边、双向的邻接表。"""
from csp import different, graph


def solve_forest(domains, neighbors, allowed):
    remaining = {x: set(values) for x, values in domains.items()}
    if any(not values for values in remaining.values()):
        return None
    parent, order = {}, []
    for root in remaining:
        if root in parent:
            continue
        parent[root] = root
        stack = [root]
        while stack:
            x = stack.pop()
            order.append(x)
            for child in neighbors[x]:
                if child == x:
                    raise ValueError("自环不属于森林")
                if child == parent[x]:
                    continue
                if child in parent:
                    raise ValueError("输入含环")
                parent[child] = x
                stack.append(child)
    for child in reversed(order):
        x = parent[child]
        if x == child:
            continue
        remaining[x] = {a for a in remaining[x]
                        if any(allowed(x, a, child, b) for b in remaining[child])}
        if not remaining[x]:
            return None
    result = {}
    for x in order:
        p = parent[x]
        result[x] = next(a for a in remaining[x] if x == p or allowed(p, result[p], x, a))
    return result


if __name__ == "__main__":
    from random import Random
    from check_csp import solutions
    rng = Random(615)
    for _ in range(100):
        nodes = range(6)
        edges = [(i, rng.randrange(i)) for i in range(1, 6) if rng.random() < .8]
        adj = graph(nodes, edges)
        d = {x: {a for a in range(3) if rng.random() < .7} for x in nodes}
        answer = solve_forest(d, adj, different)
        valid = list(solutions(d, adj, different))
        assert (answer in valid) if valid else (answer is None)
    print("100 个随机森林的两遍求解结果与穷举一致。")