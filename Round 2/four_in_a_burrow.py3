# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Round 2 - Problem B: Four in a Burrow
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-2/problems/B
#
# Time:  O((R * C) * (R + 1)^C)
# Space: O(C * (R + 1)^C)
#
# pass in PyPy3 but Python3
#

def four_in_a_burrow():
    def bfs1():
        init = tuple(R for _ in range(C))
        lookup = {init}
        q = [init]
        target = 'C'
        while q:
            new_q = []
            for state in q:
                for j in range(C):
                    if state[j]-1 < 0:
                        continue
                    if grid[state[j]-1][j] != target:
                        continue
                    new_state = tuple(state[i]-int(i == j) for i in range(C))
                    if new_state in lookup:
                        continue
                    lookup.add(new_state)
                    new_q.append(new_state)
            q = new_q
            target = 'F' if target == 'C' else 'C'
        return lookup

    def bfs2():
        init = tuple(0 for _ in range(C))
        lookup = {init}
        q = [init]
        target = 'F'
        while q:
            new_q = []
            for state in q:
                for j in range(C):
                    if state[j]+1 > R:
                        continue
                    if grid[state[j]][j] != target:
                        continue
                    new_state = tuple(state[i]+int(i == j) for i in range(C))
                    if new_state in lookup:
                        continue
                    lookup.add(new_state)
                    new_q.append(new_state)
            q = new_q
            target = 'C' if target == 'F' else 'F'
        return lookup

    def build(state):
        return [['.' if i < state[j] else grid[i][j] for j in range(C)] for i in range(R)]

    def check(new_grid, target):
        return any((all(i+k < R and new_grid[i+k][j] == new_grid[i][j] == target for k in range(1, L)) or
                    all(j+k < C and new_grid[i][j+k] == new_grid[i][j] == target for k in range(1, L)) or
                    all(i+k < R and j+k < C and new_grid[i+k][j+k] == new_grid[i][j] == target for k in range(1, L)) or
                    all(i+k < R and j-k >= 0 and new_grid[i+k][j-k] == new_grid[i][j] == target for k in range(1, L)))
                   for i in range(R) for j in range(C))

    _ = input()
    grid = [list(input()) for _ in range(R)]
    lookup1 = bfs1()
    lookup2 = bfs2()
    has_C = has_F = False
    if len(lookup1) > len(lookup2):
        lookup1, lookup2 = lookup2, lookup1
    for x in lookup1:
        if x not in lookup2:
            continue
        new_grid = build(x)
        if not has_C:
            if check(new_grid, 'C') and not check(new_grid, 'F'):
                has_C = True
                if has_F:
                    return '?'
        if not has_F:
            if check(new_grid, 'F') and not check(new_grid, 'C'):
                has_F = True
                if has_C:
                    return '?'
    return 'C' if has_C else 'F' if has_F else 0

R, C = 6, 7
L = 4
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, four_in_a_burrow()))
