# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Round 1 - Problem A. Subsonic Subway
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-1/problems/A
#
# Time:  O(N)
# Space: O(1)
#

def subsonic_subway():
    def check(i, a, j, b):
        return i*b <= j*a

    N = int(input())
    A_B = [list(map(int, input().split())) for _ in range(N)]
    x, y = 0, 1
    for i, (_, b) in enumerate(A_B, 1):
        if not check(i, b, x, y):
            x, y = i, b
    return x/y if all(check(x, y, i, a) for i, (a, _) in enumerate(A_B, 1)) else -1

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, subsonic_subway()))
