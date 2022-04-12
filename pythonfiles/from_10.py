def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 14)
        nums.append(str(r))
    return ''.join(reversed(nums))

print(ternary(764839))
