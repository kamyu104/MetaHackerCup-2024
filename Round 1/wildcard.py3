# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Round 1 - Problem E. Wildcard
# https:#www.facebook.com/codingcompetitions/hacker-cup/2024/round-1/problems/E
#
# Time:  O(N * L * S), L = max(len(s) for s in S), S = len(dp), pass in PyPy3 but Python3
# Space: O(L * S)
#

from collections import defaultdict

def wildcard():
    def merge(a, b):
        a = list(a)
        l = min(len(a), len(b))
        for i in range(l):
            if a[i] == b[i] or b[i] == '?':
                continue
            if a[i] == '?':
                a[i] = b[i]
                continue
            l = i
            break
        return "".join(a[:l])

    N = int(input())
    S = [input() for _ in range(N)]
    result = 0
    dp = defaultdict(int)
    for s in S:
        for t, c in list(dp.items()):
            x = merge(t, s)
            dp[x] = (dp[x]-c)%MOD
        dp[s] = (dp[s]+1)%MOD
    result = 0
    for s, c in dp.items():
        result = (result+c)%MOD
        for i in range(len(s)):
            if s[i] == '?':
                c = (c*26)%MOD
            result = (result+c)%MOD
    return result

MOD = 998244353
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, wildcard()))