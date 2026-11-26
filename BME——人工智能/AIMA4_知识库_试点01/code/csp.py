"""第 6 章教学实现。二元关系须按检查方向取参，邻接表须双向。"""
from collections import deque
from random import Random


def ac3(domains, neighbors, allowed, arcs=None):
    """原地收缩域。返回 False 能证明无解，True 表示队列已清空。"""
    if any(not values for values in domains.values()):
        return False
    if arcs is None:
        arcs = ((x, y) for x in domains for y in neighbors[x])
    queue = deque(dict.fromkeys(arcs))
    queued = set(queue)
    while queue:
        x, y = queue.popleft()
        queued.remove((x, y))
        keep = {a for a in domains[x] if any(allowed(x, a, y, b) for b in domains[y])}
        if keep == domains[x]:
            continue
        domains[x] = keep
        if not keep:
            return False
        for z in neighbors[x]:
            arc = (z, x)
            if z != y and arc not in queued:
                queue.append(arc)
                queued.add(arc)
    return True


def solve(domains, neighbors, allowed):
    """MAC + MRV、剩余度、LCV。域值可排序，以便重现实验。"""
    def visit(current):
        open_vars = [x for x in current if len(current[x]) > 1]
        if not open_vars:
            # 全图弧一致，故单值域的唯一组合满足每条边。
            return {x: next(iter(values)) for x, values in current.items()}
        def priority(x):
            return len(current[x]), -sum(len(current[y]) > 1 for y in neighbors[x])
        x = min(open_vars, key=priority)
        def damage(a):
            return sum(not allowed(x, a, y, b) for y in neighbors[x] for b in current[y])
        for a in sorted(current[x], key=lambda value: (damage(value), value)):
            branch = {k: set(values) for k, values in current.items()}
            branch[x] = {a}
            if ac3(branch, neighbors, allowed, ((y, x) for y in neighbors[x])):
                answer = visit(branch)
                if answer is not None:
                    return answer
        return None

    current = {x: set(values) for x, values in domains.items()}
    if ac3(current, neighbors, allowed):
        return visit(current)
    return None


def min_conflicts(domains, neighbors, allowed, seed=0, steps=1000):
    """返回 (解或 None, 走过的步数)。保持原有单值域。"""
    if any(not values for values in domains.values()):
        return None, 0
    rng = Random(seed)
    state = {x: rng.choice(sorted(values)) for x, values in domains.items()}
    def cost(x, value):
        return sum(not allowed(x, value, y, state[y]) for y in neighbors[x])
    for step in range(steps + 1):
        conflicts = [x for x in state if cost(x, state[x])]
        if not conflicts:
            return state, step
        movable = [x for x in conflicts if len(domains[x]) > 1]
        if not movable or step == steps:
            return None, step
        x = rng.choice(movable)
        scores = [(cost(x, a), a) for a in sorted(domains[x])]
        best = min(score for score, _ in scores)
        state[x] = rng.choice([a for score, a in scores if score == best])


MAP_EDGES = ("WA NT", "WA SA", "NT SA", "NT Q", "Q SA", "Q NSW",
             "NSW SA", "V SA", "V NSW")


def graph(vertices, edges):
    adj = {v: [] for v in vertices}
    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)
    return adj


def different(x, a, y, b):
    return a != b


def australia(colors):
    names = "WA NT SA Q NSW V T".split()
    return ({x: set(range(colors)) for x in names},
            graph(names, [pair.split() for pair in MAP_EDGES]), different)


def queens(n):
    vertices = range(n)
    neighbors = graph(vertices, ((i, j) for i in vertices for j in range(i)))
    def compatible(i, r, j, s):
        return r != s and abs(r - s) != abs(i - j)
    return {i: set(vertices) for i in vertices}, neighbors, compatible


if __name__ == "__main__":
    print("地图着色（0 起编号）", solve(*australia(3)))
    print("四皇后（行列均从 0 起）", min_conflicts(*queens(4), seed=7))