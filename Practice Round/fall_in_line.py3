# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Practice Round - Problem C. Fall in Line
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/C
#
# Time:  O(K * N)
# Space: O(1)
#

from random import sample, seed

def ccw(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def fall_in_line():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for _ in range(K):
        i, j = sample(range(N), 2)
        result = max(result, sum(ccw(points[i], points[j], points[k]) == 0 for k in range(N)))
    return N-result

seed(0)
K = 10
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, fall_in_line()))
