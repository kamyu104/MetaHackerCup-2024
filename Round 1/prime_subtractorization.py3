# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Round 1 - Problem B. Prime Subtractorization
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-1/problems/B
#
# Time:  precompute: O(MAX_N)
#        runtime:    O(1)
# Space: O(MAX_N)
#

def prime_subtractorization():
    N = int(input())
    return DP[N]

def linear_sieve_of_eratosthenes(n):  # Time: O(n), Space: O(n)
    primes = []
    spf = [-1]*(n+1)  # the smallest prime factor
    for i in range(2, n+1):
        if spf[i] == -1:
            spf[i] = i
            primes.append(i)
        for p in primes:
            if i*p > n or p > spf[i]:
                break
            spf[i*p] = p
    return spf

MAX_N = 10**7
SPF = linear_sieve_of_eratosthenes(MAX_N)
DP = [0]*(MAX_N+1)
DP[5] = 2
for i in range(6, MAX_N+1):
    DP[i] = DP[i-1]+int(SPF[i] == i and SPF[i-2] == i-2)
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, prime_subtractorization()))
