# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Final Round - Problem E. Snake Cover
# https://www.facebook.com/codingcompetitions/hacker-cup/2024/final-round/problems/E
#
# Time:  O(M)
# Space: O(M)
#

from collections import deque

class MonoDeque:
    def __init__(self, cmp):
        self.head = self.tail = 0
        self.dq = deque()
        self.cmp = cmp

    def push(self, val):
        while self.dq and not self.cmp(self.dq[-1][0], val):
            self.dq.pop()
        self.dq.append([val, self.head])
        self.head += 1

    def pop(self):
        if self.dq[0][1] == self.tail:
            self.dq.popleft()
        self.tail += 1

    def top(self):
        return self.dq[0][0]

    def top2(self, val):
        if len(self.dq) >= 2 and not self.cmp(val, self.dq[1][0]):
            val = self.dq[1][0]
        return val

    def extend_head(self, val):
        self.dq.pop()
        self.head -= 1
        self.push(val)

    def trim_tail(self, val):
        if self.dq[0][1] != self.tail:
            return
        self.dq[0][0] = val
        if len(self.dq) >= 2 and not self.cmp(self.dq[0][0], self.dq[1][0]):
            self.dq.popleft()

class Segment:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def length(self):
        return abs(self.x2-self.x1)+abs(self.y2-self.y1)+1

    def dir(self):
        if self.x1 == self.x2:
            return UP if self.y1 > self.y2 else DOWN
        if self.y1 == self.y2:
            return RIGHT if self.x1 > self.x2 else LEFT

    def extend(self, l):
        if self.dir() == RIGHT:
            self.x1 += l
        elif self.dir() == UP:
            self.y1 += l
        elif self.dir() == LEFT:
            self.x1 -= l
        elif self.dir() == DOWN:
            self.y1 -= l

    def trim(self, l):
        if self.dir() == RIGHT:
            self.x2 += l
        elif self.dir() == UP:
            self.y2 += l
        elif self.dir() == LEFT:
            self.x2 -= l
        elif self.dir() == DOWN:
            self.y2 -= l

class Snake:
    def __init__(self, N):
        self.dq = deque()
        self.right = MonoDeque(lambda a, b: a >= b)
        self.up = MonoDeque(lambda a, b: a >= b)
        self.left = MonoDeque(lambda a, b: a <= b)
        self.down = MonoDeque(lambda a, b: a <= b)
        self.d = RIGHT
        self.push_head(Segment(N, 1, 1, 1))

    def insert(self, s):
        self.right.push(max(s.x1, s.x2))
        self.up.push(max(s.y1, s.y2))
        self.left.push(min(s.x1, s.x2))
        self.down.push(min(s.y1, s.y2))

    def erase(self):
        self.right.pop()
        self.up.pop()
        self.left.pop()
        self.down.pop()

    def extend(self, s):
        self.right.extend_head(max(s.x1, s.x2))
        self.up.extend_head(max(s.y1, s.y2))
        self.left.extend_head(min(s.x1, s.x2))
        self.down.extend_head(min(s.y1, s.y2))

    def trim(self, s):
        self.right.trim_tail(max(s.x1, s.x2))
        self.up.trim_tail(max(s.y1, s.y2))
        self.left.trim_tail(min(s.x1, s.x2))
        self.down.trim_tail(min(s.y1, s.y2))

    def head(self):
        return self.dq[0]

    def tail(self):
        return self.dq[-1]

    def dir(self):
        return self.d

    def turn_left(self):
        self.d = (self.d+1) % 4

    def turn_right(self):
        self.d = (self.d-1) % 4

    def min_x(self):
        return self.left.top()

    def max_x(self):
        return self.right.top()

    def min_y(self):
        return self.down.top()

    def max_y(self):
        return self.up.top()

    def min2_x(self, val):
        return self.left.top2(val)

    def max2_x(self, val):
        return self.right.top2(val)

    def min2_y(self, val):
        return self.down.top2(val)

    def max2_y(self, val):
        return self.up.top2(val)

    def min_area(self):
        return (self.max_x()-self.min_x()+1)*(self.max_y()-self.min_y()+1)

    def push_head(self, s):
        self.dq.appendleft(s)
        self.insert(s)

    def pop_tail(self):
        self.dq.pop()
        self.erase()

    def extend_head(self, l):
        s = self.head()
        if self.dir() == s.dir():
            s.extend(l)
            self.extend(s)
            return
        new_s = Segment(s.x1, s.y1, s.x1, s.y1)
        if self.dir() == RIGHT:
            new_s.x1 += l
        elif self.dir() == UP:
            new_s.y1 += l
        elif self.dir() == LEFT:
            new_s.x1 -= l
        elif self.dir() == DOWN:
            new_s.y1 -= l
        self.push_head(new_s)

    def trim_tail(self, l):
        s = self.tail()
        to_trim = min(l, s.length()-1)
        if to_trim == s.length()-1:
            self.pop_tail()
            return to_trim
        s.trim(to_trim)
        self.trim(s)
        return to_trim

    def head_to_border_length(self):
        s = self.head()
        if self.dir() == RIGHT:
            return self.max_x()-s.x1
        if self.dir() == UP:
            return self.max_y()-s.y1
        if self.dir() == LEFT:
            return s.x1-self.min_x()
        if self.dir() == DOWN:
            return s.y1-self.min_y()
        return 0

    def relevant_tail_len(self):
        s = self.tail()
        if s.dir() == RIGHT and s.x2 == self.min_x() and (mn2 := self.min2_x(s.x1)) > s.x2:
            return mn2-s.x2
        if s.dir() == UP and s.y2 == self.min_y() and (mn2 := self.min2_y(s.y1)) > s.y2:
            return mn2-s.y2
        if s.dir() == LEFT and s.x2 == self.max_x() and (mx2 := self.max2_x(s.x1)) < s.x2:
            return s.x2-mx2
        if s.dir() == DOWN and s.y2 == self.max_y() and (mx2 := self.max2_y(s.y1)) < s.y2:
            return s.y2-mx2
        return 0

    def slither(self, cnt):
        def move(n):
            if n <= 0:
                return
            n = min(n, cnt[0])
            while n:
                trimmed = self.trim_tail(n)
                self.extend_head(trimmed)
                n -= trimmed
                cnt[0] -= trimmed
                result[0] = min(result[0], self.min_area())

        def phase1():
            while cnt[0]:
                head_to_border = self.head_to_border_length()
                if not head_to_border:
                    break
                relevant = self.relevant_tail_len()
                irrelevant = self.tail().length()-relevant-1
                if relevant and self.dir() == (self.tail().dir()+2) % 4:
                    if self.dir() == RIGHT:
                        l = abs(self.head().x1-self.tail().x2)
                    elif self.dir() == UP:
                        l = abs(self.head().y1-self.tail().y2)
                    elif self.dir() == LEFT:
                        l = abs(self.head().x1-self.tail().x2)
                    elif self.dir() == DOWN:
                        l = abs(self.head().y1-self.tail().y2)
                    mid = (l+1)//2
                    if mid < relevant:
                        move(mid)
                        continue
                if head_to_border <= relevant:
                    move(head_to_border)
                    break
                move(relevant)
                head_to_border = self.head_to_border_length()
                if head_to_border <= irrelevant:
                    move(head_to_border)
                    break
                move(irrelevant)

        def phase2():
            while cnt[0]:
                relevant = self.relevant_tail_len()
                irrelevant = self.tail().length()-relevant-1
                if relevant:
                    move(1)
                move(relevant-1)
                if irrelevant:
                    move(1)
                move(irrelevant-1)

        result = [float("inf")]
        phase1()
        phase2()
        return result[0]

def snake_cover():
    N, M = list(map(int, input().split()))
    D_X = [list(input().split()) for _ in range(M)]
    snake = Snake(N)
    result = 0
    for D, X in D_X:
        X = int(X)
        if D == 'L':
            snake.turn_left()
        elif D == 'R':
            snake.turn_right()
        result = (result+snake.slither([X])) % MOD
    return result

RIGHT, UP, LEFT, DOWN = list(range(4))
MOD = 10**9+7
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, snake_cover()))
