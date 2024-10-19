# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Round 2 - Problem A1: Cottontail Climb (Part 1)
# https:#www.facebook.com/codingcompetitions/hacker-cup/2024/round-2/problems/A1
#
# Time:  precompute: O(sum((9-i)*(2*i+1) for i in range(9))) = O(285)
#        runtime:    O(nCr(9, 2)) = O(45)
# Space: O(nCr(9, 2)) = O(45)
#

def cottontail_climb_part_1():
    A, B, M = list(map(int, input().split()))
    return sum(A <= x <= B for x in CANDIDATES if x%M == 0)

CANDIDATES = []
for i in range(1, 9+1):
    for j in range(i, 9+1):
        curr = 0
        for k in range(i, j+1):
            curr = curr*10+k
        for k in reversed(range(i, j)):
            curr = curr*10+k
        CANDIDATES.append(curr)
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, cottontail_climb_part_1()))
