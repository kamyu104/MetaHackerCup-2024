# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Round 3 - Problem B: Least Common Ancestor
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-3/problems/B
#
# Time:  O(N * (logN)^2)
# Space: O(N)
#

from sortedcontainers import SortedList
from collections import defaultdict

def least_common_ancestor():
    def update(sl, cnt, u, d):
        if u in cnt:
            sl.remove((cnt[u], u))
        cnt[u] += d
        if cnt[u]:
            sl.add((cnt[u], u))
        else:
            del cnt[u]            

    def merge(sl1, cnt1, sl2, cnt2):
        if len(sl1) < len(sl2):
            sl1, cnt1, sl2, cnt2 = sl2, cnt2, sl1, cnt1
        for c, u in sl2:
            update(sl1, cnt1, u, c)
        return sl1, cnt1

    def least_common(sl):
        return sl[0][1] if sl else -1

    def iter_dfs():
        A, D = [-1]*N, [-1]*N
        sl, cnt = SortedList(), defaultdict(int)
        ret = [SortedList(), defaultdict(int)]
        stk = [(1, (0, ret))]
        while stk:
            step, args = stk.pop()
            if step == 1:
                u, ret = args
                A[u] = least_common(sl)
                update(sl, cnt, s_to_idx[S[u]], +1)
                stk.append((4, (u, ret)))
                stk.append((2, (u, 0, ret)))
            elif step == 2:
                u, i, ret = args
                if i == len(adj[u]):
                    continue
                v = adj[u][i]
                stk.append((2, (u, i+1, ret)))
                new_ret = [SortedList(), defaultdict(int)]
                stk.append((3, (v, new_ret, ret)))
                stk.append((1, (v, new_ret)))
            elif step == 3:
                v, new_ret, ret = args
                ret[:] = merge(ret[0], ret[1], new_ret[0], new_ret[1])
            elif step == 4:
                u, (curr_sl, curr_cnt) = args
                update(sl, cnt, s_to_idx[S[u]], -1)
                D[u] = least_common(curr_sl)
                update(curr_sl, curr_cnt, s_to_idx[S[u]], +1)
        return A, D

    def find_hash():
        result = 0
        for i in range(N):
            result = (result*(len(s_to_idx)+1)+(A[i]+1))%MOD
            result = (result*(len(s_to_idx)+1)+(D[i]+1))%MOD
        return result

    N = int(input())
    P, S = [-1]*N, [None]*N
    for i in range(N):
        P[i], S[i] = list(input().split())
        P[i] = int(P[i])-1
    adj = [[] for _ in range(N)]
    for u in range(N):
        if P[u] >= 0:
            adj[P[u]].append(u)
    s_to_idx = {x:i for i, x in enumerate(sorted(set(S)))}
    A, D = iter_dfs()
    return find_hash()

MOD = 998244353
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, least_common_ancestor()))
