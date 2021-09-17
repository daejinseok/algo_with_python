"""
바닥 공사

f(1) = |
f(2) = ||, -, ㅁ = 3
f(3) = | f(2)
       - f(1)
       ㅁ f(1)
f(4) = | f(3)
       - f(2)
       ㅁ f(2)

f(n) = f(n-1) + f(n-2) * 2
"""

def solution(n):

    if n == 1:
        return 1

    dp = [0] * n

    dp[0] = 1
    dp[1] = 3

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2] * 2
    
    return dp[n-1]


def main():
    assert solution(1) == 1
    assert solution(2) == 3
    assert solution(3) == 5
    assert solution(4) == 11
    assert solution(5) == 21

if __name__ == "__main__":
	main()
