# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Round 3 - Problem A: Set Cover
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-3/problems/A
#
# Time:  O(N^2)
# Space: O(N)
#

def set_cover():
    def min_max_i_j(target):
        mn_i = mn_j = N
        mx_i = mx_j = -1
        for i in range(N):
            for j in range(N):
                if G[i][j] != target:
                    continue
                mn_i = min(mn_i, i)
                mn_j = min(mn_j, j)
                mx_i = max(mx_i, i)
                mx_j = max(mx_j, j)
        return mn_i, mn_j, mx_i, mx_j

    N, K = list(map(int, input().split()))
    G = [list(input()) for _ in range(N)]
    mn_i_1, mn_j_1, mx_i_1, mx_j_1 = min_max_i_j('1')
    mn_i_q, mn_j_q, mx_i_q, mx_j_q = min_max_i_j('?')
    if K == 0:
        return (mx_i_1-mn_i_1+1)*(mx_j_1-mn_j_1+1)
    if K == 1:
        return max((max(i, mx_i_1)-min(i, mn_i_1)+1)*(max(j, mx_j_1)-min(j, mn_j_1)+1) for i in range(N) for j in range(N) if G[i][j] == '?')
    if K == 2:
        row_mn_j_q = [N]*N
        row_mx_j_q = [-1]*N
        for i in range(N):
            for j in range(N):
                if G[i][j] != '?':
                    continue
                row_mn_j_q[i] = min(row_mn_j_q[i], j)
                row_mx_j_q[i] = max(row_mx_j_q[i], j)
        return max((max(i, j, mx_i_1)-min(i, j, mn_i_1)+1)*(max(row_mx_j_q[j], mx_j_1)-min(row_mn_j_q[i], mn_j_1)+1) for i in range(N) for j in range(N))
    if K == 3:
        return max(max((max(i, mx_i_1)-min(mn_i_q, mn_i_1)+1)*(max(j, mx_j_1)-min(mn_j_q, mn_j_1)+1),
                       (max(mx_i_q, mx_i_1)-min(i, mn_i_1)+1)*(max(j, mx_j_1)-min(mn_j_q, mn_j_1)+1),
                       (max(i, mx_i_1)-min(mn_i_q, mn_i_1)+1)*(max(mx_j_q, mx_j_1)-min(j, mn_j_1)+1),
                       (max(mx_i_q, mx_i_1)-min(i, mn_i_1)+1)*(max(mx_j_q, mx_j_1)-min(j, mn_j_1)+1))
                   for i in range(N) for j in range(N) if G[i][j] == '?')
    return (max(mx_i_q, mx_i_1)-min(mn_i_q, mn_i_1)+1)*(max(mx_j_q, mx_j_1)-min(mn_j_q, mn_j_1)+1)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, set_cover()))
