# Copyright (c) 2024 kamyu. All rights reserved.
#
# Meta Hacker Cup 2024 Round 1 - Problem D. Substitution Cipher
# https:#www.facebook.com/codingcompetitions/hacker-cup/2024/round-1/problems/D
#
# Time:  O(N)
# Space: O(1)
#

def substitution_cipher():
    def kth_largest(K):
        for i in reversed(range(len(E))):
            if E[i] != '?':
                continue
            cnt = 1
            if i+1 == len(E) or (i+2 < len(E) and E[i+2] == '0'):
                if i-1 < 0 or E[i-1] not in ('?', '2'):
                    cnt = 9-1+1  # 1-9
                    E[i] = chr(ord('9')-K%cnt)
                elif E[i-1] == '2':
                    cnt = 6-1+1  # 1-6
                    E[i] = chr(ord('6')-K%cnt)
            elif E[i+1] == '?':
                cnt = (26-11+1)-1  # 11-19, 21-26
                q, r = divmod(26-K%cnt-int((26-K%cnt) <= 20), 10)
                E[i], E[i+1] = chr(ord('0')+q), chr(ord('0')+r)
            elif '0' <= E[i+1] <= '6':
                cnt = 2  # 1-2
                E[i] = chr(ord('2')-K%cnt)
            elif '7' <= E[i+1] <= '9':
                cnt = 1-1+1  # 1
                E[i] = '1'
            else:
                assert(False)
            K //= cnt
        assert(K == 0)

    def count():
        dp = [0]*3
        dp[0] = 1
        for i in range(len(E)):
            dp[(i+1)%3] = 0
            if E[i] != '0':
                dp[(i+1)%3] = (dp[(i+1)%3]+dp[i%3])%MOD
            if i-1 >= 0 and 10 <= int(E[i-1]+E[i]) <= 26:
                dp[(i+1)%3] = (dp[(i+1)%3]+dp[(i-1)%3])%MOD
        return dp[len(E)%3]

    E, K = input().split()
    E, K = list(E), int(K)
    kth_largest(K-1)
    return f"{''.join(E)} {count()}"

MOD = 998244353
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, substitution_cipher()))
