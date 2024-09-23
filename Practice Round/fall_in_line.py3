# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Practice Round - Problem C. Fall in Line
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/C
#
# Time:  O(K * N)
# Space: O(1)
#

from random import sample, seed

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def slope(dy, dx):
    g = gcd(dy, dx)
    return (dy//g, dx//g)

def fall_in_line():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for _ in range(K):
        i, j = sample(range(N), 2)
        s = slope(points[j][1]-points[i][1], points[j][0]-points[i][0])
        result = max(result, sum(k in (i, j) or slope(points[k][1]-points[i][1], points[k][0]-points[i][0]) == s for k in range(N)))
    return N-result

seed(0)
K = 10
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, fall_in_line()))
