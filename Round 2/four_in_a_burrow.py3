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
    def bfs(init, target, d):
        lookup = {init}
        q = [init]
        while q:
            new_q = []
            for state in q:
                for j in range(C):
                    if not (0 <= state[j]+d <= R and grid[state[j]+(d if d == -1 else 0)][j] == target and (new_state := tuple(state[i]+(d if i == j else 0) for i in range(C))) not in lookup):
                        continue
                    lookup.add(new_state)
                    new_q.append(new_state)
            q = new_q
            target = 'F' if target == 'C' else 'C'
        return lookup

    def build(state):
        return [['.' if i < state[j] else grid[i][j] for j in range(C)] for i in range(R)]

    def check(new_grid, target):
        for i in range(R-L+1):
            for j in range(C):
                if all(new_grid[i+k][j] == target for k in range(L)):
                    return True
        for i in range(R):
            for j in range(C-L+1):
                if all(new_grid[i][j+k] == target for k in range(L)):
                    return True
        for i in range(R-L+1):
            for j in range(C-L+1):
                if all(new_grid[i+k][j+k] == target for k in range(L)):
                    return True
        for i in range(R-L+1):
            for j in range(L-1, C):
                if all(new_grid[i+k][j-k] == target for k in range(L)):
                    return True
        return False

    _ = input()
    grid = [list(input()) for _ in range(R)]
    lookup1 = bfs((R,)*C, 'C', -1)
    lookup2 = bfs((0,)*C, 'F', 1)
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

R, C, L = 6, 7, 4
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, four_in_a_burrow()))
