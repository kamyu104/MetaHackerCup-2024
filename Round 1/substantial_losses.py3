# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Round 1 - Problem C. Substantial Losses
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-1/problems/C
#
# Time:  O(1)
# Space: O(1)
#

def substantial_losses():
    W, G, L = list(map(int, input().split()))
    return (2*L+1)*(W-G)%MOD

MOD = 998244353
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, substantial_losses()))
