# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Final Round - Problem D. Sushi Platter
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/final-round/problems/D
#
# Time:  O(NlogN + MlogM + N^2 * (N * MAX_A) + M * min(L, N * MAX_A) + M! * ((M - 1) * 2^(M - 1))), MAX_A = max(A) = 100
#      = O(N^3 * MAX_A + M! * ((M - 1) * 2^(M - 1))), if L >= N * MAX_A and N >= M
# Space: O(N^2 * MAX_A + M * min(L, N * MAX_A)
#      = O(N^2 * MAX_A), if L >= N * MAX_A and N >= M
#

from itertools import permutations

def popcount(x):
    return bin(x).count('1')

def sushi_platter():
    # reference: https://codeforces.com/blog/entry/45593
    # modified from template: https://ideone.com/bj9pm9
    def fill_A():
        dp = [[[] for _ in range(3)] for _ in range(N+1)]
        mx = 0
        if A[1]-A[0] <= L:
            if not A[1]-A[0] < len(dp[1][1]):
                mx = max(mx, A[1]-A[0])
                dp[1][1].extend((0 for _ in range(((A[1]-A[0])+1)-len(dp[1][1]))))
            dp[1][1][A[1]-A[0]] = 2
        if 2*(A[1]-A[0]) <= L:
            if not 2*(A[1]-A[0]) < len(dp[1][0]):
                mx = max(mx, 2*(A[1]-A[0]))
                dp[1][0].extend((0 for _ in range(((2*(A[1]-A[0]))+1)-len(dp[1][0]))))
            dp[1][0][2*(A[1]-A[0])] = 1
        for i in range(1, N):
            new_dp = [[[] for _ in range(3)] for _ in range(N+1)]
            diff = (A[i+1] if i+1 < N else A[-1]+1)-A[i]
            for j in reversed(range(1, i+1)):
                for k in range(3):
                    for v in reversed(range(len(dp[j][k]))):
                        if not dp[j][k][v]:
                            continue
                        if v+diff*(2*j-k-1) <= L and k <= 1 and 2*j-k-1 >= 1:  # appending a endpoint to an existing connected component.
                            if not v+diff*(2*j-k-1) < len(new_dp[j][k+1]):
                                mx = max(mx, v+diff*(2*j-k-1))
                                new_dp[j][k+1].extend((0 for _ in range(((v+diff*(2*j-k-1))+1)-len(new_dp[j][k+1]))))
                            new_dp[j][k+1][v+diff*(2*j-k-1)] = (new_dp[j][k+1][v+diff*(2*j-k-1)]+dp[j][k][v]*(2-k)*(j-k)) % MOD
                        if v+diff*(2*j-k+1) <= L and k <= 1:  # creating a new connected component with a endpoint
                            if not v+diff*(2*j-k+1) < len(new_dp[j+1][k+1]):
                                mx = max(mx, v+diff*(2*j-k+1))
                                new_dp[j+1][k+1].extend((0 for _ in range(((v+diff*(2*j-k+1))+1)-len(new_dp[j+1][k+1]))))
                            new_dp[j+1][k+1][v+diff*(2*j-k+1)] = (new_dp[j+1][k+1][v+diff*(2*j-k+1)]+dp[j][k][v]*(2-k)) % MOD
                        if v+diff*(2*j-k) <= L:  # appending a non-endpoint to an existing connected component
                            if not v+diff*(2*j-k) < len(new_dp[j][k]):
                                mx = max(mx, v+diff*(2*j-k))
                                new_dp[j][k].extend((0 for _ in range(((v+diff*(2*j-k))+1)-len(new_dp[j][k]))))
                            new_dp[j][k][v+diff*(2*j-k)] = (new_dp[j][k][v+diff*(2*j-k)]+dp[j][k][v]*(2*j-k)) % MOD
                        if v+diff*(2*j-k+2) <= L:  # creating a new connected component with a non-endpoint
                            if not v+diff*(2*j-k+2) < len(new_dp[j+1][k]):
                                mx = max(mx, v+diff*(2*j-k+2))
                                new_dp[j+1][k].extend((0 for _ in range(((v+diff*(2*j-k+2))+1)-len(new_dp[j+1][k]))))
                            new_dp[j+1][k][v+diff*(2*j-k+2)] = (new_dp[j+1][k][v+diff*(2*j-k+2)]+dp[j][k][v]) % MOD
                        if v+diff*(2*j-k-2) <= L and j >= 2 and 2*j-k-2 >= 1: # merging connected components
                            if not v+diff*(2*j-k-2) < len(new_dp[j-1][k]):
                                mx = max(mx, v+diff*(2*j-k-2))
                                new_dp[j-1][k].extend((0 for _ in range(((v+diff*(2*j-k-2))+1)-len(new_dp[j-1][k]))))
                            new_dp[j-1][k][v+diff*(2*j-k-2)] = (new_dp[j-1][k][v+diff*(2*j-k-2)]+dp[j][k][v]*((j-k)*(j-k-1)+(j-k)*k)) % MOD
            dp = new_dp
        return dp, mx

    def fill_B():
        prefix = [[[0]*((min(L, mx)+1)+1) for _ in range(4)] for _ in range(min(M, len(dp))+1)]
        for cnt_B in range(1, len(prefix)):
            for e in range(4):
                c = popcount(e)
                cnt_A = cnt_B-1 if c == 2 else cnt_B if c == 1 else cnt_B+1
                for i in range(min(L, mx)+1):
                    cnt = dp[cnt_A][2-c][i] if cnt_A < len(dp) and i < len(dp[cnt_A][2-c]) else 0
                    if e == 1 or e == 2:
                        cnt = (INV_2*cnt) % MOD
                    cnt *= FACT[cnt_B-1]
                    prefix[cnt_B][e][i+1] = (prefix[cnt_B][e][i]+cnt) % MOD
        result = 0
        B.sort()
        for p in permutations(B):
            for mask in range(1<<(M-1)):
                cnt_B = 1+popcount(mask)
                total = sum(abs(p[i+1]-p[i]) for i in range(M-1) if not mask&(1<<i))
                for e in range((3 if cnt_B != 1 else 2)+1):
                    new_total = total
                    for i in range(M):
                        if (i > 0 and mask&(1<<(i-1))) or (i == 0 and e != 1 and e != 3):
                            new_total += p[i]-(A[-1]+1)
                        if (i < M-1 and mask&(1<<i)) or (i == M-1 and e != 2 and e != 3):
                            new_total += p[i]-(A[-1]+1)
                    if cnt_B < len(prefix) and min(L-new_total, mx) >= 0:
                        result = (result+prefix[cnt_B][e][min(L-new_total, mx)+1]) % MOD
        return result

    N, M, L = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    dp, mx = fill_A()
    return fill_B()

MOD = 10**9+7
INV_2 = pow(2, MOD-2, MOD)
MAX_M = 5
FACT = [1]
while not MAX_M-1 < len(FACT):
    FACT.append(FACT[-1]*len(FACT) % MOD)
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, sushi_platter()))