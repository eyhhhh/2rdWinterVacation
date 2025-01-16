import random

# 밀러-라빈 소수 판별법
def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# 에라토스테네스의 체로 10^6 이하의 소수 구하기
def generate_primes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return primes

# 메인 함수
def main():
    primes = generate_primes(10**6)  # 10^6 이하의 소수 생성
    N = int(input())

    for _ in range(N):
        n = int(input())

        if is_prime(n):
            print("YES")
            continue

        # 소인수 검사: 10^6 이하의 소수로 나누어떨어지는지 확인
        has_small_prime_factor = False
        for p in primes:
            if p * p > n:  # p^2 > n이면 더 이상 검사할 필요 없음
                break
            if n % p == 0:
                has_small_prime_factor = True
                break

        if has_small_prime_factor:
            print("NO")
        else:
            print("YES")

# 실행
main()