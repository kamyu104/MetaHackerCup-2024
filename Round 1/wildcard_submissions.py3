# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Round 1 - Problem E. Wildcard Submissions
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-1/problems/E
#
# Time:  O(N * L * S), L = max(len(s) for s in S), S = len(dp)
# Space: O(L * S)
#
# pass in PyPy3 but Python3
#

from collections import defaultdict

def wildcard_submissions():
    def longest_common_prefix(a, b):
        if len(a) > len(b):
            a, b = b, a
        c = list(a)
        for i in range(len(a)):
            if a[i] == b[i] or b[i] == '?':
                continue
            if c[i] != '?':
                break
            c[i] = b[i]
        else:
            i = len(a)
        return "".join(c[:i])

    N = int(input())
    S = [input() for _ in range(N)]
    result = 0
    dp = defaultdict(int)
    for s in S:
        for t, c in list(dp.items()):
            x = longest_common_prefix(t, s)
            if x:
                dp[x] = (dp[x]-c)%MOD
        dp[s] = (dp[s]+1)%MOD
    result = 1
    for s, c in dp.items():
        for i in range(len(s)):
            if s[i] == '?':
                c = (c*26)%MOD
            result = (result+c)%MOD
    return result

MOD = 998244353
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, wildcard_submissions()))
