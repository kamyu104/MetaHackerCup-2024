# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Round 3 - Problem E1: All Triplets Shortest Path (Part 1)
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-3/problems/E1
#
# Time:  O(N)
# Space: O(N)
#

def all_triplets_shortest_path_part_1():
    N = int(input())
    U_V = [list(map(lambda x: int(x)-1, input().split())) for _ in range(N-1)]
    adj = [[] for _ in range(N)]
    for u, v in U_V:
        adj[u].append(v)
        adj[v].append(u)
    return "Lucky" if not any(sum(v < u for v in adj[u]) >= 2 and any(len(adj[v]) >= 2 for v in adj[u] if v < u) for u in range(N)) else "Wrong"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, all_triplets_shortest_path_part_1()))
