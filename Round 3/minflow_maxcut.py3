# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Round 3 - Problem D: Min-flow Max-cut
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-3/problems/D
#
# Time:  O(N * logN * logM)
# Space: O(N)
#

from random import seed, random
from itertools import accumulate
from functools import reduce

class TreapNode:
    def __init__(self, key):
        self.key = key
        self.prior = random()
        self.left = None
        self.right = None

        # added
        self.size = 1
        self.total = key
        self.substract = 0

def get_size(x):
    return x.size if x else 0

def get_total(x):
    return x.total if x else 0

def get_substract(x):
    return x.substract if x else 0

def update(x):
    x.size = 1+get_size(x.left)+get_size(x.right)
    x.total = x.key+get_total(x.left)+get_total(x.right)
    x.substract = (get_substract(x.left)+get_substract(x.right)+get_size(x.right)*x.key+(get_size(x.right)+1)*get_total(x.left))%MOD
    return x

def split(t, key):
    if not t:
        return (None, None)
    if t.key >= key:
        left, right = split(t.left, key)
        t.left = right
        return (left, update(t))
    else:
        left, right = split(t.right, key)
        t.right = left
        return (update(t), right)

def split_by_size(t, size):
    if not t:
        return (None, None)
    if get_size(t.left) >= size:
        left, right = split_by_size(t.left, size)
        t.left = right
        return (left, update(t))
    else:
        left, right = split_by_size(t.right, size-1-get_size(t.left))
        t.right = left
        return (update(t), right)

def merge(left, right):
    if not left or not right:
        return left if left else right
    if left.prior > right.prior:
        left.right = merge(left.right, right)
        return update(left)
    else:
        right.left = merge(left, right.left)
        return update(right)

def insert(t, key):
    left, right = split(t, key)
    return merge(merge(left, TreapNode(key)), right)

def to_list(t):
    def inorder_traversal(u, cb):
        if not u:
            return
        inorder_traversal(u.left, cb)
        cb(u)
        inorder_traversal(u.right, cb)

    result = []
    inorder_traversal(t, lambda x: result.append(x.key))
    return result

def minflow_maxcut():
    def small_to_large_merge(t1, t2):
        def trim_total(t, total):
            if not t:
                return None
            if total < 0:
                return None
            if get_total(t.right) >= total:
                return trim_total(t.right, total)
            if get_total(t.right)+t.key >= total:
                new_t = TreapNode(total-get_total(t.right))
                new_t.right = t.right
                return update(new_t)
            t.left = trim_total(t.left, total-get_total(t.right)-t.key)
            return update(t)

        def merge_min(t1, t2):
            prefix1 = list(accumulate(reversed(to_list(t1)), initial=0))
            prefix2 = list(accumulate(reversed(to_list(t2)), initial=0))
            mns = [min(x, y) for x, y in zip(prefix1, prefix2)]
            diffs = [mns[i+1]-mns[i] for i in reversed(range(len(mns)-1))]
            return reduce(merge, (TreapNode(d) for d in diffs))

        if t1.size < t2.size:
            t1, t2 = t2, t1
        left, right = split_by_size(t1, t1.size-t2.size)
        left = trim_total(left, get_total(t2)-get_total(right))
        return merge(left, merge_min(right, t2))

    def iter_dfs():
        result = 0
        ret = [None]
        stk = [(1, (0, -1, ret))]
        while stk:
            step, args = stk.pop()
            if step == 1:
                u, p, ret = args
                stk.append((4, (u, ret)))
                stk.append((2, (u, p, 0, ret)))
            elif step == 2:
                u, p, i, ret = args
                if i == len(adj[u]):
                    continue
                v = adj[u][i]
                stk.append((2, (u, p, i+1, ret)))
                if v == p:
                    continue
                new_ret = [None]
                stk.append((3, (v, new_ret, ret)))
                stk.append((1, (v, u, new_ret)))
            elif step == 3:
                v, new_ret, ret = args
                ret[0] = small_to_large_merge(ret[0], new_ret[0]) if ret[0] else new_ret[0]
            elif step == 4:
                u, ret = args
                ret[0] = insert(ret[0], A[u])
                if get_size(ret[0]) > M:
                    ret[0] = split_by_size(ret[0], get_size(ret[0])-M)[1]
                result = (result+get_total(ret[0])*M-get_substract(ret[0]))%MOD
        return result

    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    U_V = [list(map(lambda x: int(x)-1, input().split())) for _ in range(N-1)]
    adj = [[] for _ in range(N)]
    for u, v in U_V:
        adj[u].append(v)
        adj[v].append(u)
    return iter_dfs()

seed(0)
MOD = 998244353
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, minflow_maxcut()))
