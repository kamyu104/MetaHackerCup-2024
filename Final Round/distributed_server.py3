# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Final Round - Problem B. Distributed Server
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/final-round/problems/B
#
# Time:  O((R + C) * log26 * (R + C) * V^2 * E)
#      = O((R + C) * log26 * (R + C) * (R * C)^2 * (R * C))
#      = O((R + C)^2 * (R * C)^3)
# Space: O(R * C)
#

from collections import deque

# Time:  O(V^2 * E)
# Space: O(V + E)
class Dinic(object):
    def __init__(self, n):
        self.adj = [[] for _ in range(n)]
        self.source = 0
        self.sink = n-1

    def add_edge(self, i, j, c):
        self.adj[i].append([j, c, len(self.adj[j])])
        self.adj[j].append([i, 0, len(self.adj[i]) - 1])

    def max_flow(self, S, T):
        def bfs(S, T, adj, lev):  # Time: O(E), levelize
            for i in range(len(adj)):
                lev[i] = -1
            lev[S] = 0
            q = deque([S])
            while q:
                v = q.popleft()
                for i in range(len(adj[v])):
                    to, cap, rev = adj[v][i]
                    if cap and lev[to] == -1:
                        lev[to] = lev[v] + 1
                        q.append(to)
            return lev[T] != -1

        def dfs(S, T, v, f, adj, lev, done):  # Time: O(V * E), augment
            if v == T or not f:
                return f
            while done[v] < len(adj[v]):
                to, cap, rev = adj[v][done[v]]
                if lev[to] > lev[v]:
                    t = dfs(S, T, to, min(f, cap), adj, lev, done)
                    if t > 0:
                        adj[to][rev][1] += t
                        adj[v][done[v]][1] -= t
                        return t
                done[v] += 1
            return 0

        adj = self.adj
        V = len(self.adj)
        f = 0
        lev = [-1] * V
        while bfs(S, T, adj, lev):  # at most O(V) times
            done = [0] * V
            while True:
                t = dfs(S, T, S, float("inf"), adj, lev, done)
                if t == 0:
                    break
                f += t
        return f

def binary_search_right(left, right, check):
    while left <= right:
        mid = left + (right-left)//2
        if not check(mid):
            right = mid-1
        else:
            left = mid+1
    return right

def distributed_server():
    def check(x):
        def index(i, j, out):
            return out*(R*C)+(i*C+j)+1

        result.append(chr(ord('a')+x))
        for d, robots in enumerate(lookup):
            if not robots:
                continue
            dinic = Dinic(1+(R*C)*2+1)
            for i, j in robots:
                dinic.add_edge(dinic.source, index(i, j, 0), 1)
            for i in range(R):
                for j in range(C):
                    if not (0 <= i+j-d < len(result)):
                        continue
                    dinic.add_edge(index(i, j, 0), index(i, j, 1), 1)
                    if G[i][j] > result[i+j-d]:
                        dinic.add_edge(index(i, j, 1), dinic.sink, 1)
                        continue
                    if G[i][j] < result[i+j-d]:
                        continue
                    if i+j-d == len(result)-1:
                        dinic.add_edge(index(i, j, 1), dinic.sink, 1)
                        continue
                    if i+1 < R:
                        dinic.add_edge(index(i, j, 1), index(i+1, j, 0), 1)
                    if j+1 < C:
                        dinic.add_edge(index(i, j, 1), index(i, j+1, 0), 1)
            if dinic.max_flow(dinic.source, dinic.sink) != len(robots):
                result.pop()
                return False
        result.pop()
        return True

    R, C = list(map(int, input().split()))
    G = [list(input()) for _ in range(R)]
    lookup = [[] for _ in range(R+C-1)]
    for i in range(R):
        for j in range(C):
            if not G[i][j].isupper():
                continue
            G[i][j] = G[i][j].lower()
            lookup[i+j].append((i, j))
    result = []
    while (i := binary_search_right(0, 25, check)) != -1:
        result.append(chr(ord('a')+i))
    return "".join(result)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, distributed_server()))
