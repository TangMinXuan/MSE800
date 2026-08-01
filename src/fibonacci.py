def get_nth_number(a: int, b: int, n: int) -> int:
    if n == 1:
        return a
    if n == 2:
        return b

    # dp stores already computed Fibonacci numbers (standard DP memoization)
    # Initialize base states F_0 = 0, F_1 = 1, F_2 = 1
    dp = {0: 0, 1: 1, 2: 1}

    # Define a top-down DP function to compute the k-th Fibonacci number
    def dp_fib(k: int) -> int:
        # If the state is already in the dp, return it directly (avoid redundant computation)
        if k in dp:
            return dp[k]

        # Reduce the problem size by half, using regular division instead of binary right shift
        m = k // 2

        # Recursively compute sub-states
        f_m = dp_fib(m)
        f_m_plus_1 = dp_fib(m + 1)

        # State transition equation (based on parity)
        if k % 2 == 0:
            # Even case: F_2m = F_m * (2 * F_m+1 - F_m)
            dp[k] = f_m * (2 * f_m_plus_1 - f_m)
        else:
            # Odd case: F_2m+1 = F_m^2 + F_m+1^2
            dp[k] = f_m ** 2 + f_m_plus_1 ** 2

        return dp[k]

    # Calculate result based on the derived general formula: S_n = F_{n-2} * a + F_{n-1} * b
    return dp_fib(n - 2) * a + dp_fib(n - 1) * b


# Test code
if __name__ == "__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    n = int(input("Enter n: "))
    print(get_nth_number(a, b, n))
