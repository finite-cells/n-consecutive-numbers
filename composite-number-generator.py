import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.isqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_composite_sequence(n):
    # Start from (n+1)! + 2 to (n+1)! + (n+1)
    start = math.factorial(n + 1)
    composite_seq = []
    
    for i in range(2, n + 2):
        candidate = start + i
        assert not is_prime(candidate), f"{candidate} is somehow prime!"
        composite_seq.append(candidate)

    return composite_seq

# Example:
n = 10
composites = generate_composite_sequence(n)
print(f"{n} consecutive composite numbers:")
print(composites)
