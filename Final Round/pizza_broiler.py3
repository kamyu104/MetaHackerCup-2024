# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Final Round - Problem F. Pizza Broiler
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/final-round/problems/F
#
# Time:  O(W + NlogW), W = min(max(max(abs(x) for t in triangles for x, _ in t), R), max(max(abs(y) for t in triangles for _, y in t), R))
# Space: O(W)
#

def binary_search_right(left, right, check):
    while left <= right:
        mid = left + (right-left)//2
        if not check(mid):
            right = mid-1
        else:
            left = mid+1
    return right

def ccw(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def inner_product(a, b):
    return a[0]*b[0]+a[1]*b[1]

# modified template from: https://cp-algorithms.com/geometry/lattice_points.html
def count_lattices(a, b, c, n):  # sum((a*i+b)//c for i in range(n)), Time: O(logn)
    assert(n >= 1 and c >= 1)
    fa = a//c
    fb = b//c
    cnt = (fa*(n-1)+2*fb)*n//2
    a -= fa*c
    b -= fb*c
    t = a*n+b
    ft = t//c
    if ft >= 1:
        cnt += count_lattices(c, t-c*ft, a, ft)
    return cnt

def pizza_broiler():
    def count(v):
        def count_under_line(v1, v2, exclude):
            if v1 > v2:
                v1, v2 = v2, v1
            if v1[0] == v2[0]:  # vertical line
                cnt = f[v1[0]+w]
                return max(min(cnt, v1[1]-exclude)+cnt+1, 0) if cnt >= 0 else 0
            if inner_product(v1, v1) > R**2 and inner_product(v2, v2) > R**2:  # line(v1, v2) is outside circle
                x = 0
                if v1[0] > 0:
                    x = v1[0]
                elif v2[0] < 0:
                    x = v2[0]
                if ccw(v1, v2, [x, f[x+w]]) >= 0:  # line(v1, v2) is under circle
                    return 0
                # line(v1, v2) is above circle
                left, right = max(v1[0], -R), min(v2[0], R)
                return max(prefix1[(right+w)+1]-prefix1[left+w], 0)
            if inner_product(v1, v1) > R**2:  # make v1 inside circle
                v1, v2 = [-v2[0], v2[1]], [-v1[0], v1[1]]
            # y = (v2[1]-v1[1])/(v2[0]-v1[0])*(x-v1[0])+v1[1]
            # => (v2[0]-v1[0])*y =(v2[1]-v1[1])*(x-v1[0])+v1[1]*(v2[0]-v1[0])
            # => c*y = a*(x-v1[0])+b
            a, b, c = v2[1]-v1[1], v1[1]*(v2[0]-v1[0]), v2[0]-v1[0]
            left, right = v1[0], v2[0]
            right = binary_search_right(left, right, lambda x: (a*(x-v1[0])+b)**2 <= (R**2-x**2)*(c**2))
            result = (prefix2[(right+w)+1]-prefix2[left+w])+count_lattices(a, b-exclude, c, right-left+1)
            if a*((right+1)-left)+b > 0:  # outer vertex is above circle
                result += prefix1[(v2[0]+w)+1]-prefix1[(right+1)+w]
            return result

        v.sort()
        if v[0][0] == v[1][0]:  # a special case for vertical line
            v[0], v[1] = v[1], v[0]
        if ccw(v[0], v[2], v[1]) >= 0:
            return (count_under_line(v[0], v[1], 0)+count_under_line(v[1], v[2], 0)-count_under_line(v[1], v[1], 0))-count_under_line(v[0], v[2], 1)
        return count_under_line(v[0], v[2], 0)-(count_under_line(v[0], v[1], 1)+count_under_line(v[1], v[2], 1)-count_under_line(v[1], v[1], 1))

    N, R = list(map(int, input().split()))
    triangles = []
    for _ in range(N):
        x1, y1, x2, y2, x3, y3 = list(map(int, input().split()))
        triangles.append([[x1, y1], [x2, y2], [x3, y3]])
    w1 = max(max(abs(x) for t in triangles for x, _ in t), R)
    w2 = max(max(abs(y) for t in triangles for _, y in t), R)
    w = min(w1, w2)
    if w1 > w2:
        for t in triangles:
            for v in t:
                v[0], v[1] = v[1], v[0]
    f = [binary_search_right(0, R, lambda x: x**2 <= R**2-(i-w)**2) for i in range(2*w+1)]
    prefix1 = [0]*(len(f)+1)
    for i in range(len(f)):
        prefix1[i+1] = prefix1[i]+max(2*f[i]+1, 0)
    prefix2 = [0]*(len(f)+1)
    for i in range(len(f)):
        prefix2[i+1] = prefix2[i]+(f[i]+1)
    return sum(count(t) for t in triangles)%MOD

MOD = 10**9+7
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, pizza_broiler()))
