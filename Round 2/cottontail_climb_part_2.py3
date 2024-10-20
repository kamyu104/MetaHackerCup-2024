# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Round 2 - Problem A2: Cottontail Climb (Part 2)
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-2/problems/A2
#
# Time:  precompute: O(17 * 73025424)
#        runtime:    O(73025424)
# Space: O(73025424)
#
# pass in PyPy3 but Python3
#

def cottontail_climb_part_2():
    A, B, M = list(map(int, input().split()))
    return sum(A <= x <= B for x in CANDIDATES if x%M == 0)

def backtracking(l, curr):
    if l == 0:
         return
    for i in range(curr%10 if curr else 1, 9+1):
        curr = curr*10+i
        HALF_CANDIDATES[-l].append(curr)
        backtracking(l-1, curr)
        curr //= 10

def reverse(x):
    result = 0
    while x:
        result = result*10+x%10
        x //= 10
    return result

MAX_L = 17
L = MAX_L//2
HALF_CANDIDATES = [[] for _ in range(L+1)]
backtracking(L, 0)
CANDIDATES = list(range(1, 9+1))
p = 1
for l in range(1, L+1):
    p *= 10
    for x in HALF_CANDIDATES[l]:
        for y in HALF_CANDIDATES[l]:
            mx = max(x%10, y%10)
            y = reverse(y)
            for i in range(mx+1, 9+1):
                CANDIDATES.append((x*10+i)*p+y)
assert(len(CANDIDATES) == 73025424)
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, cottontail_climb_part_2()))
