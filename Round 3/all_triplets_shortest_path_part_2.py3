# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Round 3 - Problem E1: All Triplets Shortest Path (Part 2)
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-3/problems/E2
#
# Time:  O(N)
# Space: O(N)
#

def all_triplets_shortest_path_part_2():
    S = input()
    N = int(input())
    U_V = [list(map(lambda x: int(x)-1, input().split())) for _ in range(N-1)]
    adj = [[] for _ in range(N)]
    for u, v in U_V:
        adj[u].append(v)
        adj[v].append(u)
    i = S.index('k')
    if i == 0:
        return "Lucky"
    if i == 1:
        return "Lucky" if not any(sum(v < u for v in adj[u]) >= 2 and any(len(adj[v]) >= 2 for v in adj[u] if v < u) for u in range(N)) else "Wrong"
    smaller_cnt = list(map(lambda u: sum(v < u for v in adj[u]), range(N)))
    mn_adj = list(map(min, adj))
    check1 = not any(any(v > u and smaller_cnt[v] >= 2 for v in adj[u]) and any(v < u for v in adj[u]) for u in range(N))
    check2 = not any(sum(v > u and smaller_cnt[v] >= 2 for v in adj[u]) >= 2 and any(v > u and smaller_cnt[v] >= 2 and mn_adj[v] < u for v in adj[u]) for u in range(N))
    return "Lucky" if check1 and check2 else "Wrong"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, all_triplets_shortest_path_part_2()))
