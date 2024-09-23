# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Practice Round - Problem D1. Line of Delivery 1
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/D1
#
# Time:  O(NlogN)
# Space: O(1)
#

def line_of_delivery_1():
    N, G = list(map(int, input().split()))
    a = [int(input()) for _ in range(N)]
    a.sort()
    result = min((abs(a[i]-G), N-i) for i in reversed(range(N)))
    return "%d %d" % (result[1], result[0])

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, line_of_delivery_1()))
