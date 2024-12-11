# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Final Round - Problem A. Duplicate Order
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/final-round/problems/A
#
# Time:  O(N + min(M1, M2) + H^2)
# Space: O(N + min(M1, M2) + H)
#

fact, inv, inv_fact = [[1]*2 for _ in range(3)]
def nCr(n, k):
    if k < 0 or k > n:
        return 0
    while len(inv) <= n:  # lazy initialization
        fact.append(fact[-1]*len(inv) % MOD)
        inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
        inv_fact.append(inv_fact[-1]*inv[-1] % MOD)
    return (fact[n]*inv_fact[n-k] % MOD) * inv_fact[k] % MOD

def duplicate_order():
    N, M1, M2, H, S = list(map(int, input().split()))
    cnt = [0]*(min(M1, M2)+1)
    curr = 1
    for i in range(len(cnt)):
        cnt[i] = (nCr(N-H, i)*curr)%MOD
        curr = curr*(S-1)%MOD
    prefix = [0]*(len(cnt)+1)
    for i in range(len(cnt)):
        prefix[i+1] = (prefix[i]+cnt[i])%MOD
    pow_S_2 = [1]*(H+1)
    for i in range(len(pow_S_2)-1):
        pow_S_2[i+1] = (pow_S_2[i]*(S-2))%MOD
    result = 0
    for a in range(max(H-M1, 0), H+1):
        for b in range(max(H-M2, 0), H-a+1):
            result = (result+nCr(H, a)*nCr(H-a, b)*pow_S_2[H-a-b]*prefix[min(M1-H+a, M2-H+b)+1])%MOD
    result = (result*pow(S, N, MOD)*nCr(N, H)*pow(S-1, H, MOD))%MOD
    return result

MOD = 10**9+7
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, duplicate_order()))
