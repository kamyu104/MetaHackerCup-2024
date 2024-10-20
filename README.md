# [MetaHackerCup-2024](https://www.facebook.com/codingcompetitions/hacker-cup) ![Language](https://img.shields.io/badge/language-Python3-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE) ![Progress](https://img.shields.io/badge/progress-15%20%2F%215-ff69b4.svg) ![Visitors](https://visitor-badge.laobi.icu/badge?page_id=kamyu104.metahackercup.2024)

* Python3 solutions of Meta Hacker Cup 2024. Solution begins with `*` means it will get TLE in the largest data set.
* Total computation amount > `10^8`, which is not friendly for Python3 to solve in 5 ~ 15 seconds. A `6-minute` timer is set for uploading the result this year.
* A problem was marked as `Very Hard` means that it was an unsolved one during the contest and may not be that difficult.


## Rounds

* [Hacker Cup 2023](https://github.com/kamyu104/MetaHackerCup-2023)
* [Practice Round](https://github.com/kamyu104/MetaHackerCup-2024#practice-round)
* [Round 1](https://github.com/kamyu104/MetaHackerCup-2024#round-1)
* [Round 2](https://github.com/kamyu104/MetaHackerCup-2024#round-2)

## Practice Round
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Walk the Line](https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/A)| [Python3](./Practice%20Round/walk_the_line.py3) | _O(1)_ | _O(1)_ | Easy | | Greedy |
|B| [Line by Line](https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/B)| [Python3](./Practice%20Round/line_by_line.py3) | _O(1)_ | _O(1)_ | Easy | | Math |
|C| [Fall in Line](https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/C)| [Python3](./Practice%20Round/fall_in_line.py3) | _O(K * N)_ | _O(1)_ | Medium | | Randomized Algorithm |
|D1| [Line of Delivery (Part 1)](https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/D1)| [Python3](./Practice%20Round/line_of_delivery_part_1.py3) | _O(NlogN)_ | _O(1)_ | Medium | | Sort |
|D2| [Line of Delivery (Part 2)](https://www.facebook.com/codingcompetitions/hacker-cup/2024/practice-round/problems/D2)| [Python3](./Practice%20Round/line_of_delivery_part_2.py3) | _O(NlogN)_ | _O(1)_ | Hard | | Sort |

## Round 1
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Subsonic Subway](https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-1/problems/A)| [Python3](./Round%201/subsonic_subway.py3) | _O(N)_ | _O(1)_ | Easy | | Math |
|B| [Prime Subtractorization](https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-1/problems/B)| [Python3](./Round%201/prime_subtractorization.py3) | precompute: _O(MAX_N)_<br>runtime: _O(1)_ | _O(MAX_N)_ | Medium | | Number Theory, `Linear Sieve of Eratosthenes`, DP |
|C| [Substantial Losses](https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-1/problems/C)| [Python3](./Round%201/substantial_losses.py3) | _O(1)_ | _O(1)_ | Medium | | Expected Value |
|D| [Substitution Cipher](https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-1/problems/D)| [Python3](./Round%201/substitution_cipher.py3) | _O(N)_ | _O(1)_ | Hard | | Greedy, DP |
|E| [Wildcard Submissions](https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-1/problems/E)| [PyPy3](./Round%201/wildcard_submissions.py3) | _O(N * L * S)_ | _O(L * S)_ | Hard | | DP, Inclusion-Exclusion Principle |

## Round 2
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A1| [Cottontail Climb (Part 1)](https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-2/problems/A1)| [Python3](./Round%202/cottontail_climb_part_1.py3) | _O(285)_ | _O(45)_ | Easy | | Precomputation |
|A2| [Cottontail Climb (Part 2)](https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-2/problems/A2)| [PyPy3](./Round%202/cottontail_climb_part_2.py3) | precompute: _O(17 * 73025424)_<br>runtime: _O(73025424)_ | _O(73025424)_ | Easy | | Precomputation, Backtracking |
|B| [Four in a Burrow](https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-2/problems/B)| [PyPy3](./Round%202/four_in_a_burrow.py3) |  _O((R * C) * (R + 1)^C)_ | _O(C * (R + 1)^C)_ | Medium | | BFS |
|C| [Bunny Hopscotch](https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-2/problems/C)| [PyPy3](./Round%202/bunny_hopscotch.py3) |  _O((R * C * log(min(R, C))) * log(max(R, C)))_ | _O(R * C)_ | Medium | | Binary Search, Two Pointers, Sliding Window, BIT, Fenwick Tree |
|D| [Splitting Hares](https://www.facebook.com/codingcompetitions/hacker-cup/2024/round-2/problems/D)| [Python3](./Round%202/splitting_hares.py3) | _O(N + MAX_W^2)_ | _O(N + MAX_W)_ | Hard | | Greedy, DP, Backtracing |
