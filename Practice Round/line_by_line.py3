# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Practice Round - Problem B. Line by Line
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/B
#
# Time:  O(1)
# Space: O(1)
#

def line_by_line():
    N, P = list(map(int, input().split()))
    return (P/100)**((N-1)/N)*100-P

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, line_by_line()))
