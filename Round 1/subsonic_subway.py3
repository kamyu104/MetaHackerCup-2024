# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Round 1 - Problem A. Subsonic Subway
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-1/problems/A
#
# Time:  O(N)
# Space: O(1)
#

def subsonic_subway():
    N = int(input())
    A_B = [list(map(int, input().split())) for _ in range(N)]
    a, b = 0, 1
    for i, (_, x) in enumerate(A_B, 1):
        if a*x < i*b:
            a, b = i, x
    c, d = 1, 0
    for i, (x, _) in enumerate(A_B, 1):
        if c*x > i*d:
            c, d = i, x
    return a/b if a*d <= c*b else -1

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, subsonic_subway()))
