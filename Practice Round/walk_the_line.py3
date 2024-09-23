# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Practice Round - Problem A. Walk the Line
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/A
#
# Time:  O(N)
# Space: O(1)
#

def walk_the_line():
    N, K = list(map(int, input().split()))
    a = [int(input()) for _ in range(N)]
    return "YES" if min(a)*max((N-1)+(N-2), 1) <= K else "NO"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, walk_the_line()))
