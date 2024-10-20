# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Round 2 - Problem C: Bunny Hopscotch
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-2/problems/C
#
# Time:  O((R * C * log(min(R, C))) * log(max(R, C)))
# Space: O(R * C + min(R, C)) = O(R * C)
#
# pass in PyPy3 but Python3
#

class BIT(object):  # 0-indexed.
    def __init__(self, n):
        self.__bit = [0]*(n+1)  # Extra one for dummy node.

    def add(self, i, val):
        i += 1  # Extra one for dummy node.
        while i < len(self.__bit):
            self.__bit[i] += val
            i += (i & -i)

    def query(self, i):
        i += 1  # Extra one for dummy node.
        ret = 0
        while i > 0:
            ret += self.__bit[i]
            i -= (i & -i)
        return ret

def binary_search(left, right, check):
    while left <= right:
        mid = left + (right-left)//2
        if check(mid):
            right = mid-1
        else:
            left = mid+1
    return left

def bunny_hopscotch():
    def check(d):
        result = 0
        for group in groups:
            left = right = 0
            for i, j in group:
                l1 = max(i-d, 0)
                r1 = min(i+d, max(R, C)-1)
                l2 = max(j-d, 0)
                r2 = min(j+d, min(R, C)-1)
                while right < len(group) and group[right][0] <= r1:
                    bit.add(group[right][1], 1)
                    right += 1
                while group[left][0] < l1:
                    bit.add(group[left][1], -1)
                    left += 1
                result += (r1-l1+1)*(r2-l2+1)-(bit.query(r2)-bit.query(l2-1))
            while left < right:
                bit.add(group[left][1], -1)
                left += 1
        return result >= K

    R, C, K = list(map(int, input().split()))
    grid = [list(map(lambda x: int(x)-1, input().split())) for _ in range(R)]
    groups = [[] for _ in range(R*C)]
    for i in range(max(R, C)):
        for j in range(min(R, C)):
            groups[grid[i][j] if R > C else grid[j][i]].append((i, j))
    bit = BIT(min(R, C))
    return binary_search(1, max(R, C)-1, check)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, bunny_hopscotch()))
