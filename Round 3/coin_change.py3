# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Round 3 - Problem C: Coin Change
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-3/problems/C
#
# Time:  O(min(N, THRESHOLD))
# Space: O(1)
#

from math import log, ceil, floor

# https://en.wikipedia.org/wiki/Harmonic_number#Calculation
GAMMA = 0.5772156649015328606065120900824
THRESHOLD = 10**8
def H(N):
    return log(N)+GAMMA if N >= THRESHOLD else sum(1/i for i in range(1, N+1))

def ceil_divide(a, b):
    return (a+b-1)//b

def coin_change():
    N, P = list(map(int, input().split()))
    p = P/100
    # B1 = N/(1+p) = 100*N/(100+P)
    B1 = ceil_divide(100*N, 100+P)
    # 1 * (N/(N-0) + N/(N-1) + ... + N/(N-(B1-1)))
    # = 1 * (N * (1/(N-B1+1) + 1/(N-B1) + ... + 1/(N-0)))
    # = 1 * (N * (H(N)-H(N-B1)))
    result = 1*(N*(H(N)-H(N-B1)))  # [0, B1-1]
    if not P:
        return result
    # (M-1)*p >= 1
    # M >= 1/p+1 = 100/P+1
    # D = M-1 = 100/P
    D = ceil_divide(100, P)
    c = 1-(D-1)*p
    # D*N/(N-B2*c) >= D+1
    # D*N/(D+1) >= N-B2*c
    # B2*c >= N-D*N/(D+1) = N/(D+1)
    # B2 >= N/(D+1)/c = 100*N/((D+1)*(100-(D-1)*P))
    B2 = min(ceil_divide(100*N, (D+1)*(100-(D-1)*P)), N)
    # [B1, min(N, B2)-1]
    # sum(D*N/(N-x*c) for x in range(B1, min(N, B2)))
    # = D*N * (1/(N-B1*c) + 1/(N-(B1+1)*c) + ... + 1/(N-(min(N, B2)-1)*c))
    # = D*N * (1/(N/c-min(N, B2)+1) + 1/(N/c-min(N, B2)+2)... + 1/(N/c-B1)) / c
    # = D*N * (H(N/c-B1)-H(N/c-min(N, B2))) / c
    result += D*N*(sum(1/(N-x*c) for x in range(B1, min(N, B2))) if N/c-B1 < THRESHOLD else (H(N/c-B1)-H(N/c-min(N, B2)))/c)
    if B2 < N:  # [B2, N-1]
        result += (D+1)*(N-B2)
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, coin_change()))
