# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Round 2 - Problem D: Splitting Hares
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-2/problems/D
#
# Time:  O(NlogN + N * MAX_W + MAX_W^2)
# Space: O(N * MAX_W)
#

from collections import defaultdict

def splitting_hares():
    def count():
        cnt, total = defaultdict(int), defaultdict(int)
        for i in range(N):
            if W[i] != -1:
                cnt[C[i]] += 1
            total[C[i]] += 1
        return cnt, total

    def mapping():
        weight_to_color = [0]*((L+2)+1)
        color_to_weights = defaultdict(list)
        for i in range(N):
            if W[i] == -1:
                continue
            weight_to_color[W[i]] = C[i]
            color_to_weights[C[i]].append(W[i])
        for w in color_to_weights.values():
            w.sort()
        return weight_to_color, color_to_weights

    def sort_colors():
        sorted_colors = []
        lookup = set()
        prev = 0
        for c in weight_to_color:
            if not (c and c != prev):
                continue
            prev = c
            if c in lookup:
                return [], False
            lookup.add(c)
            sorted_colors.append(c)
        return sorted_colors, True

    def find_candidates():
        candidates = {}
        for c in cnt.keys():
            i = total[c]-cnt[c]
            if i == 0:
                candidates[c] = [color_to_weights[c]]
            elif i == 1:
                if len(color_to_weights[c]) == 1:
                    a = color_to_weights[c][0]
                    candidates[c] = [(a-1, a), (a, a+1)]
                elif len(color_to_weights[c]) == 2:
                    a, b = color_to_weights[c]
                    if b-a == 1:
                        candidates[c] = [(a-1, a, b), (a, b, b+1)]
                    else:
                        candidates[c] = [(a, i, b) for i in range(a+1, b)]
            elif i == 2:
                a = color_to_weights[c][0]
                candidates[c] = [(a-2, a-1, a), (a-1, a, a+1), (a, a+1, a+2)]
            candidates[c] = [x for x in candidates[c] if x[0] >= 1]
        return candidates

    def find_dp():
        dp = [[] for _ in range(len(sorted_colors)+1)]
        dp[0] = [(-1,)*5]
        for i, c in enumerate(sorted_colors):
            for j, x in enumerate(candidates[c]):
                mn = float("inf")
                best = None
                for idx, (_, _, right, b, c) in enumerate(dp[i]):
                    if right >= x[0]:
                        continue
                    if not i:
                        b, c = float("inf"), x[1]-x[0]
                        for k in range(2, len(x)):
                            a, b, c = b, c, min(b, c)+(x[k]-x[k-1])
                    else:
                        a, b, c = b, c, min(b, c)+(x[0]-right)
                        for k in range(1, len(x)):
                            a, b, c = b, c, min(b, c)+(x[k]-x[k-1])
                        if (len(x) == 2 and a > b) or (len(x) == 3 and a < b):
                            continue
                    if c >= mn:
                        continue
                    mn = c
                    best = (idx, j, x[-1], b, c)
                if best:
                    dp[i+1].append(best)
        return dp

    def find_result():
        def backtracing():
            partial_unknowns = defaultdict(list)
            curr = 0
            for i in reversed(range(len(sorted_colors))):
                curr, j = dp[i+1][curr][:2]
                for x in candidates[sorted_colors[i]][j]:
                    if not weight_to_color[x]:
                        partial_unknowns[sorted_colors[i]].append(x)
            return partial_unknowns

        def find_full_unknowns():
            idx = MAX_W
            full_unknowns = defaultdict(list)
            for i, c in total.items():
                if i in cnt:
                    continue
                for _ in range(c):
                    full_unknowns[i].append(idx)
                    idx -= 1
                idx -= 1
            return full_unknowns

        partial_unknowns = backtracing()
        full_unknowns = find_full_unknowns()
        return [W[i] if W[i] != -1 else partial_unknowns[C[i]].pop() if C[i] in partial_unknowns else full_unknowns[C[i]].pop() for i in range(N)]

    N = int(input())
    W = list(map(int, input().split()))
    C = list(map(int, input().split()))
    cnt, total = count()
    if any(v > 3 for v in total.values()):
        return "No"
    weight_to_color, color_to_weights = mapping()
    sorted_colors, ok = sort_colors()
    if not ok:
        return "No"
    candidates = find_candidates()
    dp = find_dp()
    if not dp[-1]:
        return "No"
    result = find_result()
    return f"Yes\n{' '.join(map(str, result))}"

L = 500
MAX_W = 10000
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, splitting_hares()))
