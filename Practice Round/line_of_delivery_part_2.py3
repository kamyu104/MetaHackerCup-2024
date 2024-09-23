# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Practice Round - Problem D2. Line of Delivery (Part 2)
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/D2
#
# Time:  O(NlogN)
# Space: O(1)
#

def line_of_delivery_part_2():
    N, G = list(map(int, input().split()))
    E = [int(input()) for _ in range(N)]
    for i in range(N):
        E[i] += i
    E.sort()
    for i in range(N):
        E[-1-i] -= i
    result = min((abs(E[i]-G), N-i) for i in reversed(range(N)))
    return "%d %d" % (result[1], result[0])

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, line_of_delivery_part_2()))
