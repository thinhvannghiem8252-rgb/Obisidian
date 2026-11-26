"""网站第 10、16 题的小规模可复现实验。耗时随机器变化。"""
from itertools import combinations
from random import Random
from statistics import mean
from time import perf_counter
from csp import ac3, different, graph, min_conflicts


def planar_map(n, seed):
    rng = Random(seed)
    points = [(rng.random(), rng.random()) for _ in range(n)]
    def side(a, b, c):
        ax, ay = points[a]
        bx, by = points[b]
        cx, cy = points[c]
        return (bx-ax)*(cy-ay) - (by-ay)*(cx-ax)
    def cross(a, b, c, d):
        return (side(a, b, c)*side(a, b, d) < 0 and
                side(c, d, a)*side(c, d, b) < 0)
    edges = []
    # 每轮随机选仍可连边的端点，连接最近且合法的邻点；连续采样避免共线退化。
    active = list(range(n))
    while active:
        a = rng.choice(active)
        def dist(b):
            return sum((x-y)**2 for x, y in zip(points[a], points[b]))
        for b in sorted((b for b in range(n) if b != a), key=dist):
            edge = tuple(sorted((a, b)))
            if edge not in edges and not any(cross(a, b, c, d) for c, d in edges):
                edges.append(edge)
                break
        else:
            active.remove(a)
    return graph(range(n), edges)


def systematic(domains, adj, mode):
    """统一静态变量序与值序，只改变是否推断。"""
    order = list(domains)
    def search(i, state, assigned):
        if i == len(order):
            return dict(assigned)
        x = order[i]
        for value in sorted(state[x]):
            if any(assigned.get(y) == value for y in adj[x]):
                continue
            nxt = {y: s.copy() for y, s in state.items()}
            nxt[x] = {value}
            if mode == 'FC':
                for y in adj[x]:
                    if y not in assigned:
                        nxt[y].discard(value)
                if any(not s for s in nxt.values()):
                    continue
            elif mode == 'MAC' and not ac3(nxt, adj, different, ((y, x) for y in adj[x])):
                continue
            assigned[x] = value
            ans = search(i+1, nxt, assigned)
            if ans is not None:
                return ans
            del assigned[x]
        return None
    return search(0, domains, {})


def verify(answer, domains, adj):
    assert all(answer[x] in domains[x] for x in domains)
    assert all(answer[x] != answer[y] for x in adj for y in adj[x])


def maps():
    for n in (6, 10, 14):
        for k in (3, 4):
            for alg in ('BT', 'FC', 'MAC', 'MC'):
                times, found = [], 0
                for seed in range(6):
                    adj = planar_map(n, seed)
                    domains = {x: set(range(k)) for x in adj}
                    start = perf_counter()
                    if alg == 'MC':
                        ans, _ = min_conflicts(domains, adj, different, seed, 200)
                    else:
                        ans = systematic(domains, adj, alg)
                    times.append(1000*(perf_counter()-start))
                    if ans is not None:
                        verify(ans, domains, adj)
                        found += 1
                print(n, k, alg, round(mean(times), 3), found, flush=True)


def sudoku():
    # 教材图 6-4 左盘，按行从上至下；0 表示空白。
    rows = ['003020600','900305001','001806400','008102900','700000008',
            '006708200','002609500','800203009','005010300']
    cells = range(81)
    def unit(i):
        r, c = divmod(i, 9)
        return r, c, (r//3)*3+c//3
    adj = graph(cells, ((i, j) for i, j in combinations(cells, 2)
                       if any(x == y for x, y in zip(unit(i), unit(j)))))
    domains = {i: {int(rows[i//9][i%9])} if rows[i//9][i%9] != '0' else set(range(1,10))
               for i in cells}
    reduced = {i: s.copy() for i, s in domains.items()}
    assert ac3(reduced, adj, different) and all(len(s)==1 for s in reduced.values())
    answer = {i: next(iter(s)) for i, s in reduced.items()}
    verify(answer, domains, adj)
    print('E6 I6 A6', [answer[(r-1)*9+5] for r in (5, 9, 1)])
    for seed in range(6):
        ans, steps = min_conflicts(domains, adj, different, seed, 1500)
        if ans is not None:
            verify(ans, domains, adj)
        print('sudoku', seed, steps, ans is not None, flush=True)


if __name__ == '__main__':
    maps()
    sudoku()