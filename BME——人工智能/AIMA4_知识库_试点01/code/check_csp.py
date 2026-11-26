"""用独立枚举解集检查保解性、完备性和示例答案。"""
from itertools import product
from random import Random
from csp import ac3, solve, australia, different, graph, queens, min_conflicts


def solutions(domains, neighbors, allowed):
    for row in product(*domains.values()):
        assigned = dict(zip(domains, row))
        if all(allowed(x, assigned[x], y, assigned[y]) for x in domains for y in neighbors[x]):
            yield assigned


def main():
    rng = Random(610)
    for trial in range(240):
        variables = range(rng.randrange(1, 6))
        domains = {i: {v for v in range(3) if rng.random() < .84} for i in variables}
        tables = {(i, j): {(a, b) for a in range(3) for b in range(3) if rng.random() < .48}
                  for i in variables for j in variables if i < j and rng.random() < .64}
        neighbors = graph(variables, tables)
        def allowed(i, a, j, b):
            if i < j:
                return (a, b) in tables[i, j]
            return (b, a) in tables[j, i]
        before = {x: d.copy() for x, d in domains.items()}
        answers = list(solutions(domains, neighbors, allowed))
        answer = solve(domains, neighbors, allowed)
        assert (answer in answers) if answers else (answer is None)
        assert before == domains
        reduced = {x: d.copy() for x, d in domains.items()}
        consistent = ac3(reduced, neighbors, allowed)
        assert consistent or not answers
        assert all(all(sol[x] in reduced[x] for x in domains) for sol in answers)
    assert [sum(1 for _ in solutions(*australia(k))) for k in (2, 3, 4)] == [0, 18, 768]
    d, n, rule = australia(2)
    assert ac3(d, n, rule) and solve(d, n, rule) is None
    for a, b in [(1, 0), (0, 2)]:
        d, n, rule = australia(3)
        d['WA'], d['V'] = {a}, {b}
        assert not ac3(d, n, rule)
    d, n, rule = queens(4)
    ans, _ = min_conflicts(d, n, rule, seed=7)
    assert ans in list(solutions(d, n, rule))
    assert [sum(not rule(3, r, i, s) for i, s in enumerate([1, 3, 0])) for r in range(4)] == [1, 3, 0, 1]
    assert solve({}, {}, different) == {}
    assert solve({'T': set()}, {'T': []}, different) is None
    print('240 个随机小型二元 CSP 与穷举一致；保解性、非对称关系、地图、皇后和空域检查通过。')


if __name__ == '__main__':
    main()